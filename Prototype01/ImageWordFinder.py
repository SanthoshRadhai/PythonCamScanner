from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog
import re

class ImageTextAnalyzer:
    def __init__(self, tesseract_cmd=None):
        """
        Initialize the ImageTextAnalyzer class and optionally set the path to the Tesseract-OCR executable.
        """
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def image_to_text(self, image_path):
        """
        Convert the image at the given path to text using OCR.
        
        :param image_path: Path to the image file
        :return: Extracted text from the image
        """
        # Open the image
        img = Image.open(image_path)
        
        # Perform OCR on the image
        text = pytesseract.image_to_string(img)
        
        return text

    def count_elements(self, text):
        """
        Count and print the total number of words, numericals, and symbols in the given text.
        
        :param text: The text to analyze
        """
        # Regular expression patterns for words, numericals, and symbols
        words = re.findall(r'\b\w+\b', text)  # Words (any sequence of letters, numbers, or underscores)
        numericals = re.findall(r'\b\d+\b', text)  # Numericals (digits only)
        symbols = re.findall(r'[^\w\s]', text)  # Symbols (non-alphanumeric characters, excluding spaces)

        # Print counts
        print(f"Total number of words: {len(words)}")
        print(f"Total number of numericals: {len(numericals)}")
        print(f"Total number of symbols: {len(symbols)}")

    def get_image_from_user(self):
        """
        Open a file dialog to allow the user to select an image file and process it to extract and analyze text.
        """
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        
        if file_path:
            extracted_text = self.image_to_text(file_path)
            self.count_elements(extracted_text)  # Count words, numericals, and symbols
        else:
            print("No file selected.")

# Example usage
if __name__ == "__main__":
    # Initialize the analyzer (optionally set the Tesseract-OCR path)
    analyzer = ImageTextAnalyzer(tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe')  # Adjust for Windows if needed
    
    # Run the function to get an image from the user and process it
    analyzer.get_image_from_user()
