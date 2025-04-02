import streamlit as st
import random

class DNAGame:
    base_pairing = {"A": "T", "T": "A", "C": "G", "G": "C"}
    nucleotides = ["A", "T", "C", "G"]

    def __init__(self, length=6):
        self.length = length
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
        self.mutated_strand[idx1], self.mutated_strand[idx2] = self.mutated_strand[idx2], self.mutated_strand[idx1]

    def check_answer(self):
        return self.mutated_strand == self.correct_strand

def app():
    # Initialize game
    if "dna_game" not in st.session_state:
        st.session_state.dna_game = DNAGame()
    game = st.session_state.dna_game

    # Styling
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600&display=swap" rel="stylesheet">
    <style>
        html, body, [class*="css"] {
            font-family: 'Orbitron', sans-serif !important;
        }

        .crt-box {
            background-color: #121212;
            padding: 20px;
            border-radius: 15px;
            color: #ffffff;
            text-align: center;
            max-width: 900px;
            margin: auto;
            box-shadow: 0px 0px 30px rgba(100, 149, 237, 0.6);
        }

        .animated-title {
            font-size: 90px;
            color: #6495ed;
            position: relative;
            display: inline-block;
            overflow: hidden;
        }

        .animated-title::after {
            content: '';
            position: absolute;
            top: 0;
            left: -75%;
            width: 50%;
            height: 100%;
            background: linear-gradient(120deg, transparent, rgba(255,255,255,0.4), transparent);
            animation: shimmer 2.5s infinite;
        }

        @keyframes shimmer {
            0% { left: -75%; }
            100% { left: 125%; }
        }

        h3.section-title {
            text-align: center;
            font-size: 24px;
            color: #ffcc33;
            text-shadow: 0 0 10px #ffcc33;
            margin-top: 20px;
        }

        h3.section-title.blue {
            color: #33ccff;
            text-shadow: 0 0 10px #33ccff;
        }

        .dna-box {
            font-size: 24px;
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            border: 3px solid #ffcc33;
            background-color: #1e1e1e;
            color: #ffcc33;
            box-shadow: 0px 0px 15px rgba(230, 184, 0, 0.6);
        }

        div.stButton > button {
            font-size: 30px !important;
            width: 100px !important;
            height: 100px !important;
            border-radius: 10px !important;
            border: 3px solid #33ccff !important;
            background-color: #1e1e1e !important;
            color: #33ccff !important;
            box-shadow: 0px 0px 15px rgba(0, 204, 255, 0.6) !important;
            transition: all 0.2s !important;
        }

        div.stButton > button:hover {
            transform: scale(1.1) !important;
            box-shadow: 0px 0px 20px rgba(0, 255, 255, 0.9) !important;
            border-color: #00ffff !important;
            color: #00ffff !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Title box
    st.markdown("""
    <div class="crt-box">
        <h1 class="animated-title">BASEWARP</h1>
        <hr style="border: 2px solid #6495ed; box-shadow: 0px 0px 10px #6495ed;">
        <p style="color: #a9c9ff; font-size: 18px;">
            Your DNA strand has been warped by mutations!<br>
            Select two nucleotides on your complementary strand to swap them until your double helix is restored.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Template DNA
    st.markdown('<h3 class="section-title">Template DNA:</h3>', unsafe_allow_html=True)
    st.markdown('<div style="display:flex;justify-content:center;gap:10px;">' +
                ''.join(f'<div class="dna-box">{b}</div>' for b in game.template_strand) +
                '</div>', unsafe_allow_html=True)

    # Complementary strand
    st.markdown('<h3 class="section-title blue">Complementary Strand:</h3>', unsafe_allow_html=True)
    st.markdown('<div class="complementary-strand">', unsafe_allow_html=True)

    cols = st.columns(game.length)
    for i, col in enumerate(cols):
        with col:
            if st.button(game.mutated_strand[i], key=f"complementary-btn-{i}"):
                if game.selected is None:
                    game.selected = i
                else:
                    game.swap_bases(game.selected, i)
                    game.selected = None
                    st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # Sidebar controls
    with st.sidebar:
        st.header("Game Controls")

        if st.button("Check Answer"):
            if game.check_answer():
                st.success("Correct! You repaired all mutations!")
                st.session_state.game_over = True
            else:
                st.error(f"Incorrect! Keep fixing mutations. Correct sequence: `{''.join(game.correct_strand)}`")

        if "game_over" in st.session_state and st.session_state.game_over:
            if st.button("Play Again!"):
                st.session_state.dna_game = DNAGame()
                st.session_state.game_over = False
                st.rerun()
