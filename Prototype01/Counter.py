import re

class TextAnalyzer:
    def __init__(self, text):
        """
        Initialize the TextAnalyzer with the text to analyze.
        """
        self.text = text

    def count_words(self):
        """
        Count the total number of words in the text.
        Words are defined as sequences of alphanumeric characters.
        """
        words = re.findall(r'\b\w+\b', self.text)
        return len(words)

    def count_alphabets(self):
        """
        Count the total number of alphabetic characters in the text.
        """
        alphabets = re.findall(r'[a-zA-Z]', self.text)
        return len(alphabets)

    def count_numbers(self):
        """
        Count the total number of numerical sequences in the text.
        """
        numbers = re.findall(r'\d+', self.text)
        return len(numbers)

    def count_symbols(self):
        """
        Count the total number of symbols (non-alphanumeric and non-whitespace) in the text.
        """
        symbols = re.findall(r'[^\w\s]', self.text)
        return len(symbols)

# Example usage
if __name__ == "__main__":
    # Sample text
    sample_text = "Artificial! 1231# #@!"
    
    # Initialize the TextAnalyzer with the sample text
    analyzer = TextAnalyzer(sample_text)
    
    # Get counts
    total_words = analyzer.count_words()
    total_alphabets = analyzer.count_alphabets()
    total_numbers = analyzer.count_numbers()
    total_symbols = analyzer.count_symbols()
    
    # Print results
    print(f"Total number of words: {total_words}")
    print(f"Total number of alphabets: {total_alphabets}")
    print(f"Total number of numbers: {total_numbers}")
    print(f"Total number of symbols: {total_symbols}")
