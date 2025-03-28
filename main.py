import streamlit as st
import home  # Import home page
import mutation_explorer  
import dnatoprotein_simulator 
import basewarp

PAGES = {
    "Home": home,  # Home page
    "BaseWarp Game": basewarp,
    "Mutation Explorer": mutation_explorer,
    "DNA to Protein Simulator": dnatoprotein_simulator,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=0)  # Default to Home

page = PAGES[selection]
page.app()
