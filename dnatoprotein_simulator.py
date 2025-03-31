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

def app():
    # Inject Updated Custom CSS
    st.markdown("""
    <style>
    html, body, [class*="st"] {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        font-family: 'Orbitron', sans-serif;
        color: #d8f3dc;
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        backdrop-filter: blur(15px);
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        margin: auto;
        max-width: 850px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .futuristic-title {
        font-size: 45px;
        font-weight: 700;
        text-align: center;
        color: #80deea;
        text-shadow: 0px 0px 15px #29b6f6;
        letter-spacing: 2px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        color: #c3e88d;
        text-shadow: 0px 0px 10px #a5d6a7;
    }

    .monospace-code {
        font-family: 'Courier New', monospace;
        background: rgba(0, 0, 0, 0.3);
        color: #80deea;
        border-radius: 8px;
        padding: 8px;
    }

    .button-glass {
        background: linear-gradient(135deg, #29b6f6, #00838f);
        border-radius: 8px;
        color: white;
        font-weight: bold;
        padding: 10px 15px;
        text-transform: uppercase;
        box-shadow: 0px 0px 10px #29b6f6;
        transition: 0.3s;
    }

    .button-glass:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 20px #29b6f6;
    }

    .neon-hover:hover {
        transform: scale(1.02);
        transition: 0.3s;
        text-shadow: 0 0 10px #29b6f6;
    }

    .sidebar-custom {
        background: rgba(255, 255, 255, 0.1) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown("""
    <div class="glass-box">
        <h1 class="futuristic-title neon-hover">DNA to Protein Simulator</h1>
        <hr style="border: 2px solid #80deea; box-shadow: 0px 0px 10px #80deea;">
        <p class="section-title">Transcribe, Translate & Visualize Genetic Sequences</p>
    </div>
    """, unsafe_allow_html=True)

    # User Input
    user_input = st.text_area("Enter your text to convert into DNA:", "Type your text here...")
    mutation_rate = st.slider("Mutation rate (in percentage):", min_value=0.0, max_value=100.0, value=0.0, step=0.1) / 100
    prepend_start_codon = st.checkbox("Prepend 'ATG' to DNA sequence", value=False)

    if st.button("Let's Transcribe and Translate!", key="process", help="Click to start the DNA transcription and translation process", 
                 args=(), kwargs={}, on_click=None, disabled=False):
        if user_input:
            original_dna = user_input.upper().replace(" ", "")
            mutated_dna, mutations_occurred = mutate_dna(original_dna, mutation_rate)

            st.markdown("### Your DNA Adventure Begins!")
            st.markdown(f"<div class='monospace-code'>{original_dna}</div>", unsafe_allow_html=True)

            st.markdown("### Mutated DNA:")
            st.markdown(f"<div class='monospace-code'>{mutated_dna}</div>", unsafe_allow_html=True)

            rna_output = transcribe_dna_to_rna(mutated_dna)
            st.markdown("### Transcribed RNA:")
            st.markdown(f"<div class='monospace-code'>{rna_output}</div>", unsafe_allow_html=True)

            if not original_dna.startswith("ATG"):
                st.warning("⚠️ Your original DNA doesn't start with 'ATG'. No translation will happen.")
                return

            protein_sequence, _ = translate_rna_to_protein(rna_output)
            st.markdown("### Translated Protein:")
            st.markdown(f"<div class='monospace-code'>{protein_sequence}</div>", unsafe_allow_html=True)

            if protein_sequence:
                with st.spinner("Generating 2D molecular structures..."):
                    image_path = generate_amino_acid_image(protein_sequence)
                if image_path and os.path.exists(image_path):
                    st.image(image_path, caption="2D Structure of Amino Acids", use_container_width=True)
                else:
                    st.error("Could not generate amino acid structure image.")

        else:
            st.error("Please enter a DNA sequence to start the process!")

# Run the app
app()
