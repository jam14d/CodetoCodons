import dna_generator  # Import the module

def transcribe_dna_to_rna(dna_sequence):
    """
    Transcribes a DNA sequence into an RNA sequence by replacing every "T" with "U".
    
    :param dna_sequence: A string representing the DNA sequence.
    :return: A string representing the RNA sequence.
    """
    rna_sequence = dna_sequence.replace("T", "U")
    return rna_sequence

def save_to_file(content, file_name="rna_sequence.txt"):
    """
    Saves the given content to a text file.
    
    :param content: The text to save.
    :param file_name: The name of the file to save the content in.
    """
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Content saved to {file_name}")

if __name__ == "__main__":
    # Define an input string
    input_string = "I need a jobbbbbb!!! thank you!"
    
    # Flag to control saving to file
    save_to_file_flag = True  # Change to False if you do not want to save the output to a file
    
    # Use the `run_pipeline` function from the imported `dna_generator` module to process the input string
    # and generate a DNA sequence.
    dna_sequence = dna_generator.run_pipeline(input_string, save_to_file=False)
    
    print("DNA Sequence:", dna_sequence)
    
    # Transcribe the DNA sequence into RNA
    rna_sequence = transcribe_dna_to_rna(dna_sequence)
    print("RNA Sequence:", rna_sequence)

    # Optional: Save the RNA sequence to a file
    if save_to_file_flag:
        save_to_file(rna_sequence, "RNA_output.txt")
