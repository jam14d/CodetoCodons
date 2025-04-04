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
        font-size: 90px;
        font-weight: 800;
        text-align: center;
        color: #00ffe7;
        text-shadow:
            0 0 15px #00ffe7,
            0 0 35px #00ffe7,
            0 0 60px #00d4ff,
            0 0 80px #00baff,
            0 0 100px #00baff;
        position: relative;
        animation: scanlines 1s infinite linear, glitch 2.5s infinite alternate;
        line-height: 1.2;
    }

    /* Make title container bigger */
    .neon-box {
        background-color: rgba(38, 34, 35, 0.9);
        border: 2px solid #88c0d0;
        border-radius: 14px;
        padding: 50px 40px;
        box-shadow: 0px 0px 25px #88c0d0;
        margin: 40px auto;
        max-width: 1000px;
        text-align: center;
    }

    /* Fix gray vertical bar issue in sidebar (for expanders, etc.) */
    section[data-testid="stSidebar"] svg[data-testid="stIcon"] {
        display: none !important;
    }

    /* Streamlit checkbox and radio matching palette */
    section[data-testid="stSidebar"] input[type="checkbox"],
    section[data-testid="stSidebar"] input[type="radio"] {
        accent-color: #88c0d0;
        transform: scale(1.15);
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

    # Title box
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
