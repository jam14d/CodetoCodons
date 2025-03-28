import streamlit as st

def app():
    # Retro Sci-Fi Styling
    st.markdown("""
    <style>
    @keyframes glow {
        0% { text-shadow: 0 0 5px #6495ed, 0 0 10px #6495ed, 0 0 15px #6495ed; }
        50% { text-shadow: 0 0 10px #ff66cc, 0 0 20px #ff66cc, 0 0 30px #ff66cc; }
        100% { text-shadow: 0 0 5px #6495ed, 0 0 10px #6495ed, 0 0 15px #6495ed; }
    }
    .title-glow {
        font-size: 60px;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        animation: glow 2s infinite alternate;
    }
    .neon-box {
        background-color: rgba(18, 18, 18, 0.95);
        padding: 20px;
        border-radius: 10px;
        color: #ffffff;
        text-align: center;
        box-shadow: 0px 0px 30px rgba(100, 149, 237, 0.6);
        max-width: 900px;
        margin: auto;
    }
    .cyber-text {
        color: #a9c9ff;
        font-size: 22px;
        font-weight: 500;
        text-shadow: 0px 0px 10px rgba(255, 105, 180, 0.8);
    }
    .glitch {
        position: relative;
        display: inline-block;
        color: #ffcc33;
        font-size: 18px;
        text-transform: uppercase;
        text-shadow: 0 0 5px #ffcc33, 0 0 10px #ffcc33, 0 0 15px #ffcc33;
    }
    .glitch:before, .glitch:after {
        content: attr(data-text);
        position: absolute;
        left: 0;
        opacity: 0.8;
    }
    .glitch:before {
        animation: glitch 1.5s infinite alternate-reverse;
        color: #00ffff;
        left: 2px;
    }
    .glitch:after {
        animation: glitch 1.5s infinite alternate;
        color: #ff66cc;
        left: -2px;
    }
    @keyframes glitch {
        0% { transform: translateX(0); }
        50% { transform: translateX(5px); }
        100% { transform: translateX(-5px); }
    }
    </style>
    """, unsafe_allow_html=True)

    # Glowing Title
    st.markdown("""
    <div class="neon-box">
        <h1 class="title-glow">Code to Codons </h1>
        <hr style="border: 2px solid #ff66cc; box-shadow: 0px 0px 10px #ff66cc;">
        <p class="cyber-text">
            Explore the mysteries of DNA with tools and games! 
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Create cyberpunk-themed sections
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color:#222; padding:15px; border-radius:10px; 
                    box-shadow:0px 0px 20px rgba(255, 105, 180, 0.7);">
            <h2 style="color:#ff66cc;">Mutation Explorer</h2>
            <p class="cyber-text">Analyze genetic variations and detect mutations in viral genomes.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color:#222; padding:15px; border-radius:10px; 
                    box-shadow:0px 0px 20px rgba(100, 149, 237, 0.7);">
            <h2 style="color:#6495ed;">DNA to Protein Simulator</h2>
            <p class="cyber-text">Convert DNA sequences into proteins through transcription and translation.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color:#222; padding:15px; border-radius:10px; 
                box-shadow:0px 0px 20px rgba(255, 204, 51, 0.7); text-align:center; margin-top:20px;">
        <h2 style="color:#ffcc33;">BaseWarp Game</h2>
        <p class="cyber-text">Fix mutations in a DNA strand by swapping base pairs in this neon-lit arcade challenge!</p>
    </div>
    """, unsafe_allow_html=True)

    # Move navigation lower
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Call to Action
    st.markdown("""
    <div style="text-align:center; margin-top:30px;">
        <h3 class="glitch" data-text="Start Exploring Now!">Start Exploring Now!</h3>
    </div>
    """, unsafe_allow_html=True)
