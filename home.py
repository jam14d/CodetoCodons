import streamlit as st

def app():
    # Inject Custom CSS
    st.markdown("""
    <style>
    html, body, [class*="st"] {
        background-color: #0d0d0d;
        color: #00ffee;
        font-family: 'Orbitron', sans-serif;
    }
    .title-glow {
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        color: #ff8800;
        text-shadow: 0 0 10px #ff8800, 0 0 20px #ff5500, 0 0 30px #ff2200;
        animation: flicker 1.5s infinite alternate;
    }
    @keyframes flicker {
        0% { opacity: 1; text-shadow: 0 0 10px #ff8800; }
        50% { opacity: 0.8; text-shadow: 0 0 20px #ff5500; }
        100% { opacity: 1; text-shadow: 0 0 10px #ff8800; }
    }
    .neon-box {
        background-color: rgba(20, 20, 20, 0.9);
        border: 2px solid #00ffee;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 0px 15px #00ffee;
        margin: auto;
        max-width: 900px;
        text-align: center;
    }
    .cyber-text {
        color: #00ffee;
        font-size: 22px;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

    # Glowing Title
    st.markdown("""
    <div class="neon-box">
        <h1 class="title-glow">Code to Codons</h1>
        <hr style="border: 2px solid #ff8800; box-shadow: 0px 0px 10px #ff8800;">
        <p class="cyber-text">
            Explore the mysteries of DNA with tools and games!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Sci-Fi Sections
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="neon-box">
            <h2 class="title-glow" style="font-size: 24px;">Mutation Explorer</h2>
            <p class="cyber-text">Analyze genetic variations and detect mutations in viral genomes.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="neon-box">
            <h2 class="title-glow" style="font-size: 24px;">DNA to Protein Simulator</h2>
            <p class="cyber-text">Convert DNA sequences into proteins through transcription and translation.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="neon-box">
        <h2 class="title-glow" style="font-size: 24px;">BaseWarp Game</h2>
        <p class="cyber-text">Fix mutations in a DNA strand by swapping base pairs in this neon-lit arcade challenge!</p>
    </div>
    """, unsafe_allow_html=True)

    # Call to Action
    st.markdown("""
    <div style="text-align:center; margin-top:30px;">
        <h3 class="title-glow" style="font-size: 24px;">Start Exploring Now!</h3>
    </div>
    """, unsafe_allow_html=True)