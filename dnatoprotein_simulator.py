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
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">

        <style>
        body, .stApp {
            background-color: #000000 !important;
            color: #00fff7 !important;
            font-family: 'Orbitron', sans-serif !important;
        }

        .fantasy-title {
            position: relative;
            font-size: 42px;
            text-align: center;
            padding: 12px 24px;
            color: #00fff7;
            border: 2px solid #00fff7;
            border-radius: 12px;
            background-color: #0a0a0a;
            text-shadow: 0 0 10px #00fff7;
            box-shadow: 0 0 25px #00fff7;
            font-weight: 700;
            overflow: hidden;
        }

        .fantasy-title::before, .fantasy-title::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            overflow: hidden;
            clip: rect(0, 900px, 0, 0);
            animation: glitch 2s infinite linear alternate-reverse;
        }

        .fantasy-title::after {
            color: #ff00cc;
            animation-delay: .3s;
        }

        @keyframes glitch {
            0% { clip: rect(42px, 9999px, 44px, 0); transform: skew(0.3deg); }
            5% { clip: rect(12px, 9999px, 58px, 0); transform: skew(0.5deg); }
            10% { clip: rect(85px, 9999px, 96px, 0); transform: skew(0.2deg); }
            15% { clip: rect(25px, 9999px, 32px, 0); transform: skew(0.6deg); }
            20% { clip: rect(44px, 9999px, 50px, 0); transform: skew(0.1deg); }
            100% { clip: rect(0, 9999px, 0, 0); transform: skew(0.3deg); }
        }

        .intro-scroll {
            background: linear-gradient(145deg, #1a1a1a, #0a0a0a);
            border: 2px solid #ff00cc;
            border-radius: 10px;
            padding: 20px;
            font-size: 16px;
            color: #ff00cc;
            text-shadow: 0 0 5px #ff00cc;
            box-shadow: 0 0 20px #ff00cc;
            text-align: center;
        }

        .stButton > button {
            background-color: #000000 !important;
            color: #00fff7 !important;
            border: 2px solid #00fff7 !important;
            font-family: 'Orbitron', sans-serif;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            text-shadow: 0 0 5px #00fff7;
            box-shadow: 0 0 15px #00fff7;
            transition: 0.3s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #0ff !important;
            color: #000 !important;
            box-shadow: 0 0 25px #0ff, 0 0 50px #0ff;
        }

        .stCodeBlock, .stCode {
            background-color: #111 !important;
            color: #00fff7 !important;
            font-family: 'Courier New', Courier, monospace;
            border-left: 3px solid #ff00cc;
            padding: 10px;
            box-shadow: inset 0 0 10px #ff00cc;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='fantasy-title' data-text='DNA to Protein Simulator'>DNA to Protein Simulator</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="intro-scroll">
            <strong>Welcome to the Bio-Synth Terminal.</strong><br><br>
            Input any phrase, and initiate molecular encoding — <br>
            from character input to DNA codification,<br>
            mutation injections, RNA synthesis, and protein rendering.<br><br>
            Your words become data. Data becomes code. Code becomes life.<br><br>
            <em>Press [ENGAGE] to initiate bio-sequence pipeline.</em>
        </div>
        """,
        unsafe_allow_html=True
    )

#     st.markdown("""
# <div style='text-align: left; color: #d4af37; font-size: 18px;'>
#     Explore the central dogma of molecular biology: <strong>DNA → RNA → Protein</strong>. 
#     <br>Input any text, and we’ll convert it into a simulated DNA sequence, introduce random mutations, transcribe it into RNA, 
#     and translate it into a chain of amino acids — the building blocks of proteins. Along the way, 
#     you'll get explanations of key biological processes and even a visualization of the resulting protein structure. 
#     Whether you're a student, researcher, or just curious, dive in and see your message come to life — molecule by molecule.
#     <br>
# </div>
# """, unsafe_allow_html=True)


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
