from rdkit import Chem
from rdkit.Chem import Draw
import streamlit as st
import os

# Dictionary mapping one-letter amino acid codes to SMILES notation
aa_smiles = {
    "A": "CC(C)C(=O)O",      # Alanine
    "R": "NC(CCCNC(N)=N)C(=O)O",  # Arginine
    "N": "NC(CC(=O)N)C(=O)O",  # Asparagine
    "D": "NC(CC(=O)O)C(=O)O",  # Aspartic Acid
    "C": "NC(CS)C(=O)O",      # Cysteine
    "E": "NC(CCC(=O)O)C(=O)O",  # Glutamic Acid
    "Q": "NC(CCC(=O)N)C(=O)O",  # Glutamine
    "G": "C(C(=O)O)N",        # Glycine
    "H": "NC(CC1=CNC=N1)C(=O)O",  # Histidine
    "I": "CC(C)CC(C(=O)O)N",  # Isoleucine
    "L": "CC(C)CC(C(=O)O)N",  # Leucine
    "K": "NC(CCCCN)C(=O)O",   # Lysine
    "M": "CSCC(C(=O)O)N",     # Methionine
    "F": "NC(CC1=CC=CC=C1)C(=O)O",  # Phenylalanine
    "P": "C1CC(NC1)C(=O)O",   # Proline
    "S": "NC(CO)C(=O)O",      # Serine
    "T": "CC(O)C(C(=O)O)N",   # Threonine
    "W": "NC(CC1=CNC2=CC=CC=C12)C(=O)O",  # Tryptophan
    "Y": "NC(CC1=CC=C(O)C=C1)C(=O)O",  # Tyrosine
    "V": "CC(C)C(C(=O)O)N"    # Valine
}

def generate_amino_acid_image(sequence, filename="amino_acids.png"):
    """
    Generates a 2D image of the amino acid sequence using RDKit and saves it.
    """
    mols = [Chem.MolFromSmiles(aa_smiles[aa]) for aa in sequence if aa in aa_smiles]

    if not mols:
        print("Error: No valid amino acids found in sequence!")
        return None

    img = Draw.MolsToGridImage(mols, molsPerRow=4, subImgSize=(200,200), legends=[aa for aa in sequence if aa in aa_smiles])

    img_path = os.path.join(os.getcwd(), filename)
    img.save(img_path)

    return img_path  # Return file path for Streamlit display

# Test the function
if __name__ == "__main__":
    test_sequence = "MVTTTY"
    output_img = generate_amino_acid_image(test_sequence)
    print(f"Amino acid structure image saved at: {output_img}")
