import streamlit as st
from Bio.Seq import Seq
import random
import time

# Futuristic Research Lab Styling
st.set_page_config(page_title="STABILITY MATRIX", layout="wide")

def set_theme():
    st.markdown(
        """
        <style>
            body {
                background-color: #0a1a0a;
                color: #33FF99;
                font-family: 'Courier New', monospace;
            }
            .stApp {
                background: radial-gradient(circle, #042204, #000000);
                color: #33FF99;
            }
            .css-1d391kg {
                color: #33FF99 !important;
            }
            .stButton > button {
                background-color: #FF5733;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                border: 2px solid #C70039;
                transition: all 0.3s ease-in-out;
            }
            .stButton > button:hover {
                background-color: #900C3F;
                color: white;
                transform: scale(1.05);
            }
            .data-box {
                border: 2px solid #33FF99;
                padding: 10px;
                border-radius: 10px;
                text-align: center;
                font-size: 18px;
            }
            .scan-animation {
                font-size: 20px;
                color: #FF5733;
                animation: flicker 1.5s infinite alternate;
            }
            @keyframes flicker {
                from { opacity: 1; }
                to { opacity: 0.4; }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_theme()

# Generate a random DNA sequence of length 50
def generate_random_dna(length=50):
    return "".join(random.choices("ATCG", k=length))

class DNAAnalyzer:
    def __init__(self, sequence):
        self.sequence = Seq(sequence.upper())
    
    def count_cytosine(self):
        return self.sequence.count('C')
    
    def sequence_length(self):
        return len(self.sequence)
    
    def compute_gc_percentage(self):
        g_count = self.sequence.count('G')
        c_count = self.count_cytosine()
        total_length = self.sequence_length()
        if total_length == 0:
            return 0
        return ((g_count + c_count) / total_length) * 100


def app():
    st.title("STABILITY MATRIX - Secure Genetic Analysis Terminal")
    
    st.write("""
    **Welcome to STABILITY MATRIX.** Please submit a sequence for analysis.
    System security protocols are engaged. Unauthorized access will be monitored.
    """)
    
    sequence_input = st.text_input("Enter a DNA sequence (or let the system generate one):")
    if not sequence_input:
        sequence_input = generate_random_dna()
        st.info(f"🔍 Scanning Biological Sample... Sequence Extracted: {sequence_input}")
    
    dna_analyzer = DNAAnalyzer(sequence_input)
    
    if st.button("Begin Genetic Analysis"):
        with st.spinner("🔎 Analyzing Sample... Please Wait..."):
            time.sleep(2)  # Simulate processing time
            gc_content = dna_analyzer.compute_gc_percentage()
        st.success(f"Analysis Complete: GC Content: {gc_content:.2f}%")
        st.markdown('<div class="data-box">Stability Threshold: {}</div>'.format(
            'Stable' if gc_content > 40 else '⚠️ Unstable'), unsafe_allow_html=True)
    
    st.markdown("### Research Data Insights:")
    st.markdown("- **GC Content** affects DNA stability and genetic function.")
    st.markdown("- **Cytosine & Guanine** pairs strengthen the structure.")
    st.markdown("- **Genetic anomalies** can be detected through content analysis.")
    
    if st.button("Unlock Full Genetic Report"):
        solution_code = '''from Bio.Seq import Seq\n\nclass DNAAnalyzer:\n    def __init__(self, sequence):\n        self.sequence = Seq(sequence.upper())\n    \n    def count_cytosine(self):\n        return self.sequence.count('C')\n    \n    def sequence_length(self):\n        return len(self.sequence)\n    \n    def compute_gc_percentage(self):\n        g_count = self.sequence.count('G')\n        c_count = self.count_cytosine()\n        total_length = self.sequence_length()\n        if total_length == 0:\n            return 0\n        return ((g_count + c_count) / total_length) * 100\n'''  
        with open("solution.txt", "w") as f:
            f.write(solution_code)
        st.download_button("Download Genetic Report", "solution.txt")

if __name__ == "__main__":
    app()
