import pandas as pd

def load_and_filter_clinvar(filepath: str) -> pd.DataFrame:
    """
    Loads and filters ClinVar variant summary data for binary classification.
    
    https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/
    
    Keeps only SNVs labeled as 'Benign' or 'Pathogenic' for binary classification.
    """
    # Load file
    df = pd.read_csv(filepath, sep='\t', low_memory=False)
    
    # Keep only GRCh37 human data (optional)
    df = df[df['Assembly'] == 'GRCh37']
    df = df[df['Type'] == 'single nucleotide variant']
    
    # Filter for binary classification
    df = df[df['ClinicalSignificance'].isin(['Benign', 'Pathogenic'])]
    
    # Keep only relevant columns
    df = df[[
        'GeneSymbol', 'ClinicalSignificance',
        'Chromosome', 'Start', 'ReferenceAllele', 'AlternateAllele'
    ]]

    # Encode labels: Benign = 0, Pathogenic = 1
    df['Label'] = df['ClinicalSignificance'].map({'Benign': 0, 'Pathogenic': 1})
    
    # Drop rows with missing values
    df = df.dropna()

    return df.reset_index(drop=True)
