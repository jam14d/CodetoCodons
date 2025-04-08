import pandas as pd
import os

def load_and_filter_clinvar(filepath: str, cache_path: str = "data/filtered_clinvar.csv") -> pd.DataFrame:
    """
    Loads and filters ClinVar variant summary data for binary classification.
    If a filtered version exists, load it instead to save time.
    """

    if os.path.exists(cache_path):
        print(f"Loading cached data from {cache_path}...")
        return pd.read_csv(cache_path)

    print("Loading full ClinVar file and filtering...")
    
    usecols = [
        'GeneSymbol', 'ClinicalSignificance', 'Chromosome',
        'Start', 'ReferenceAllele', 'AlternateAllele', 'Assembly', 'Type'
    ]
    
    #df = pd.read_csv(filepath, sep='\t', usecols=usecols, low_memory=False)

    # Treat "na" as missing
    df = pd.read_csv(filepath, sep='\t', usecols=usecols, na_values="na", low_memory=False)


    # Filter data
    df = df[
        (df['Assembly'] == 'GRCh37') &
        (df['Type'] == 'single nucleotide variant') &
        (df['ClinicalSignificance'].isin(['Benign', 'Pathogenic']))
    ]
    
    df = df.dropna(subset=[
        'GeneSymbol', 'ClinicalSignificance', 'Chromosome',
        'Start', 'ReferenceAllele', 'AlternateAllele'
    ])
    
    df['Label'] = df['ClinicalSignificance'].map({'Benign': 0, 'Pathogenic': 1})
    df = df.reset_index(drop=True)

    # Save filtered version
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    df.to_csv(cache_path, index=False)
    print(f"Filtered data saved to {cache_path}.")

    return df
