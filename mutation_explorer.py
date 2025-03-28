import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO
import io

def app():
    # Title
    st.title("Mutation Explorer: Tracking SNPs in Viral Genomes")

    # Introduction
    st.markdown("""
    ### Understanding SNPs (Single Nucleotide Polymorphisms)
    SNPs are small genetic variations that occur when a single nucleotide in a DNA sequence differs from the reference sequence.
    """)

    # Upload FASTA Files
    st.sidebar.header("Upload Your Own FASTA Files (Optional)")
    ref_file = st.sidebar.file_uploader("Upload Reference Genome (FASTA)", type=["fasta"])
    var_file = st.sidebar.file_uploader("Upload Variant Genome (FASTA)", type=["fasta"])

    # Function to load FASTA sequences
    def load_fasta(file):
        return str(SeqIO.read(io.StringIO(file.getvalue().decode("utf-8")), "fasta").seq)

    # Load sequences
    if ref_file and var_file:
        reference_seq = load_fasta(ref_file)
        variant_seq = load_fasta(var_file)
        st.sidebar.success("Using uploaded FASTA files!")
    else:
        st.sidebar.warning("Please upload both reference and variant genome FASTA files.")
        return  # Exit the function if no files are uploaded

    # Display genome lengths
    st.subheader("Genome Information")
    col1, col2 = st.columns(2)
    col1.metric("Reference Genome Length", f"{len(reference_seq)} bp")
    col2.metric("Variant Genome Length", f"{len(variant_seq)} bp")

    # Function to find SNPs
    def find_snps(ref_seq, var_seq):
        return [(i, ref_nuc, var_nuc) for i, (ref_nuc, var_nuc) in enumerate(zip(ref_seq, var_seq)) if ref_nuc != var_nuc]

    snps = find_snps(reference_seq, variant_seq)

    # Show SNP summary
    st.subheader("SNP Detection Results")
    st.write(f"**Total SNPs Found:** {len(snps)}")

    # Display first 10 SNPs
    if snps:
        st.write("**First 10 SNPs Detected:**")
        snp_table = {"Position": [], "Reference Nucleotide": [], "Variant Nucleotide": []}
        for pos, ref_nuc, var_nuc in snps[:10]:
            snp_table["Position"].append(pos)
            snp_table["Reference Nucleotide"].append(ref_nuc)
            snp_table["Variant Nucleotide"].append(var_nuc)
        st.table(snp_table)

    # Extract SNP positions
    snp_positions = [pos for pos, _, _ in snps]

    # Function to classify SNP types
    def classify_snp_types(snps):
        transitions = {"A": "G", "G": "A", "C": "T", "T": "C"}
        transversions = {"A": ["C", "T"], "G": ["C", "T"], "C": ["A", "G"], "T": ["A", "G"]}
        counts = {"Transitions": 0, "Transversions": 0}
        for _, ref_nuc, var_nuc in snps:
            if transitions.get(ref_nuc) == var_nuc:
                counts["Transitions"] += 1
            elif var_nuc in transversions.get(ref_nuc, []):
                counts["Transversions"] += 1
        return counts

    # Classify SNPs
    snp_classification = classify_snp_types(snps)

    # Data Visualization
    st.subheader("Data Analysis")
    col1, col2 = st.columns(2)

    # SNP Distribution Histogram (Left)
    with col1:
        st.markdown("#### SNP Distribution Across the Genome")
        fig, ax = plt.subplots(figsize=(4, 2))
        ax.hist(snp_positions, bins=75, color='purple', alpha=0.7)
        ax.set_xlabel("Genome Position", fontsize=8)
        ax.set_ylabel("SNP Frequency", fontsize=8)
        ax.set_title("SNP Distribution", fontsize=10)
        ax.tick_params(axis='both', labelsize=6)
        st.pyplot(fig)

    # SNP Classification Pie Chart (Right)
    with col2:
        st.markdown("#### SNP Type Proportion")
        fig2, ax2 = plt.subplots(figsize=(3, 3))
        ax2.pie(
            snp_classification.values(),
            labels=snp_classification.keys(),
            autopct='%1.1f%%',
            colors=['blue', 'orange'],
            textprops={'fontsize': 6}
        )
        ax2.set_title("SNP Types", fontsize=8)
        st.pyplot(fig2)

    # Conclusion
    st.markdown("""
    ### Key Takeaways:
    - **SNPs (mutations) are common in viral genomes** and can affect **viral transmissibility and vaccine resistance**.
    - **Transitions (A↔G, C↔T) are more frequent** because they preserve chemical structure.
    - **Transversions (A↔C, A↔T, G↔C, G↔T) are less common** but may have stronger functional effects.
    """)

