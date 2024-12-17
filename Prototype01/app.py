from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import re


class ImageToTextConverter:
    def __init__(self, tesseract_cmd=None):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def image_to_text(self, image_path):
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text


class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        words = re.findall(r'\b\w+\b', self.text)
        return len(words)

    def count_alphabets(self):
        alphabets = re.findall(r'[a-zA-Z]', self.text)
        return len(alphabets)

    def count_numbers(self):
        numbers = re.findall(r'\d+', self.text)
        return len(numbers)

    def count_symbols(self):
        symbols = re.findall(r'[^\w\s]', self.text)
        return len(symbols)


class ImageTextAnalyzer:
    def __init__(self, tesseract_cmd=None):
        if tesseract_cmd:
            pytesseract.pytesseract_cmd = tesseract_cmd

    def image_to_text(self, image_path):
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text

    def count_elements(self, text):
        words = re.findall(r'\b\w+\b', text)
        numericals = re.findall(r'\b\d+\b', text)
        symbols = re.findall(r'[^\w\s]', text)
        return len(words), len(numericals), len(symbols)


from transformers import pipeline

class TextSummarizer:
    def __init__(self):
        # Initialize the summarization pipeline
        self.summarizer = pipeline("summarization")

    def summarize(self, text, max_length=150, min_length=30):
        """
        Summarize the text using transformers.

        :param text: The text to summarize
        :param max_length: Maximum length of the summary
        :param min_length: Minimum length of the summary
        :return: Summary of the text
        """
        summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']



class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("OCR and Text Analysis")
        self.master.geometry("500x300")
        self.master.configure(bg="#f0f0f0")

        self.converter = ImageToTextConverter()
        self.text_analyzer = TextAnalyzer
        self.image_text_analyzer = ImageTextAnalyzer()
        self.text_summarizer = TextSummarizer()  # Initialize the TextSummarizer

        Label(master, text="Select a Functionality", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=20)

        button_style = {"font": ("Helvetica", 12), "bg": "#007ACC", "fg": "white", "width": 20, "height": 2}
        Button(master, text="Convert Image to Text", command=self.open_image_to_text_window, **button_style).pack(pady=10)
        Button(master, text="Text Analysis", command=self.open_text_analysis_window, **button_style).pack(pady=10)
        Button(master, text="Image Text Analyzer", command=self.open_image_text_analyzer_window, **button_style).pack(pady=10)
        Button(master, text="Text Summarizer", command=self.open_text_summarizer_window, **button_style).pack(pady=10)

    def open_image_to_text_window(self):
        # Create a new window for Image to Text conversion
        new_window = Toplevel(self.master)
        new_window.title("Image to Text Conversion")
        new_window.geometry("500x300")
        new_window.configure(bg="#e6f7ff")

        def open_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                try:
                    extracted_text = self.converter.image_to_text(file_path)
                    text_area.delete(1.0, END)
                    text_area.insert(INSERT, extracted_text)
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

        Label(new_window, text="Convert Image to Text", font=("Helvetica", 14, "bold"), bg="#e6f7ff").pack(pady=10)
        
        Button(new_window, text="Select Image", command=open_image, font=("Helvetica", 12), bg="#007ACC", fg="white").pack(pady=10)
        
        text_area = Text(new_window, height=10, width=60, wrap=WORD, font=("Helvetica", 12))
        text_area.pack(pady=10, padx=10, fill=BOTH, expand=True)



    def open_text_summarizer_window(self):
        # Create a new window for Text Summarization
        new_window = Toplevel(self.master)
        new_window.title("Text Summarization")
        new_window.geometry("500x300")
        new_window.configure(bg="#e6f7ff")

        Label(new_window, text="Enter text to summarize:", font=("Helvetica", 12), bg="#e6f7ff").pack(pady=10)
        text_entry = Text(new_window, height=5, width=50, wrap=WORD, font=("Helvetica", 10))
        text_entry.pack(pady=10)

        Label(new_window, text="Summary Length (max length of summary):", font=("Helvetica", 12), bg="#e6f7ff").pack(pady=10)
        summary_length_entry = Entry(new_window, font=("Helvetica", 12))
        summary_length_entry.pack(pady=10)

    def open_text_analysis_window(self):
        new_window = Toplevel(self.master)
        new_window.title("Text Analysis")
        new_window.geometry("500x300")
        new_window.configure(bg="#e6f7ff")

        Label(new_window, text="Enter text to analyze:", font=("Helvetica", 12), bg="#e6f7ff").pack(pady=10)
        text_entry = Text(new_window, height=5, width=50, wrap=WORD, font=("Helvetica", 10))
        text_entry.pack(pady=10)

        def analyze_text():
            text = text_entry.get("1.0", END).strip()
            analyzer = TextAnalyzer(text)
            words = analyzer.count_words()
            alphabets = analyzer.count_alphabets()
            numbers = analyzer.count_numbers()
            symbols = analyzer.count_symbols()
            messagebox.showinfo("Analysis Result",
                                f"Words: {words}\nAlphabets: {alphabets}\nNumbers: {numbers}\nSymbols: {symbols}")

        Button(new_window, text="Analyze Text", command=analyze_text, font=("Helvetica", 12), bg="#007ACC", fg="white").pack(pady=10)

    def open_image_text_analyzer_window(self):
        new_window = Toplevel(self.master)
        new_window.title("Image Text Analyzer")
        new_window.geometry("500x300")
        new_window.configure(bg="#e6f7ff")

        def open_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                extracted_text = self.image_text_analyzer.image_to_text(file_path)
                words, numericals, symbols = self.image_text_analyzer.count_elements(extracted_text)
                messagebox.showinfo("Analysis Result",
                                    f"Words: {words}\nNumericals: {numericals}\nSymbols: {symbols}")

        Button(new_window, text="Select Image", command=open_image, font=("Helvetica", 12), bg="#007ACC", fg="white").pack(pady=10)

    def open_text_summarizer_window(self):
        # Create a new window for Text Summarization

        new_window = Toplevel(self.master)
        new_window.title("Text Summarization")
        new_window.geometry("500x300")
        new_window.configure(bg="#e6f7ff")


        Label(new_window, text="Enter text to summarize:", font=("Helvetica", 12), bg="#e6f7ff").pack(pady=10)
        text_entry = Text(new_window, height=5, width=50, wrap=WORD, font=("Helvetica", 10))
        text_entry.pack(pady=10)

        Label(new_window, text="Summary Size (number of sentences):", font=("Helvetica", 12), bg="#e6f7ff").pack(pady=10)
        summary_size_entry = Entry(new_window, font=("Helvetica", 12))
        summary_size_entry.pack(pady=10)
        
        summary_length_entry = Entry(new_window, font=("Helvetica", 12))
        summary_length_entry.pack(pady=10)

        def summarize_text():
            text = text_entry.get("1.0", END).strip()
            summary_length = int(summary_length_entry.get().strip())  # Convert the entry value to integer
            summary = self.text_summarizer.summarize(text, max_length=summary_length)
            messagebox.showinfo("Summary Result", summary)

        Button(new_window, text="Generate Summary", command=summarize_text, font=("Helvetica", 12), bg="#007ACC", fg="white").pack(pady=10)


# Initialize and run the application
if __name__ == "__main__":
    root = Tk()
    app = MainApplication(root)
    root.mainloop()
