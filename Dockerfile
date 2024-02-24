FROM ubuntu:latest

# Set the environment variable DEBIAN_FRONTEND to noninteractive
ARG DEBIAN_FRONTEND=noninteractive

# Set the environment variable TZ to Asia/Kolkata
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone



# Update packages and install sudo, apt-utils, and software-properties-common
RUN apt-get update && \
    apt-get install -y sudo apt-utils software-properties-common && \
    apt-get clean

# Set up sudo
RUN echo "ALL ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Set up a non-root user (optional but recommended)
# Replace <username> with your desired username
RUN useradd -ms /bin/bash admin
USER admin

# Set the working directory in the container
WORKDIR /home/admin

# Copy the Python and R scripts into the container
COPY ocr_tess.py /home/admin
COPY split_pdf.r /home/admin
COPY main.py /home/admin
COPY sample.pdf /home/admin

# Install any dependencies for Python and R
# RUN sudo apt-get update && sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
# RUN sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
# RUN echo deb https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ >> /etc/apt-get/sources.list
RUN sudo add-apt-repository ppa:c2d4u.team/c2d4u4.0+
RUN sudo apt-get update
RUN sudo apt-get install -y python3 python3-pip
RUN sudo apt-get install -y r-base r-base-dev
RUN sudo apt-get install -y r-cran-pdftools
RUN sudo apt-get install -y poppler-utils
RUN sudo apt-get install -y tesseract-ocr tesseract-ocr-ben
RUN pip3 install numpy pandas multilingual_pdf2text pytesseract

COPY Bengali.traineddata /usr/share/tesseract-ocr/4.00/tessdata/

CMD ["/bin/bash"]