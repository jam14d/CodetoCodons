import streamlit as st
import random
import re
import requests
import time  
import os

from pipeline import Pipeline
from string_reader import StringReader
from character_capitalizer import CharacterCapitalizer
from dna_base_converter import DNABaseConverter
from space_remover import SpaceRemover
from special_characters_remover import SpecialCharactersRemover
from draw_molecules import generate_amino_acid_image
from protein_synthesis import translate_rna_to_protein


def app():
    # Inject Custom CSS
    st.markdown("""
    <style>
    html, body, [class*="st"] {
        background-color: #282425;
        color: #a8e6cf;
        font-family: 'Orbitron', sans-serif;
    }

    .big-title-glow {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #ffcc66;
        text-shadow: 0 0 50px #ff9966, 0 0 50px #ffcc66, 0 0 50px #ff6633;
        animation: flicker-big 1.5s infinite alternate;
    }

    .title-glow {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: #88c0d0;
        text-shadow: 0 0 10px #88c0d0, 0 0 15px #6fa3bf, 0 0 20px #5790af;
        animation: flicker 1.5s infinite alternate;
    }

    @keyframes flicker-big {
        0% { opacity: 1; text-shadow: 0 0 25px #ff9966; }
        50% { opacity: 0.9; text-shadow: 0 0 40px #ffcc66; }
        100% { opacity: 1; text-shadow: 0 0 25px #ff9966; }
    }

    @keyframes flicker {
        0% { opacity: 1; text-shadow: 0 0 20px #88c0d0; }
        50% { opacity: 0.9; text-shadow: 0 0 25px #6fa3bf; }
        100% { opacity: 1; text-shadow: 0 0 20px #88c0d0; }
    }

    .neon-box {
        background-color: rgba(38, 34, 35, 0.9);
        border: 2px solid #88c0d0;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 0px 15px #88c0d0;
        margin: auto;
        max-width: 900px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)


API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

if HF_TOKEN is None:
    raise ValueError("❌ Error: Hugging Face API token is missing! Set it as an environment variable.")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_llm(prompt, retries=3):
    for attempt in range(retries):
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

        if response.status_code == 200:
            try:
                data = response.json()
                full_response = data[0].get("generated_text", "No response text.") if isinstance(data, list) else data.get("generated_text", "No response text.")
                cleaned_response = re.sub(r'[^\x00-\x7F]+', '', full_response.replace(prompt, "").strip())
                return cleaned_response
            except requests.exceptions.JSONDecodeError:
                return "Error: Response was not in JSON format."

        elif response.status_code in [503, 429]:
            wait_time = 10 if response.status_code == 503 else 30
            time.sleep(wait_time)

    return "API is currently unavailable. Please try again later."


def mutate_dna(dna_sequence, mutation_rate):
    dna_list = list(dna_sequence)
    mutations_occurred = False
    for i in range(len(dna_list)):
        if random.random() < mutation_rate:
            mutations = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
            dna_list[i] = random.choice(mutations[dna_list[i]])
            mutations_occurred = True
    return ''.join(dna_list), mutations_occurred

def transcribe_dna_to_rna(dna_sequence):
    return dna_sequence.replace('T', 'U')

def run_pipeline(input_string, mutation_rate=0, prepend_start_codon=False):
    pipeline = Pipeline()
    pipeline.add(StringReader())
    pipeline.add(CharacterCapitalizer())
    pipeline.add(DNABaseConverter())
    pipeline.add(SpaceRemover())
    pipeline.add(SpecialCharactersRemover())

    original_dna_output = pipeline.execute(input_string)
    if prepend_start_codon:
        original_dna_output = 'ATG' + original_dna_output

    mutated_dna_output, mutations_occurred = mutate_dna(original_dna_output, mutation_rate)
    return original_dna_output, mutated_dna_output, mutations_occurred

def app():
        # App Title
    st.markdown("""
    <div class="neon-box">
        <h1 class="big-title-glow">DNA to Protein Simulator</h1>
        <hr style="border: 2px solid #ffcc66; box-shadow: 0px 0px 50px #ffcc66;">
        <p class="title-glow">Transcribe, Translate & Visualize Genetic Sequences</p>
    </div>
    """, unsafe_allow_html=True)

    user_input = st.text_area("Enter your text to convert into DNA:", "Type your text here...")
    mutation_rate = st.slider("Mutation rate (in percentage):", min_value=0.0, max_value=100.0, value=0.0, step=0.1) / 100
    prepend_start_codon = st.checkbox("Prepend 'ATG' to DNA sequence", value=False)

    if st.button("Let's Transcribe and Translate!"):
        if user_input:
            original_dna, mutated_dna, mutations_occurred = run_pipeline(user_input, mutation_rate, prepend_start_codon)

            st.subheader("Your DNA Adventure Begins!")
            st.code(original_dna, language="plaintext")

            with st.spinner("Thinking of a cool explanation..."):
                explanation_dna = query_llm("Explain DNA in a fun and simple way.")
            st.markdown("**DNA: The Blueprint**")
            st.write(explanation_dna)

            st.code(mutated_dna, language="plaintext")

            with st.spinner("Unraveling the mystery of mutations..."):
                explanation_mutation = query_llm("Describe DNA mutations using a construction blueprint analogy.")
            st.markdown("**Mutations: Altering The Blueprint**")
            st.write(explanation_mutation)

            rna_output = transcribe_dna_to_rna(mutated_dna)
            st.code(rna_output, language="plaintext")

            with st.spinner("Writing the script for transcription..."):
                explanation_transcription = query_llm("Explain DNA transcription using a copy machine analogy.")
            st.markdown("**Transcription: A Copy Machine**")
            st.write(explanation_transcription)

            if not original_dna.startswith("ATG"):
                st.warning("⚠️ Your original DNA doesn't start with 'ATG'. No translation will happen.")
                return

            protein_sequence, stop_codon_present = translate_rna_to_protein(rna_output)
            st.code(protein_sequence, language="plaintext")

            if protein_sequence:
                with st.spinner("Generating 2D molecular structures..."):
                    image_path = generate_amino_acid_image(protein_sequence)
                if image_path and os.path.exists(image_path):
                    st.image(image_path, caption="2D Structure of Amino Acids", use_container_width=True)
                else:
                    st.error("Could not generate amino acid structure image.")

            with st.spinner("Decoding the protein-making process..."):
                explanation_translation = query_llm("Describe translation (mRNA to protein) using a factory analogy.")
            st.markdown("**Translation: The Protein Factory!**")
            st.write(explanation_translation)

        else:
            st.error("Please enter a DNA sequence to start the process!")
