# Code to Codons: Developing a Python Web App for DNA Mutation and Protein Synthesis

## Overview
This is a web application designed to simulate the process of DNA mutation, transcription, and translation into proteins. This tool allows users to input a text, which is then converted into a DNA sequence, potentially mutated, transcribed into RNA, and finally translated into a protein sequence.

## Features
- **Text to DNA Conversion:** Convert input text into a simulated DNA sequence.
- **DNA Mutation:** Apply a mutation rate to the DNA sequence to simulate natural genetic variation.
- **RNA Transcription:** Transcribe the mutated DNA sequence into RNA.
- **Protein Translation:** Translate the RNA sequence into a chain of amino acids, forming a protein.

## Prerequisites
Before you begin, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/). This project assumes you are using Python Python 3.11.7.

## Installation Steps
To run the app, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jam14d/Projects/CodetoCodons.git
   
2. **Navigate to the directory where dnatoprotein.py is located**
   ```bash
   cd CodetoCodons

3. **Install Virtualenv:**
   ```bash 
    pip install virtualenv

4. **Create the environment:**
    ```bash 
    virtualenv tensorflow_env

5. **On macOS and Linux, activate it:**
    ```bash 
    source tensorflow_env/bin/activate

6.  **Install packages**
    ```bash 
    pip install  tensorflow tensorflow-hub numpy Pillow requests streamlit matplotlib seaborn plotly scikit-learn

7. **Run the application** 
    ```bash 
    streamlit run dnatoprotein.py

## Usage
Upon launching the application, you will see a text area where you can input your text. After inputting the text, use the slider to set the mutation rate and press the "Transcribe and Translate" button to see the results:

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
