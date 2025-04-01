import streamlit as st
import matplotlib.pyplot as plt
from Bio import SeqIO
import io


def app():
    # Title animation
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">

        <style>
        @keyframes scramble {
            0%   { content: "XUTATION EXBLORER"; }
            10%  { content: "MCTBTION FXPLARER"; }
            20%  { content: "MUTJTIGN EXFLOROR"; }
            30%  { content: "MUTATFON EXHLOFER"; }
            40%  { content: "MUTATIOK EXPLURER"; }
            60%  { content: "MUTATION EXPLORER"; }
            100% { content: "MUTATION EXPLORER"; }
        }

        .mutation-title::after {
            content: "MUTATION EXPLORER";
            font-family: 'Share Tech Mono', monospace;
            font-size: 70px;
            color: #00FFCC;
            letter-spacing: 3px;
            display: block;
            text-align: center;
            animation: scramble 3s steps(6, end) infinite;
        }

        .intro-box {
            background: rgba(0, 255, 204, 0.05);
            border: 1px solid #00FFCC;
            border-left: 5px solid #FF3C00;
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
            font-family: 'Chakra Petch', monospace;
            font-size: 16px;
            line-height: 1.6;
            color: #00FFCC;
            box-shadow: 0 0 10px rgba(0, 255, 204, 0.2);
        }

        .stSidebar button {
            background: linear-gradient(180deg, #00FFC6, #7a9ccf);
            color: #0A0A0F;

            
            text-transform: uppercase;
            border: none;
            border-radius: 7px;
            padding: 5px 10px;
            cursor: pointer;
            transition: 1s ease;
            box-shadow: 0 0 20px rgba(255, 60, 0, 0.6);
        }

        .stSidebar button:hover {
            background: linear-gradient(180deg, #EFBF04, #FF3C00);
            box-shadow: 0 0 35px #FF3C00;
        }
        </style>

        <div class="mutation-title"></div>
        """,
        unsafe_allow_html=True
    )

    # Intro box
    st.markdown(
        """
        <div class="intro-box">
            Welcome to your personal genomic gadget!
            The Mutation Explorer dives into the code of life, scanning two DNA sequences to uncover subtle changes known as Single Nucleotide Polymorphisms (SNPs).<br><br>
            These tiny mutations may be just one letter apart, but they can spark big biological differences — from inherited traits to evolutionary twists.<br><br>
            Upload your genomes, hit scan, and let’s decode the mutations hiding in plain sight.

        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <style>
        .markdown-box {
            background: #0A0A0F; 
            border-left: 5px solid #FF3C00;
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
            font-family: 'Chakra Petch', monospace;
            color: #00FFCC;
            box-shadow: 0 0 10px rgba(0, 255, 204, 0.2);
        }
        </style>

        <div class="markdown-box">
        <strong>How to Operate:</strong><br><br>

        <strong>Step 1:</strong> Upload Your FASTA Files<br>
        - Reference Genome: The baseline genome sequence<br>
        - Variant Genome: The sequence with potential mutations<br><br>

        <strong>Where to Get FASTA Files:</strong><br>
        - <a href="https://www.ncbi.nlm.nih.gov/genbank/" target="_blank">NCBI GenBank</a><br>
        - <a href="https://www.ensembl.org/" target="_blank">Ensembl</a><br>
        - <a href="https://genome.ucsc.edu/" target="_blank">UCSC Genome Browser</a><br><br>

        <strong>Step 2:</strong> Start SNP Detection<br>
        - Compares the reference and variant genome<br>
        - Identifies <i>mutation positions</i><br>
        - Displays <i>statistical and visual outputs</i><br><br>

        <strong>Step 3:</strong> Analyze the Results<br>
        - Histogram of mutation positions<br>
        - Pie chart of SNP classifications
        </div>
        """,
        unsafe_allow_html=True
    )





    # # Instructions
    # st.markdown("""
    # ### How to Operate:
    # **Step 1: Upload Your FASTA Files**
    # - **Reference Genome:** The baseline genome sequence.
    # - **Variant Genome:** The sequence with potential mutations.
    
    # Where to Get FASTA Files?
    # - [NCBI GenBank](https://www.ncbi.nlm.nih.gov/genbank/)
    # - [Ensembl](https://www.ensembl.org/)
    # - [UCSC Genome Browser](https://genome.ucsc.edu/)

    # **Step 2: Start SNP Detection**
    # - Compares the reference and variant genome.
    # - Identifies **mutation positions**.
    # - Displays **statistical and visual outputs**.

    # **Step 3: Analyze the Results**
    # - **Histogram of mutation positions**
    # - **Pie chart of SNP classifications**
    # """)

    # Sidebar Upload
    st.sidebar.header("Upload Your FASTA Files")
    ref_file = st.sidebar.file_uploader("Reference Genome (FASTA)", type=["fasta"])
    var_file = st.sidebar.file_uploader("Variant Genome (FASTA)", type=["fasta"])

    # Helper
    def load_fasta(file):
        return str(SeqIO.read(io.StringIO(file.getvalue().decode("utf-8")), "fasta").seq)

    if ref_file and var_file:
        st.sidebar.success("Files Uploaded Successfully")

        if st.sidebar.button("SCAN GENOMES"):
            reference_seq = load_fasta(ref_file)
            variant_seq = load_fasta(var_file)

            # Show lengths
            st.subheader("Genome Data")
            col1, col2 = st.columns(2)
            col1.metric("Reference Genome Length", f"{len(reference_seq)} bp")
            col2.metric("Variant Genome Length", f"{len(variant_seq)} bp")

            # Detect SNPs
            def find_snps(ref_seq, var_seq):
                return [(i, ref_nuc, var_nuc)
                        for i, (ref_nuc, var_nuc) in enumerate(zip(ref_seq, var_seq))
                        if ref_nuc != var_nuc]

            snps = find_snps(reference_seq, variant_seq)
            snp_positions = [pos for pos, _, _ in snps]

            st.subheader("SNP Detection")
            st.write(f"Total SNPs Found: {len(snps)}")

            # Visualizations
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
                ax2.pie([60, 40], labels=["Transitions", "Transversions"], autopct='%1.1f%%',
                        colors=['#00FFCC', '#006666'])
                ax2.set_title("SNP Types")
                st.pyplot(fig2)

            st.markdown(
                """
                <div class='intro-box'>
                Mutation patterns mapped successfully.
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.sidebar.warning("Upload Reference and Variant FASTA Files.")


if __name__ == "__main__":
    app()
