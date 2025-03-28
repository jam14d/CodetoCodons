import streamlit as st
import random
import re
import requests
import time  # Added for retries
import os

from pipeline import Pipeline
from string_reader import StringReader
from character_capitalizer import CharacterCapitalizer
from dna_base_converter import DNABaseConverter
from space_remover import SpaceRemover
from special_characters_remover import SpecialCharactersRemover
from draw_molecules import generate_amino_acid_image
from protein_synthesis import translate_rna_to_protein


#import streamlit.components.v1 as components
#from visualizer import show_3d_protein




# Hugging Face API Setup
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

# Retrieve the token from an environment variable
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Ensure the token exists to prevent errors
if HF_TOKEN is None:
    raise ValueError("❌ Error: Hugging Face API token is missing! Set it as an environment variable.")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}


def query_llm(prompt, retries=3):
    """Queries Hugging Face API with improved prompts and character filtering."""
    for attempt in range(retries):
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

        if response.status_code == 200:
            try:
                data = response.json()
                if isinstance(data, list) and len(data) > 0:
                    full_response = data[0].get("generated_text", "No response text.")
                elif isinstance(data, dict):
                    full_response = data.get("generated_text", "No response text.")
                else:
                    return "Error: Unexpected response format."

                # **Ensure the response doesn't include strange characters**
                cleaned_response = full_response.replace(prompt, "").strip()
                
                # Remove any non-ASCII characters (fixes weird output)
                cleaned_response = re.sub(r'[^\x00-\x7F]+', '', cleaned_response)

                return cleaned_response

            except requests.exceptions.JSONDecodeError:
                return "Error: Response was not in JSON format."

        elif response.status_code == 503:
            print(f"⚠️ Server unavailable. Retrying in 10 seconds... ({attempt+1}/{retries})")
            time.sleep(10)  # Wait before retrying

        elif response.status_code == 429:
            print("⚠️ Rate limit exceeded. Waiting 30 seconds...")
            time.sleep(30)

        else:
            return f"Error: API call failed with status code {response.status_code}"

    return "API is currently unavailable. Please try again later."



def mutate_dna(dna_sequence, mutation_rate):
    """Mutates the given DNA sequence based on the mutation rate."""
    dna_list = list(dna_sequence)
    mutations_occurred = False
    for i in range(len(dna_list)):
        if random.random() < mutation_rate:
            mutations = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
            base_to_mutate = dna_list[i]
            mutated_base = random.choice(mutations[base_to_mutate])
            dna_list[i] = mutated_base
            mutations_occurred = True
    return ''.join(dna_list), mutations_occurred

def transcribe_dna_to_rna(dna_sequence):
    """Transcribes DNA sequence into RNA by replacing all instances of 'T' with 'U'."""
    return dna_sequence.replace('T', 'U')

def run_pipeline(input_string, mutation_rate=0, prepend_start_codon=False):
    """
    Runs the transformation pipeline on an input string and applies mutations if specified.
    Optionally prepends 'ATG' to simulate a start codon.
    """
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

# Streamlit UI
st.title('🧬 DNA to Protein Simulator')

user_input = st.text_area("Enter your text to convert into DNA:", "Type your text here...")
mutation_rate = st.slider("Mutation rate (in percentage):", min_value=0.0, max_value=100.0, value=0.0, step=0.1) / 100
prepend_start_codon = st.checkbox("Prepend 'ATG' to DNA sequence", value=False)

if st.button("Let's Transcribe and Translate!"):
    if user_input:
        # Generate and mutate DNA
        original_dna, mutated_dna, mutations_occurred = run_pipeline(user_input, mutation_rate, prepend_start_codon)

        st.subheader("Your DNA Adventure Begins!")
        st.text("Original DNA Sequence (Before Mutation):")
        st.code(original_dna, language="plaintext")

        with st.spinner("Thinking of a cool explanation..."):
            explanation_dna = query_llm(
                "Explain DNA in a fun and simple way, like how blueprints guide building construction."
            )

        st.markdown("**DNA: The Blueprint**")
        st.write(explanation_dna)

        st.text("Mutated DNA Sequence:")
        st.code(mutated_dna, language="plaintext")

        with st.spinner("Unraveling the mystery of mutations..."):
            explanation_mutation = query_llm(
                "Describe what mutations in DNA. Then describe it as changing the blueprint for construction."
            )

        st.markdown("**Mutations: Altering The Blueprint**")
        st.write(explanation_mutation)

        # Transcribe to RNA
        rna_output = transcribe_dna_to_rna(mutated_dna)
        st.text("Resulting mRNA Sequence:")
        st.code(rna_output, language="plaintext")

        with st.spinner("Writing the script for transcription..."):
            explanation_transcription = query_llm(
    "Explain the biological process of transcription, where DNA is converted into mRNA."
    "Keep the explanation concise, engaging, and scientifically accurate, suitable for someone new to genetics."
    "Then, use a copy machine analogy to explain it in an engaging way"
)


        st.markdown("**Transcription: A Copy Machine**")
        st.write(explanation_transcription)

        # Check for 'ATG' start codon
        if not original_dna.startswith("ATG"):
            st.warning("⚠️ Oops! Your original DNA doesn't start with 'ATG'. No translation will happen.")

            with st.spinner("🤔 Understanding the impact of missing an ATG..."):
                explanation_atg_missing= query_llm(
                    "Explain what happens if the ATG start codon in a DNA sequence is not available. "
                    "Then, use an analogy to explain it in an engaging way.")
            
                st.markdown("**What Happens When ATG is Missing?**")
                st.write(explanation_atg_missing)  # **This line ensures the explanation is displayed!**


        elif mutated_dna[:3] != "ATG":
            st.warning("⚠️ Uh-oh! The ATG start codon got mutated during Transcription. Translation is canceled.")

            with st.spinner("🤔 Understanding the impact of losing ATG..."):
                explanation_atg_mutation = query_llm(
                    "Explain what happens if the ATG start codon in a DNA sequence is mutated during Transcription. "
                    "Then, use an analogy to explain it in an engaging way."
                )

            st.markdown("**What Happens When ATG Gets Mutated?**")
            st.write(explanation_atg_mutation)
        else:
            # Translate RNA to protein
            protein_sequence, stop_codon_present = translate_rna_to_protein(rna_output)
            
            if stop_codon_present:
                st.text("Stop codon detected! Translation stops here.")

            st.text("Translated Protein Sequence:")
            st.code(protein_sequence, language="plaintext")

            if protein_sequence:
                with st.spinner("Generating 2D molecular structures..."):
                    image_path = generate_amino_acid_image(protein_sequence)
                
                if image_path and os.path.exists(image_path):
                    st.image(image_path, caption="2D Structure of Amino Acids", use_container_width=True)
                else:
                    st.error("Could not generate amino acid structure image.")
            else:
                st.error("Please enter a DNA sequence to start the process!")

            with st.spinner("Decoding the protein-making process..."):
                explanation_translation = query_llm(
                    "Describe translation (mRNA to protein). Then, use a factory analogy to explain it in an engaging way."
                )

            st.markdown("**Translation: The Protein Factory!**")
            st.write(explanation_translation)
    else:
        st.error("Please enter a DNA sequence to start the process!")


