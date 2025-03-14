import random

class DNABaseConverter:
    def process(self, chars):
        # Function to decide replacement based on the character
        def replace_char(char):
            vowels = 'AEIOU'
            if char in vowels:
                return 'A'
            elif char.isalpha():  # Check if it's a consonant (assuming only letters are processed)
                return random.choice(['T', 'C', 'G'])
            else:
                return char  # Non-alphabetic characters remain unchanged
        
        # Apply replacement to each character
        return ''.join(replace_char(char) for char in chars)
