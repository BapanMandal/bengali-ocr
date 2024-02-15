from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
import logging
logging.basicConfig(level=logging.INFO)

def main():
    # create document for extraction with configurations
    pdf_document = Document(
        document_path='C:\\CODING\\Bangla_OCR\\Test.pdf',
        language='Bengali'
        )
    pdf2text = PDF2Text(document=pdf_document)
    content = pdf2text.extract()
    # get size of content
    print(len(content))
    with open("file.txt", "w", encoding="utf-8") as f:
        for i in range(len(content)):
            f.write(content[i]['text'])
            f.write("\n")

if __name__ == "__main__":
    main()