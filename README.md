# Code to Codons: Interactive Biology Web Application

**Code to Codons** is a project dedicated to making biology concepts more accessible. This project consists of a Streamlit application that explores different aspects of genetics, DNA mutations, and protein synthesis. 

- [Live App](https://codetocodons.streamlit.app/)
- [Watch Demo](https://streamable.com/3nef8x)

---
## BaseWarp

BaseWarp is an interactive DNA repair game built using Streamlit. In this game, a DNA strand has been mutated, and your task is to swap bases on the complementary strand until it correctly pairs with the template strand.

### Features
- Randomly generated DNA template strand.
- Complementary strand with shuffled mutations.
- Interactive swapping mechanism to correct mutations.
- Stylish UI with CSS-enhanced elements.
- Sidebar controls for checking the answer and restarting the game.

### How to Play
1. Observe the **Template DNA Strand** displayed at the top.
2. The **Complementary Strand** below has mutations; bases are misplaced.
3. Click on two bases to swap their positions.
4. Keep swapping until the strand correctly pairs with the template.
5. Click **Check Answer** in the sidebar to verify your solution.
6. If correct, you win! Otherwise, try again.
7. Click **Play Again** to restart with a new DNA sequence.

### Game Logic
- The template strand is randomly generated.
- The correct complementary strand is derived using base-pairing rules:
  - A <-> T
  - C <-> G
- The complementary strand is shuffled to introduce mutations.
- The player swaps bases until the sequence is restored.

---

## Bio-Synthesis Simulator

This web application simulates the process of DNA mutation, transcription, and translation into proteins. Users can input text, which is then converted into a DNA sequence, potentially mutated, transcribed into RNA, and finally translated into a protein sequence.

### Features
- **Text to DNA Conversion:** Convert input text into a simulated DNA sequence.
- **DNA Mutation:** Apply a mutation rate to the DNA sequence to simulate natural genetic variation.
- **RNA Transcription:** Transcribe the mutated DNA sequence into RNA.
- **Protein Translation:** Translate the RNA sequence into a chain of amino acids, forming a protein.
- **Hugging Face AI Integration:** Falcon-7B provides real-time explanations of biological processes like DNA replication, RNA transcription, and protein synthesis.

### Usage
1. Input text in the text area.
2. Adjust the mutation rate using the slider.
3. Click **Let's Transcribe and Translate!** to process the sequence.
4. View the results:
   - **Original and Mutated DNA Sequences**
   - **RNA Sequence** (with highlighted stop codons)
   - **Protein Sequence** (amino acid chain)

---

## Mutation Explorer

The **Mutation Explorer** is for detecting and visualizing mutations in genome sequences. It compares two FASTA files — a reference genome and a variant genome — to identify **Single Nucleotide Polymorphisms (SNPs)** and displays them.

### Features
- Upload **FASTA** files for both reference and variant genomes.
- Detect SNPs through base-by-base comparison.
- View genome lengths and total mutation count.
- Explore SNP data through:
  - **Histogram** of mutation positions.
  - **Pie chart** showing transitions vs transversions.

### How to Use
1. Upload your **Reference Genome** and **Variant Genome** FASTA files using the sidebar.
2. Once uploaded, the app:
   - Parses and compares the sequences.
   - Highlights mismatches as SNPs.
   - Displays results interactively.
3. Use the visualizations to analyze mutation distribution and classification.

### Applications
- Educational exploration of genome variation.
- Small-scale mutation analysis.
- Introductory bioinformatics teaching tool.

