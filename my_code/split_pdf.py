import os
import sys
from PyPDF2 import PdfReader, PdfWriter

print("Current Working Directory:", os.getcwd())

def split_pdf(input_pdf):

    output_folder = "/home/uverma/Documents/code/My_Ganga/my_code/output_pages"   # make out directory if not exist
    os.makedirs(output_folder, exist_ok=True)   
    
    reader = PdfReader(input_pdf)   # load PDF
    num_pages = len(reader.pages)

    output_files = []   # out_file path
    for i in range(num_pages):

        writer = PdfWriter()   # add each new page
        writer.add_page(reader.pages[i])

        output_filename = os.path.join(output_folder, f"page_{i+1}.pdf")   # saves each file at path
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Type : python my_code/split_pdf.py LHC.pdf")
        sys.exit(1)

    input_pdf = sys.argv[1]
    split_pdf(input_pdf)
