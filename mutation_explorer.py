import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO
import io

def load_fasta(file):
    return str(SeqIO.read(io.StringIO(file.getvalue().decode("utf-8")), "fasta").seq)

def find_snps(ref_seq, var_seq):
    return [(i, ref_nuc, var_nuc) for i, (ref_nuc, var_nuc) in enumerate(zip(ref_seq, var_seq)) if ref_nuc != var_nuc]

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
            0% { text-shadow: 0px 0px 5px #FF3C00, 0px 0px 10px #00FFC6; }
            50% { text-shadow: 0px 0px 10px #FF3C00, 0px 0px 20px #00FFC6; }
            100% { text-shadow: 0px 0px 5px #FF3C00, 0px 0px 10px #00FFC6; }
        }
        .glitch-title {
            font-size: 42px;
            font-weight: bold;
            color: #FF3C00;
            text-align: center;
            animation: cyber-glitch 1.5s infinite alternate;
            letter-spacing: 3px;
        }
        .glow-box {
            background: rgba(0, 255, 204, 0.1);
            border-left: 4px solid #00FFCC;
            padding: 14px;
            border-radius: 5px;
            font-size: 16px;
            box-shadow: 0px 0px 15px #00FFCC;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h1 class='glitch-title'>Mutation Explorer</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='glow-box'>
    Welcome to Mutation Explorer! Upload your FASTA files to compare DNA sequences and detect Single Nucleotide Polymorphisms (SNPs).
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.header("Upload Your FASTA Files")
    ref_file = st.sidebar.file_uploader("Reference Genome (FASTA)", type=["fasta"])
    var_file = st.sidebar.file_uploader("Variant Genome (FASTA)", type=["fasta"])

    if ref_file and var_file:
        reference_seq = load_fasta(ref_file)
        variant_seq = load_fasta(var_file)
        st.sidebar.success("Files Uploaded Successfully")
    else:
        st.sidebar.warning("Upload Reference and Variant FASTA Files.")
        return

    st.subheader("Genome Data")
    col1, col2 = st.columns(2)
    col1.metric("Reference Genome Length", f"{len(reference_seq)} bp")
    col2.metric("Variant Genome Length", f"{len(variant_seq)} bp")

    snps = find_snps(reference_seq, variant_seq)
    st.subheader("SNP Detection")
    st.write(f"Total SNPs Found: {len(snps)}")
    
    snp_positions = [pos for pos, _, _ in snps]

    st.subheader("Data Analysis")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### SNP Distribution")
        fig, ax = plt.subplots()
        ax.hist(snp_positions, bins=50, color='#E06C2D', alpha=0.9)
        ax.set_xlabel("Genome Position")
        ax.set_ylabel("Mutation Frequency")
        ax.set_title("SNP Spread")
        st.pyplot(fig)

    with col2:
        st.markdown("#### SNP Type Proportion")
        fig2, ax2 = plt.subplots()
        ax2.pie([60, 40], labels=["Transitions", "Transversions"], autopct='%1.1f%%', colors=['#00FFCC', '#006666'])
        ax2.set_title("SNP Types")
        st.pyplot(fig2)

    st.markdown("""
    <div class='glow-box'>
    Analysis complete.
    </div>
    """, unsafe_allow_html=True)
