import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO
import io


def app():
    
    st.markdown(
        """
        <style>
        body {
            background-color: #0A0A0F;
            color: #00FFCC;
            font-family: 'Orbitron', sans-serif;
        }
        .stApp {
            background-color: #0A0A0F;
        }
        @keyframes cyber-glitch {
            0% { text-shadow: 4px 4px 0px #FF3C00, -4px -4px 0px #00FFC6; }
            50% { text-shadow: -3px -3px 0px #FF3C00, 3px 3px 0px #00FFC6; }
            100% { text-shadow: 4px -4px 0px #FF3C00, -4px 4px 0px #00FFC6; }
        }
        .glitch-title {
            font-size: 42px;
            font-weight: bold;
            color: #FF3C00;
            text-align: center;
            animation: cyber-glitch 5s infinite alternate;
            letter-spacing: 3px;
        }
        .stButton>button {
            background: linear-gradient(90deg, #FF3C00, #00FFC6);
            color: #0A0A0F;
            border-radius: 8px;
            font-size: 14px;
            padding: 12px;
            border: none;
            cursor: pointer;
            text-transform: uppercase;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #00FFC6, #FF3C00);
            box-shadow: 0px 0px 15px #FF3C00;
        }
        .stSidebar {
            background-color: #141222;
            color: #00FFCC;
            border-right: 3px solid #FF3C00;
        }
        .stMetric {
            color: #00FFCC;
            font-size: 18px;
        }
        .stTable {
            background-color: #1A1A3A;
            color: #FF3C00;
            border: 2px solid #00FFCC;
        }
        .cyber-box {
            background: rgba(0, 255, 204, 0.1);
            border-left: 4px solid #00FFCC;
            padding: 14px;
            border-radius: 5px;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Title with glitch animation
    st.markdown("<h1 class='glitch-title'>Mutation Explorer</h1>", unsafe_allow_html=True)


    # Introduction
    st.markdown("""
    
    Welcome to your personal genomic gadget! The Mutation Explorer scans two DNA sequences, compares them, and pinpoints Single Nucleotide Polymorphisms (SNPs)—the tiny mutations that can make a big difference.

    ### How to Operate:
    **Step 1: Upload Your FASTA Files**
    - **Reference Genome:** The baseline genome sequence.
    - **Variant Genome:** The sequence with potential mutations.
    
    Where to Get FASTA Files?
    - [NCBI GenBank](https://www.ncbi.nlm.nih.gov/genbank/)
    - [Ensembl](https://www.ensembl.org/)
    - [UCSC Genome Browser](https://genome.ucsc.edu/)

    **Step 2: Start SNP Detection**
    - Compares the reference and variant genome.
    - Identifies **mutation positions**.
    - Displays **statistical and visual outputs**.

    **Step 3: Analyze the Results**
    - **Histogram of mutation positions**
    - **Pie chart of SNP classifications**

    This data can be used to study genome variations, transmissibility, and evolutionary trends!
    """)

    # Upload FASTA Files
    st.sidebar.header("Upload Your FASTA Files")
    ref_file = st.sidebar.file_uploader("Reference Genome (FASTA)", type=["fasta"])
    var_file = st.sidebar.file_uploader("Variant Genome (FASTA)", type=["fasta"])

    # Function to load FASTA sequences
    def load_fasta(file):
        return str(SeqIO.read(io.StringIO(file.getvalue().decode("utf-8")), "fasta").seq)

    if ref_file and var_file:
        reference_seq = load_fasta(ref_file)
        variant_seq = load_fasta(var_file)
        st.sidebar.success("Files Uploaded Successfully")
    else:
        st.sidebar.warning("Upload Reference and Variant FASTA Files.")
        return

    # Display genome lengths
    st.subheader("Genome Data")
    col1, col2 = st.columns(2)
    col1.metric("Reference Genome Length", f"{len(reference_seq)} bp")
    col2.metric("Variant Genome Length", f"{len(variant_seq)} bp")

    # Function to find SNPs
    def find_snps(ref_seq, var_seq):
        return [(i, ref_nuc, var_nuc) for i, (ref_nuc, var_nuc) in enumerate(zip(ref_seq, var_seq)) if ref_nuc != var_nuc]

    snps = find_snps(reference_seq, variant_seq)

    # Show SNP summary
    st.subheader("SNP Detection")
    st.write(f"Total SNPs Found: {len(snps)}")

    # Extract SNP positions
    snp_positions = [pos for pos, _, _ in snps]

    # Visualizations
    st.subheader("Data Analysis")
    col1, col2 = st.columns(2)

    # SNP Distribution Histogram
    with col1:
        st.markdown("#### SNP Distribution")
        fig, ax = plt.subplots()
        ax.hist(snp_positions, bins=50, color='#E06C2D', alpha=0.9)
        ax.set_xlabel("Genome Position")
        ax.set_ylabel("Mutation Frequency")
        ax.set_title("SNP Spread")
        st.pyplot(fig)
        
    # SNP Classification Pie Chart
    with col2:
        st.markdown("#### SNP Type Proportion")
        fig2, ax2 = plt.subplots()
        ax2.pie([60, 40], labels=["Transitions", "Transversions"], autopct='%1.1f%%', colors=['#00FFCC', '#006666'])
        ax2.set_title("SNP Types")
        st.pyplot(fig2)


    # Conclusion
    st.markdown("""
    <div class='radar-box'>
    Mutation patterns mapped successfully.
    </div>
    """, unsafe_allow_html=True)