import streamlit as st

def app():
    # Inject Custom CSS
    st.markdown("""
    <style>
    html, body, [class*="st"] {
        background-color: #282425;
        color: #a8e6cf;
        font-family: 'Orbitron', sans-serif;
    }

    * > [data-testid=stHeaderActionElements] {
        display: none;
    }
    .big-title-glow {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #ffcc66;
        text-shadow: 0 0 50px #ff9966, 0 0 50px #ffcc66, 0 0 50px #ff6633;
        animation: flicker-big 1.5s infinite alternate;
    }
    .title-glow {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: #88c0d0;
        text-shadow: 0 0 10px #88c0d0, 0 0 15px #6fa3bf, 0 0 20px #5790af;
        animation: flicker 1.5s infinite alternate;
    }
    @keyframes flicker-big {
        0% { opacity: 1; text-shadow: 0 0 25px #ff9966; }
        50% { opacity: 0.9; text-shadow: 0 0 40px #ffcc66; }
        100% { opacity: 1; text-shadow: 0 0 25px #ff9966; }
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
    /* Fix for black boxes under link icons */
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

    # Glowing Title
    st.markdown("""
    <div class="neon-box">
        <h1 class="big-title-glow">Code to Codons</h1>
        <hr style="border: 2px solid #ffcc66; box-shadow: 0px 0px 50px #ffcc66;">
        <p class="cyber-text">
            Explore the mysteries of DNA with tools and games!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Sci-Fi Sections with subtle animation
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="neon-box sci-fi-section">
            <h4 class="title-glow">Mutation Explorer</h4>
            <p class="cyber-text">Analyze genetic variations and detect mutations in viral genomes.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="neon-box sci-fi-section">
            <h4 class="title-glow">DNA to Protein Simulator</h4>
            <p class="cyber-text">Convert DNA sequences into proteins through transcription and translation.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="neon-box sci-fi-section">
        <h4 class="title-glow">BaseWarp Game</h4>
        <p class="cyber-text">Fix mutations in a DNA strand by swapping base pairs in this neon-lit arcade challenge!</p>
    </div>
    """, unsafe_allow_html=True)
