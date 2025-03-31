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

# Inject Custom CSS for Sci-Fi Styling
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

# API Configuration
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# App Title
st.markdown("""
<div class="neon-box">
    <h1 class="big-title-glow">DNA to Protein Simulator</h1>
    <hr style="border: 2px solid #ffcc66; box-shadow: 0px 0px 50px #ffcc66;">
    <p class="title-glow">Transcribe, Translate & Visualize Genetic Sequences</p>
</div>
""", unsafe_allow_html=True)

# Input Fields
user_input = st.text_area("Enter your text to convert into DNA:", "Type your text here...")
mutation_rate = st.slider("Mutation rate (in percentage):", min_value=0.0, max_value=100.0, value=0.0, step=0.1) / 100
prepend_start_codon = st.checkbox("Prepend 'ATG' to DNA sequence", value=False)

if st.button("Let's Transcribe and Translate!"):
    if user_input:
        pipeline = Pipeline()
        pipeline.add(StringReader())
        pipeline.add(CharacterCapitalizer())
        pipeline.add(DNABaseConverter())
        pipeline.add(SpaceRemover())
        pipeline.add(SpecialCharactersRemover())

        original_dna = pipeline.execute(user_input)
        if prepend_start_codon:
            original_dna = 'ATG' + original_dna

        mutated_dna, mutations_occurred = ''.join(random.choice('ACGT') if random.random() < mutation_rate else base for base in original_dna), False
        st.markdown(f"<div class='neon-box'><h4 class='title-glow'>Original DNA</h4><code>{original_dna}</code></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='neon-box'><h4 class='title-glow'>Mutated DNA</h4><code>{mutated_dna}</code></div>", unsafe_allow_html=True)

        rna_output = mutated_dna.replace('T', 'U')
        st.markdown(f"<div class='neon-box'><h4 class='title-glow'>RNA Output</h4><code>{rna_output}</code></div>", unsafe_allow_html=True)

        protein_sequence, stop_codon_present = translate_rna_to_protein(rna_output)
        st.markdown(f"<div class='neon-box'><h4 class='title-glow'>Protein Sequence</h4><code>{protein_sequence}</code></div>", unsafe_allow_html=True)

        if protein_sequence:
            image_path = generate_amino_acid_image(protein_sequence)
            if image_path and os.path.exists(image_path):
                st.image(image_path, caption="2D Structure of Amino Acids", use_column_width=True)

        st.markdown("""
        <div class='neon-box'>
            <h4 class='title-glow'>Process Summary</h4>
            <p class='title-glow'>Your DNA has been transcribed and translated successfully!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Please enter a DNA sequence to start the process!")
