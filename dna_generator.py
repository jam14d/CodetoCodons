from string_reader import StringReader
from character_capitalizer import CharacterCapitalizer
from dna_base_converter import DNABaseConverter
from space_remover import SpaceRemover
from special_characters_remover import SpecialCharactersRemover
from pipeline import Pipeline

def save_output_to_file(output, file_path='output.txt'):
    """
    Saves the given output to a text file.
    
    :param output: The text to save.
    :param file_path: The path of the file where the output will be saved.
    """
    with open(file_path, 'w') as file:
        file.write(output)
    print(f"Output saved to {file_path}")

def run_pipeline(input_string, save_to_file=True, file_path="DNA_output.txt"):
    """
    Runs the transformation pipeline on an input string, optionally saving the output to a file.

    :param input_string: The text to process through the pipeline.
    :param save_to_file: Boolean indicating whether to save the output to a file.
    :param file_path: The path to the file where the output will be saved if save_to_file is True.
    """
    # Instantiate the pipeline
    pipeline = Pipeline()

    # Add stages to the pipeline
    pipeline.add(StringReader())
    pipeline.add(CharacterCapitalizer())
    pipeline.add(DNABaseConverter())
    pipeline.add(SpaceRemover())
    pipeline.add(SpecialCharactersRemover())

    # Execute the pipeline
    output = pipeline.execute(input_string)

    # Print output
    print(output)

    # Optional: Save output to a file
    if save_to_file:
        save_output_to_file(output, file_path)

    return output

if __name__ == "__main__":
    # Input string
    input_string = "HELLOOOO. I really need a job, please! I am living off unemployment and was laid off in late January of 2024 and it's a bummer!"

    # Call run_pipeline function with the input string and default parameters
    run_pipeline(input_string)
