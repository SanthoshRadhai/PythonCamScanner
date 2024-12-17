import re

# Sample text (Replace this with your extracted text)
text = "Artificial! 1231# #@!"

# Function to count total number of words
def count_words(text):
    # Count words as sequences of alphabetic characters
    words = re.findall(r'\b\w+\b', text)  # Changed pattern to include words with hyphens or apostrophes
    return len(words)

# Function to count total number of alphabets
def count_alphabets(text):
    # Count all alphabetic characters
    alphabets = re.findall(r'[a-zA-Z]', text)
    return len(alphabets)

# Function to count total number of numbers
def count_numbers(text):
    # Count all sequences of digits
    numbers = re.findall(r'\d+', text)
    return len(numbers)

# Function to count total number of symbols
def count_symbols(text):
    # Count all characters that are not alphanumeric or whitespace
    symbols = re.findall(r'[^\w\s]', text)
    return len(symbols)

# Get counts
total_words = count_words(text)
total_alphabets = count_alphabets(text)
total_numbers = count_numbers(text)
total_symbols = count_symbols(text)

# Print results
print(f"Total number of words: {total_words}")
print(f"Total number of alphabets: {total_alphabets}")
print(f"Total number of numbers: {total_numbers}")
print(f"Total number of symbols: {total_symbols}")
