import re
# re — Regular expression operations

class SpecialCharactersRemover:
    def process(self, text):
        """Removes any character that is not a letter (a-z, A-Z) from the text."""
        return re.sub(r'[^a-zA-Z]', '', text)
