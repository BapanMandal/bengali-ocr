import os
import shutil
import subprocess
import argparse
from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document

    

def main():

    # ================== Argument Parser ==================
    # create parser object
    parser = argparse.ArgumentParser(
        prog='ocr_tess',
        description='Bengali PDFs to Text using Tesseract OCR',
        epilog='[Created by: Bapan Mandal, Feb 2024]'
    )

    # defining arguments for parser object
    parser.add_argument('input', help='Path to the input PDF file')

    # defining options for parser object
    parser.add_argument('-o', '--output', default='./ocr_outputs/', help='Path to the output text files (UTF-8 encoded)')

    # parse the arguments from standard input
    args = parser.parse_args()

    # print(f'$$ Args.input = {args.input}\n')




    # ================== Split the PDF into chunks of 50 pages =================

    # Construct the command to run the R script
    command = ["Rscript", './split_pdf.r', args.input]

    
    # Run the command and capture the output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()




    # ================== PDF to Text Extraction ==================
    # Get list of split PDFs
    split_pdfs = [f for f in os.listdir('split_pdfs') if f.endswith('.pdf')]

    ocr_outputs='ocr_outputs'
    try:
        os.mkdir(ocr_outputs)
    except FileExistsError:
        shutil.rmtree(ocr_outputs)
        

    # Process each split PDF using OCR
    for pg_cnt, pdf in enumerate(split_pdfs):
        # subprocess.run(["python", "ocr_tess.py", os.path.join('output_pdfs', pdf)])
        # create document for extraction with configurations
        pdf_document = Document(
            document_path='split_pdfs/'+pdf,
            language='Bengali'
        )
        pdf2text = PDF2Text(document=pdf_document)
        content = pdf2text.extract()

        # get size of content
        print(f'PDF OCRed = {pdf}')
        print(f'Number of pages OCRed: {len(content)}\n')

        with open(args.output+f'{pdf[:-4]}.txt', 'w', encoding="utf-8") as f:
            for i in range(len(content)):
                f.write(content[i]['text'])
                f.write("\n")

    # Remove the split PDFs
    shutil.rmtree('split_pdfs')

    print(f'OCR outputs saved to: {args.output}')

if __name__ == "__main__":
    main()