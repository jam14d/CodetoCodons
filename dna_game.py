import streamlit as st
import random

class DNAGame:
    base_pairing = {"A": "T", "T": "A", "C": "G", "G": "C"}
    nucleotides = ["A", "T", "C", "G"]

    def __init__(self, length=6, mutation_rate=0.3):
        self.length = length
        self.mutation_rate = mutation_rate
        self.template_strand = self.generate_dna()
        self.correct_strand = [self.base_pairing[base] for base in self.template_strand]
        self.mutated_strand = self.introduce_mutations()
        self.selected = None

    def generate_dna(self):
        return ''.join(random.choices(self.nucleotides, k=self.length))

    def introduce_mutations(self):
        mutated_seq = list(self.correct_strand)
        while True:
            random.shuffle(mutated_seq)
            if mutated_seq != self.correct_strand:
                break
        return mutated_seq


    def swap_bases(self, idx1, idx2):
        self.mutated_strand[idx1], self.mutated_strand[idx2] = (
            self.mutated_strand[idx2], self.mutated_strand[idx1])

    def check_answer(self):
        return self.mutated_strand == self.correct_strand

# Initialize game in session state
if "dna_game" not in st.session_state:
    st.session_state.dna_game = DNAGame()

game = st.session_state.dna_game

# UI and interaction logic
st.markdown("""
    <div style="background-color: #1e1e1e; padding: 10px; border-radius: 10px; color: #ffffff; text-align: center; box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.5); max-width: 900px; margin: auto;">
        <h1 style="color: #00e6e6;">BaseWarp</h1>
        <hr style="border: 1px solid #00e6e6;">
        <h3 style="color: #00b3b3;">Mutations have occurred!</h3>
        <p style="color: #00b3b3; font-size: 20px; font-weight: 500;">
  Click two bases on your complementary strand to swap their positions. Your goal is to correctly pair each nucleotide on your strand with its complement on the template to rebuild the DNA double helix!
</p>

</div>
""", unsafe_allow_html=True)

st.header("Template DNA:")
st.markdown("""
    <style>.dna-box { font-size: 30px; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; border-radius: 8px; border: 3px solid #ffcc33; background-color: #1e1e1e; color: #ffcc33; box-shadow: 0px 0px 15px rgba(230, 184, 0, 0.6); }</style>
""", unsafe_allow_html=True)

st.markdown('<div style="display:flex;justify-content:center;gap:10px;">' +
            ''.join(f'<div class="dna-box">{b}</div>' for b in game.template_strand) +
            '</div>', unsafe_allow_html=True)

st.header("Complementary Strand:")
cols = st.columns(game.length)

for i, col in enumerate(cols):
    with col:
        if st.button(game.mutated_strand[i], key=f"btn_{i}"):
            if game.selected is None:
                game.selected = i
            else:
                game.swap_bases(game.selected, i)
                game.selected = None
                st.rerun()

# Check answer button
if st.button("Check Answer"):
    if game.check_answer():
        st.success("Correct! You repaired all mutations!")
        st.session_state.game_over = True  # Mark game as complete
    else:
        st.error(f"Incorrect! Keep fixing mutations. Correct sequence: `{''.join(game.correct_strand)}`")

# Separate handling for "Play Again" button
if "game_over" in st.session_state and st.session_state.game_over:
    if st.button("Play Again!"):
        # Completely reset the game state
        st.session_state.dna_game = DNAGame()
        st.session_state.game_over = False
        st.rerun()
