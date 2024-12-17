from PIL import Image
import pytesseract

# Specify the path to tesseract executable (required for Windows)
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to convert image to text
def image_to_text(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    
    return text

# Input image path
image_path = 'img.png'  # Adjust this path to the location of your image file

# Call the function and get the text
extracted_text = image_to_text(image_path)

# Print the extracted text
print(extracted_text)
