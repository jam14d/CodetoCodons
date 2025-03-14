# Code to Codons: Developing a Python Web App for DNA Mutation and Protein Synthesis

## Overview
This web application, built with Streamlit, simulates the process of DNA mutation, transcription, and translation into proteins. Users can input text, which is then converted into a DNA sequence, potentially mutated, transcribed into RNA, and finally translated into a protein sequence.

🤖 Hugging Face AI Integration with Falcon-7B
To make learning more interactive, the app integrates Hugging Face’s Falcon-7B Large Language Model (LLM) to generate real-time explanations about biological processes such as DNA replication, RNA transcription, and protein synthesis.

## Features
- **Text to DNA Conversion:** Convert input text into a simulated DNA sequence.
- **DNA Mutation:** Apply a mutation rate to the DNA sequence to simulate natural genetic variation.
- **RNA Transcription:** Transcribe the mutated DNA sequence into RNA.
- **Protein Translation:** Translate the RNA sequence into a chain of amino acids, forming a protein.

## How to run the application:
streamlit run main.py

## Usage
Upon launching the application, you will see a text area where you can input your text. After inputting the text, use the slider to set the mutation rate and press the "Let's Transcribe and Translate!" button to see the results:

- **Original and Mutated DNA Sequences:** Displays the original and mutated DNA sequences based on your input and selected mutation rate.
- **RNA Sequence:** Shows the RNA sequence with highlighted stop codons.
- **Protein Sequence:** Displays the sequence of amino acids that form the protein.

## Modules
- pipeline.py: Handles the processing pipeline for converting text to DNA and applying genetic operations.
- string_reader.py: Reads the input string and prepares it for further processing.
- character_capitalizer.py: Converts characters in the string to uppercase.
- dna_base_converter.py: Converts the string into a DNA sequence based on a predefined mapping.
- space_remover.py: Removes spaces from the string to ensure continuous DNA sequence.
- special_characters_remover.py: Removes special characters to maintain valid DNA bases.
