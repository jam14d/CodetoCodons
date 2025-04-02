import streamlit as st
import home  # Import home page
import mutation_explorer  
import biosynthesis_simulator 
import basewarp
import stability_matrix

PAGES = {
    "Home": home,  # Home page
    "BaseWarp Game": basewarp,
    "Bio-Synthesis Simulator": biosynthesis_simulator,
    "Mutation Explorer": mutation_explorer,
    "Stability Matrix": stability_matrix,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=0)  # Default to Home

page = PAGES[selection]
page.app()
