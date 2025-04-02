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
        color: #ffffff;
        position: relative;
        display: inline-block;
        overflow: hidden;
        letter-spacing: 10px;
        text-shadow:
            0 0 5px #33ccff,
            0 0 15px #33ccff,
            -2px 0 #ff00ff,
            2px 0 #00ffff;
        animation: warp 2s infinite ease-in-out;

        }

        .animated-title::before,
        .animated-title::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            overflow: hidden;
            color: #ffffff;
            z-index: -1;
        }

        .animated-title::before {
            color: #ff00ff;
            left: 2px;
            animation: glitch-left 1.8s infinite;
        }

        .animated-title::after {
            color: #00ffff;
            left: -2px;
            animation: glitch-right 1.8s infinite;
        }

        @keyframes warp {
            0%, 100% {
                transform: skewX(0deg);
            }
            50% {
                transform: skewX(2deg) scale(1.02);
            }
        }

        @keyframes glitch-left {
            0% { clip-path: inset(0 0 80% 0); }
            50% { clip-path: inset(30% 0 30% 0); }
            100% { clip-path: inset(80% 0 0 0); }
        }

        @keyframes glitch-right {
            0% { clip-path: inset(80% 0 0 0); }
            50% { clip-path: inset(20% 0 50% 0); }
            100% { clip-path: inset(0 0 80% 0); }
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

    st.markdown("""
    <div style="text-align: center;">
        <h1 class="animated-title" data-text="BASEWARP">BASEWARP</h1>
    </div>
    """, unsafe_allow_html=True)


    # intro box
    st.markdown("""
    <div style="
        background-color: rgba(18, 18, 18, 0.85);
        padding: 25px;
        border-radius: 15px;
        color: #ccf5ff;
        font-size: 18px;
        line-height: 1.6;
        letter-spacing: 0.5px;
        text-align: center;
        max-width: 800px;
        margin: 30px auto;
        border: 5px solid rgba(0, 100, 255, 0.2);
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3), 0 0 30px rgba(0, 150, 255, 0.25);
        backdrop-filter: blur(4px);
    ">
        <p>
            Your DNA strand has been warped by mutations.<br>
            Select two nucleotides on your complementary strand to swap them until your double helix is restored.
        </p>
    </div>
    """, unsafe_allow_html=True)

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
