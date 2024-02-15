# Use an existing Docker image as a base
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the Python and R scripts into the container
COPY ocr_tess.py /app
COPY split_pdf.r /app

# Install any dependencies for Python and R
# RUN sudo apt-get update && sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
# RUN sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
RUN apt-get update
RUN apt-get install -y r-base
RUN apt-get install -y poppler-utils
RUN apt-get install -y tesseract-ocr tesseract-ocr-ben
RUN pip install numpy pandas multilingual_pdf2text pytesseract

# # Command to run the Python script
# CMD ["python", "ocr_tess.py"]