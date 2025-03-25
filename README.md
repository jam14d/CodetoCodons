# Code to Codons: Interactive Biology with Python

**Code to Codons** is a project dedicated to making biology concepts more accessible through interactive programming. This project consists of multiple Streamlit applications that explore different aspects of genetics, DNA mutations, and protein synthesis. Below are the two key applications in this project:

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

### Installation
To run BaseWarp locally, install Streamlit and run the script:
```sh
pip install streamlit
streamlit run basewarp.py
```

### Game Logic
- The template strand is randomly generated.
- The correct complementary strand is derived using base-pairing rules:
  - A <-> T
  - C <-> G
- The complementary strand is shuffled to introduce mutations.
- The player swaps bases until the sequence is restored.

---

## DNA Mutation & Protein Synthesis App

This web application simulates the process of DNA mutation, transcription, and translation into proteins. Users can input text, which is then converted into a DNA sequence, potentially mutated, transcribed into RNA, and finally translated into a protein sequence.

### Features
- **Text to DNA Conversion:** Convert input text into a simulated DNA sequence.
- **DNA Mutation:** Apply a mutation rate to the DNA sequence to simulate natural genetic variation.
- **RNA Transcription:** Transcribe the mutated DNA sequence into RNA.
- **Protein Translation:** Translate the RNA sequence into a chain of amino acids, forming a protein.
- **Hugging Face AI Integration:** Falcon-7B provides real-time explanations of biological processes like DNA replication, RNA transcription, and protein synthesis.

### Running the Application
To launch the application, run the following command:
```sh
streamlit run main.py
```
Ensure you have Streamlit installed and that you are in the correct project directory before executing the command.

### Usage
1. Input text in the text area.
2. Adjust the mutation rate using the slider.
3. Click **Let's Transcribe and Translate!** to process the sequence.
4. View the results:
   - **Original and Mutated DNA Sequences**
   - **RNA Sequence** (with highlighted stop codons)
   - **Protein Sequence** (amino acid chain)

---

## Future Enhancements
- Add difficulty levels to BaseWarp with different mutation rates.
- Implement a scoring system for BaseWarp based on swap count.
- Introduce animations for BaseWarp base swaps.
- Enhance the UI with a DNA helix visualization.
- Expand the DNA mutation app with more real-world mutation simulations.

## Credits
Developed using Python and Streamlit with custom CSS styling for an engaging experience.

**Code to Codons** aims to bridge biology and programming, making genetic concepts interactive and fun!

