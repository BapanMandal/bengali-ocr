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
        description='Converts Bengali PDFs to Text using Tesseract OCR',
        epilog='[Created by: Bapan Mandal, Feb 2024]'
    )

    # defining arguments for parser object
    parser.add_argument('input', help='Path to the input PDF file')

    # defining options for parser object
    parser.add_argument('-o', '--output', default='ocr_outputs', help='Name of the output folder where OCR outputs will be saved. (Default: "ocr_outputs")')

    # parse the arguments from standard input
    args = parser.parse_args()

    # ======================================================





    # ================== Split the PDF into chunks of 50 pages =================

    # Construct the command to run the R script
    command = ["sudo", "Rscript", './split_pdf.r', args.input]

    # Run the command and capture the output
    process = subprocess.Popen(command, stderr=subprocess.PIPE)
    process.wait()

    # The output of the R script is in the split_pdfs folder
    split_pdfs_dir = 'split_pdfs/'

    # ==========================================================================





    # ================== PDF to Text Extraction ==================

    # Get list of split PDFs
    split_pdfs = [f for f in os.listdir(split_pdfs_dir) if f.endswith('.pdf')]

    ocr_outputs = args.output+'/'
    try:
        os.mkdir(ocr_outputs)
    except FileExistsError:
        try:
            subprocess.run(['sudo', 'rm', '-rf', ocr_outputs], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        os.mkdir(ocr_outputs)


    # Process each split PDF using OCR
    for pg_cnt, pdf_filename in enumerate(split_pdfs):

        # create document for extraction with configurations
        pdf_document = Document(
            document_path = split_pdfs_dir+pdf_filename,
            language = 'Bengali'
        )

        print(f'Processing PDF {pg_cnt+1} of {len(split_pdfs)}: {pdf_filename} ...')

        # extract text from the document
        pdf2text = PDF2Text(document=pdf_document)
        content = pdf2text.extract()

        # get details of the job done
        print(f'PDF OCRed = {pdf_filename}')
        print(f'Number of pages OCRed: {len(content)}\n')

        # Save the OCR outputs to a text file
        with open(ocr_outputs+f'{pdf_filename[:-4]}.txt', 'w', encoding="utf-8") as f:
            for i in range(len(content)):
                f.write(content[i]['text'])
                f.write("\n")

    # Remove the split PDFs
    try:
        subprocess.run(['sudo', 'rm', '-rf', 'split_pdfs/'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

    print(f'>> All OCR outputs saved to the folder: {args.output}\n')





if __name__ == "__main__":
    main()