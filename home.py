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

    .big-title-glow {
        font-size: 58px;
        font-weight: 700;
        text-align: center;
        color: #00ffe7;
        text-shadow:
            0 0 5px #00ffe7,
            0 0 15px #00ffe7,
            0 0 25px #00ffe7,
            0 0 40px #00d4ff,
            0 0 60px #00baff;
        position: relative;
        animation: scanlines 1s infinite linear, glitch 2.5s infinite alternate;
    }
        /* Hide default Streamlit sidebar toggle blocks */
    section[data-testid="stSidebar"] [data-testid^="stExpanderToggleIcon"] {
        display: none !important;
    }

    /* Optional: smooth out sidebar inputs */
    section[data-testid="stSidebar"] input[type="checkbox"],
    section[data-testid="stSidebar"] input[type="radio"] {
        accent-color: #88c0d0; /* matches your palette */
        transform: scale(1.1);
    }


    @keyframes glitch {
        0% { transform: translateX(0); }
        20% { transform: translateX(-1px); }
        40% { transform: translateX(1px); }
        60% { transform: translateX(-1px); }
        80% { transform: translateX(1px); }
        100% { transform: translateX(0); }
    }

    @keyframes scanlines {
        0% { opacity: 1; }
        50% { opacity: 0.95; }
        100% { opacity: 1; }
    }

    .title-glow {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: #88c0d0;
        text-shadow: 0 0 10px #88c0d0, 0 0 15px #6fa3bf, 0 0 20px #5790af;
        animation: flicker 1.5s infinite alternate;
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

    .cyber-text {
        color: #88c0d0;
        font-size: 22px;
        font-weight: 500;
    }

    .sci-fi-section {
        transition: transform 0.3s ease-in-out;
    }

    .sci-fi-section:hover {
        transform: scale(1.03);
    }

    .call-to-action {
        text-align: center;
        margin-top: 20px;
        padding: 10px;
    }

    a, a:visited {
        background: none !important;
        display: inline-flex;
        align-items: center;
    }

    a svg {
        background: none !important;
        filter: none !important;
    }

    a svg path {
        fill: #a8e6cf !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Neon-glow title with original layout
    st.markdown("""
    <div class="neon-box">
        <h1 class="big-title-glow">Code to Codons</h1>
        <hr style="border: 2px solid #ffcc66; box-shadow: 0px 0px 50px #ffcc66;">
        <p class="cyber-text">
            Explore the mysteries of DNA with tools and games!
        </p>
    </div>
    """, unsafe_allow_html=True)



if __name__ == "__main__":
    app()
