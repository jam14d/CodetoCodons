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
            background-color: #12101C;
            color: #E0C078;
            font-family: 'Space Mono', monospace;
        }
        .stApp {
            background-color: #12101C;
        }
        .radar-title {
            font-size: 38px;
            font-weight: bold;
            color: #E06C2D;
            text-align: center;
            text-shadow: 0px 0px 8px #E0C078;
            letter-spacing: 2px;
        }
        .stButton>button {
            background-color: #E06C2D;
            color: #12101C;
            border-radius: 5px;
            font-size: 14px;
            padding: 10px;
            border: none;
            cursor: pointer;
            text-transform: uppercase;
        }
        .stButton>button:hover {
            background-color: #E0C078;
            box-shadow: 0px 0px 10px #E06C2D;
        }
        .stSidebar {
            background-color: #1C1A2A;
            color: #E0C078;
            border-right: 3px solid #E06C2D;
        }
        .stMetric {
            color: #E0C078;
            font-size: 16px;
        }
        .stTable {
            background-color: #23202F;
            color: #E06C2D;
            border: 2px solid #E0C078;
        }
        .radar-box {
            background: rgba(224, 192, 120, 0.1);
            border-left: 4px solid #E0C078;
            padding: 14px;
            border-radius: 5px;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Title
    st.markdown("<h1 class='radar-title'>Mutation Explorer: SNP Tracker</h1>", unsafe_allow_html=True)

    # Introduction
    st.markdown("""
    <div class='radar-box'>
        A radar interface for genomic mutation tracking. Upload genome data, scan for variations, and map mutation patterns.
    </div>
    """, unsafe_allow_html=True)

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
        st.markdown("SNP Distribution")
        fig, ax = plt.subplots()
        ax.hist(snp_positions, bins=50, color='#E06C2D', alpha=0.9)
        ax.set_xlabel("Genome Position")
        ax.set_ylabel("Mutation Frequency")
        ax.set_title("SNP Spread")
        st.pyplot(fig)

    # Conclusion
    st.markdown("""
    <div class='radar-box'>
    Mutation patterns mapped successfully. High-frequency mutations indicate key areas of variation in the genome.
    </div>
    """, unsafe_allow_html=True)

# def app():
#     # Apply Retro-Futuristic Radar Aesthetic
#     st.markdown(
#         """
#         <style>
#         body {
#             background-color: #12101C;
#             color: #E0C078;
#             font-family: 'Space Mono', monospace;
#         }
#         .stApp {
#             background-color: #12101C;
#         }
#         .radar-title {
#             font-size: 38px;
#             font-weight: bold;
#             color: #E06C2D;
#             text-align: center;
#             text-shadow: 0px 0px 8px #E0C078;
#             letter-spacing: 2px;
#         }
#         .stButton>button {
#             background-color: #E06C2D;
#             color: #12101C;
#             border-radius: 5px;
#             font-size: 14px;
#             padding: 10px;
#             border: none;
#             cursor: pointer;
#             text-transform: uppercase;
#         }
#         .stButton>button:hover {
#             background-color: #E0C078;
#             box-shadow: 0px 0px 10px #E06C2D;
#         }
#         .stSidebar {
#             background-color: #1C1A2A;
#             color: #E0C078;
#             border-right: 3px solid #E06C2D;
#         }
#         .stMetric {
#             color: #E0C078;
#             font-size: 16px;
#         }
#         .stTable {
#             background-color: #23202F;
#             color: #E06C2D;
#             border: 2px solid #E0C078;
#         }
#         .radar-box {
#             background: rgba(224, 192, 120, 0.1);
#             border-left: 4px solid #E0C078;
#             padding: 14px;
#             border-radius: 5px;
#             font-size: 16px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
    
#     # Title
#     st.markdown("<h1 class='radar-title'>Mutation Explorer: SNP Tracker</h1>", unsafe_allow_html=True)

#     # Introduction
#     st.markdown("""
#     Welcome to your personal genomic gadget! The Mutation Explorer scans two DNA sequences, compares them, and pinpoints Single Nucleotide Polymorphisms (SNPs)—the tiny mutations that can make a big difference.

#     ### How to Operate:
#     **Step 1: Upload Your FASTA Files**
#     - **Reference Genome:** The baseline genome sequence.
#     - **Variant Genome:** The sequence with potential mutations.
    
#     Where to Get FASTA Files?
#     - [NCBI GenBank](https://www.ncbi.nlm.nih.gov/genbank/)
#     - [Ensembl](https://www.ensembl.org/)
#     - [UCSC Genome Browser](https://genome.ucsc.edu/)

#     **Step 2: Start SNP Detection**
#     - Compares the reference and variant genome.
#     - Identifies **mutation positions**.
#     - Displays **statistical and visual outputs**.

#     **Step 3: Analyze the Results**
#     - **Histogram of mutation positions**
#     - **Pie chart of SNP classifications**

#     This data can be used to study genome variations, transmissibility, and evolutionary trends!
#     """)

#     # Upload FASTA Files
#     st.sidebar.header("Upload Your FASTA Files")
#     ref_file = st.sidebar.file_uploader("Reference Genome (FASTA)", type=["fasta"])
#     var_file = st.sidebar.file_uploader("Variant Genome (FASTA)", type=["fasta"])

#     # Function to load FASTA sequences
#     def load_fasta(file):
#         return str(SeqIO.read(io.StringIO(file.getvalue().decode("utf-8")), "fasta").seq)

#     if ref_file and var_file:
#         reference_seq = load_fasta(ref_file)
#         variant_seq = load_fasta(var_file)
#         st.sidebar.success("Files Uploaded Successfully")
#     else:
#         st.sidebar.warning("Upload Reference and Variant FASTA Files.")
#         return

#     # Display genome lengths
#     st.subheader("Genome Data")
#     col1, col2 = st.columns(2)
#     col1.metric("Reference Genome Length", f"{len(reference_seq)} bp")
#     col2.metric("Variant Genome Length", f"{len(variant_seq)} bp")

#     # Function to find SNPs
#     def find_snps(ref_seq, var_seq):
#         return [(i, ref_nuc, var_nuc) for i, (ref_nuc, var_nuc) in enumerate(zip(ref_seq, var_seq)) if ref_nuc != var_nuc]

#     snps = find_snps(reference_seq, variant_seq)

#     # Show SNP summary
#     st.subheader("SNP Detection")
#     st.write(f"Total SNPs Found: {len(snps)}")

#     # Extract SNP positions
#     snp_positions = [pos for pos, _, _ in snps]

#     # Visualizations
#     st.subheader("Data Analysis")
#     col1, col2 = st.columns(2)

#     # SNP Distribution Histogram
#     with col1:
#         st.markdown("SNP Distribution")
#         fig, ax = plt.subplots()
#         ax.hist(snp_positions, bins=50, color='#E06C2D', alpha=0.9)
#         ax.set_xlabel("Genome Position")
#         ax.set_ylabel("Mutation Frequency")
#         ax.set_title("SNP Spread")
#         st.pyplot(fig)

#     # Conclusion
#     st.markdown("""
#     <div class='radar-box'>
#     Mutation patterns mapped successfully. High-frequency mutations indicate key areas of variation in the genome.
#     </div>
#     """, unsafe_allow_html=True)