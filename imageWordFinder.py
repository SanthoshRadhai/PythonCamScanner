from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog
import re

# Set the path to Tesseract-OCR (if necessary)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to convert image to text
def image_to_text(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    
    return text

# Function to count words, numericals, and symbols
def count_elements(text):
    # Regular expression patterns for words, numericals, and symbols
    words = re.findall(r'\b\w+\b', text)  # Words (any sequence of letters, numbers, or underscores)
    numericals = re.findall(r'\b\d+\b', text)  # Numericals (digits only)
    symbols = re.findall(r'[^\w\s]', text)  # Symbols (non-alphanumeric characters, excluding spaces)

    # Print counts
    print(f"Total number of words: {(words)}")
    print(f"Total number of numericals: {len(numericals)}")
    print(f"Total number of symbols: {len(symbols)}")

# Function to open file dialog and get image from the user
def get_image_from_user():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        extracted_text = image_to_text(file_path)
        count_elements(extracted_text)  # Count words, numericals, and symbols
    else:
        print("No file selected.")

# Run the function to get image and process it
get_image_from_user()
