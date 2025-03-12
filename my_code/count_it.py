import sys
from PyPDF2 import PdfReader

def count_word_it(pdf_file):

    word_to_count = "it"
    reader = PdfReader(pdf_file)  

    text = reader.pages[0].extract_text() or ""

    words = [word.strip('.,!?;:"()[]') for word in text.split()]    # strips punctuation 
    count = sum(1 for word in words if word.lower() == word_to_count)

    print(count)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_it.py <pdf_file>")
        sys.exit(1)

    count_word_it(sys.argv[1])
