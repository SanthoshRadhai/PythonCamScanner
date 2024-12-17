from PIL import Image
import pytesseract

class ImageToTextConverter:
    def __init__(self, tesseract_cmd=None):
        if tesseract_cmd:
            # Set the path to the tesseract executable (only required for Windows)
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    
    def image_to_text(self, image_path):
        """
        Convert image to text using OCR.

        :param image_path: Path to the image file
        :return: Extracted text from the image
        """
        # Open the image
        img = Image.open(image_path)
        
        # Perform OCR on the image using pytesseract
        text = pytesseract.image_to_string(img)
        
        return text

# Example usage
if __name__ == "__main__":
    # Adjust the tesseract_cmd if needed for your OS (Windows only)
    tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Uncomment and adjust on Windows

    # Initialize the converter
    converter = ImageToTextConverter(tesseract_cmd=tesseract_cmd)
    
    # Input image path
    image_path = 'img.png'  # Adjust this path to the location of your image file
    
    # Extract text from the image
    extracted_text = converter.image_to_text(image_path)
    
    # Print the extracted text
    print(extracted_text)
