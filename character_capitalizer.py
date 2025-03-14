class CharacterCapitalizer:
    """Capitalizes each character in the string."""
    def process(self, text):
        return [char.upper() for char in text]
