import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO
import io

# Streamlit Page Configuration
st.set_page_config(page_title="SNP Detection in Viral Genomes", layout="wide")

# Title
st.title("Mutation Explorer: Tracking SNPs in Viral Genomes")

# Introduction
st.markdown("""
### Understanding SNPs (Single Nucleotide Polymorphisms)
\n\nSNPs are small genetic variations that occur when a single nucleotide in a DNA sequence differs from the reference sequence.
\n\nDetecting SNPs helps scientists study viral mutations, disease evolution, and vaccine effectiveness.

In this app, we analyze genetic variations in SARS-CoV-2 (COVID-19) using reference and variant genome sequences.
""")

# Pre-loaded file paths (your uploaded files)
default_ref_file_path = "/Users/jamieannemortel/Desktop/CodetoCodons/data/reference-NC_045512.fasta"
default_var_file_path = "/Users/jamieannemortel/Desktop/CodetoCodons/data/BA.3.1.fasta"

# Upload FASTA Files
st.sidebar.header(" Upload Your Own FASTA Files (Optional)")
ref_file = st.sidebar.file_uploader("Upload Reference Genome (FASTA)", type=["fasta"])
var_file = st.sidebar.file_uploader("Upload Variant Genome (FASTA)", type=["fasta"])

# Function to load FASTA sequences
def load_fasta(file_path):
    with open(file_path, "r") as file:
        record = SeqIO.read(file, "fasta")
    return str(record.seq)

# Load sequences (use uploaded files if available, otherwise use default)
if ref_file and var_file:
    reference_seq = SeqIO.read(io.StringIO(ref_file.getvalue().decode("utf-8")), "fasta").seq
    variant_seq = SeqIO.read(io.StringIO(var_file.getvalue().decode("utf-8")), "fasta").seq
    st.sidebar.success("Using uploaded FASTA files!")
else:
    reference_seq = load_fasta(default_ref_file_path)
    variant_seq = load_fasta(default_var_file_path)
    st.sidebar.info("Using pre-loaded SARS-CoV-2 reference and Omicron variant sequences.")

# Display genome lengths
st.subheader("Genome Information")
col1, col2 = st.columns(2)
col1.metric("Reference Genome Length", f"{len(reference_seq)} bp")
col2.metric("Variant Genome Length", f"{len(variant_seq)} bp")

# Function to find SNPs
def find_snps(ref_seq, var_seq):
    snps = []
    for i, (ref_nuc, var_nuc) in enumerate(zip(ref_seq, var_seq)):
        if ref_nuc != var_nuc:
            snps.append((i, ref_nuc, var_nuc))
    return snps

# Find SNPs
snps = find_snps(reference_seq, variant_seq)

# Display SNP summary
st.subheader("SNP Detection Results")
st.write(f"**Total SNPs Found:** {len(snps)}")

# Explain what the SNP table shows
st.markdown("""
**What Does This Table Show?**
- **Position**: The exact location of the mutation in the genome.
- **Reference Nucleotide**: The original nucleotide in the reference genome.
- **Variant Nucleotide**: The changed nucleotide in the variant genome.

These mutations could be:
- **Silent mutations** (no effect on protein function).
- **Missense mutations** (change protein structure).
- **Nonsense mutations** (can stop protein synthesis prematurely).
""")

# Show first 10 SNPs
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

# Side-by-side layout for SNP Distribution and SNP Classification
st.subheader("Data Analysis")

# Create two columns
col1, col2 = st.columns(2)

# SNP Distribution Histogram (Left)
with col1:
    st.markdown("#### SNP Distribution Across the Genome")
    fig, ax = plt.subplots(figsize=(4, 2))  # Smaller size
    ax.hist(snp_positions, bins=75, color='purple', alpha=0.7)
    ax.set_xlabel("Genome Position", fontsize=8)
    ax.set_ylabel("SNP Frequency", fontsize=8)
    ax.set_title("SNP Distribution", fontsize=10)
    ax.tick_params(axis='both', labelsize=6)  # Smaller tick labels
    st.pyplot(fig)

# SNP Classification Pie Chart (Right)
with col2:
    st.markdown("#### SNP Type Proportion")
    fig2, ax2 = plt.subplots(figsize=(3, 3))  # Smaller size
    ax2.pie(
        snp_classification.values(),
        labels=snp_classification.keys(),
        autopct='%1.1f%%',
        colors=['blue', 'orange'],
        textprops={'fontsize': 6}  # Smaller text
    )
    ax2.set_title("SNP Types", fontsize=8)
    st.pyplot(fig2)



# # SNP Distribution Plot
# st.subheader("📊 SNP Distribution Across the Genome")
# fig, ax = plt.subplots(figsize=(6, 3))  # Smaller plot
# ax.hist(snp_positions, bins=75, color='purple', alpha=0.7)
# ax.set_xlabel("Genome Position", fontsize=10)
# ax.set_ylabel("SNP Frequency", fontsize=10)
# ax.set_title("Distribution of SNPs Across the Genome", fontsize=12)
# ax.tick_params(axis='both', labelsize=8)  # Smaller tick labels
# st.pyplot(fig)




# #Pie Chart for SNP Classification
# fig2, ax2 = plt.subplots(figsize=(4, 4))  # Smaller pie chart
# ax2.pie(
#     snp_classification.values(),
#     labels=snp_classification.keys(),
#     autopct='%1.1f%%',
#     colors=['blue', 'orange'],
#     textprops={'fontsize': 8}  # Smaller text
# )
# ax2.set_title("Comparison of SNP Types", fontsize=10)
# st.pyplot(fig2)

# Conclusion
st.markdown("""
### Key Takeaways:
- **SNPs (mutations) are common in viral genomes** and can affect **viral transmissibility and vaccine resistance**.
- **Transitions (A↔G, C↔T) are more frequent** because they preserve chemical structure.
- **Transversions (A↔C, A↔T, G↔C, G↔T) are less common** but may have stronger functional effects.

**Want to explore?** You can upload **different viral genome sequences** to compare their mutations!
""")
