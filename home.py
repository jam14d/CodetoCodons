import streamlit as st

def app():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&display=swap');

    html, body, [class*="st"] {
        background-color: #282425;
        color: #a8e6cf;
        font-family: 'Orbitron', sans-serif;
        overflow-x: hidden;
    }

    * > [data-testid=stHeaderActionElements] {
        display: none;
    }

    body::before {
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        background-image: repeating-linear-gradient(
            to bottom,
            rgba(255, 255, 255, 0.02),
            rgba(255, 255, 255, 0.02) 1px,
            transparent 1px,
            transparent 4px
        );
        pointer-events: none;
        z-index: 9999;
    }

    .big-title-glow {
        font-size: 56px;
        font-weight: bold;
        text-align: center;
        color: #ffcc66;
        text-shadow: 0 0 8px #ff9966, 0 0 22px #ffcc66, 0 0 42px #ff6633;
        animation: flicker-big 2s infinite alternate;
    }

    .title-glow {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        color: #88c0d0;
        text-shadow: 0 0 10px #88c0d0, 0 0 15px #6fa3bf, 0 0 20px #5790af;
        animation: flicker 1.8s infinite alternate;
    }

    @keyframes flicker-big {
        0%, 100% { opacity: 1; text-shadow: 0 0 25px #ff9966; }
        50% { opacity: 0.7; text-shadow: 0 0 50px #ffcc66; }
    }

    @keyframes flicker {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.85; }
    }

    .neon-box {
        background: linear-gradient(145deg, rgba(40,36,37,0.95), rgba(50,45,46,0.95));
        border: 2px dashed #88c0d0;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 0 25px #88c0d0;
        max-width: 960px;
        margin: auto;
        text-align: center;
        transition: all 0.3s ease-in-out;
    }

    .neon-box:hover {
        box-shadow: 0 0 45px #a8e6cf;
        transform: scale(1.02);
    }

    .cyber-text {
        font-size: 22px;
        font-weight: 500;
        background: linear-gradient(to right, #a8e6cf, #88c0d0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .sci-fi-section {
        margin-top: 20px;
    }

    hr {
        border: 0;
        height: 3px;
        background: linear-gradient(to right, #ffcc66, #ff9966, #ffcc66);
        box-shadow: 0 0 15px #ffcc66;
    }

    a, a:visited {
        background: none !important;
        display: inline-flex;
        align-items: center;
    }

    a svg path {
        fill: #a8e6cf !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="neon-box">
        <h1 class="big-title-glow">Code to Codons</h1>
        <hr />
        <p class="cyber-text">
            Explore the mysteries of DNA with tools and games!
        </p>
    </div>
    """, unsafe_allow_html=True)
