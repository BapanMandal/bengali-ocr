# Bengali OCR using Tesseract
Install [docker](https://docs.docker.com/get-docker/#supported-platforms) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for your platform, if they're not already. Then follow the instructions below to run the OCR.

## Clone the repository
Clone the repository on your system by running the following command in your terminal application.
```bash
git clone https://github.com/BapanMandal/bengali-ocr
```
Now change the current directory to the cloned repository.
```bash
cd bengali-ocr
```

## Running the Docker container
> NOTE: The current directory (where you cloned the bengali-ocr repository) needs to be mounted inside the container at /home/admin (the default home directory of the container).
> This allows you to access (both read and write) the files in the current directory from inside the container. The following commands achieve this.

Platform | Command
--- | ---
Linux | `sudo docker run -it -v "$(pwd)":/home/admin bapan/ocr:latest`
Windows | `docker run -it -v ${PWD}:/home/admin bapan/ocr:latest`
MacOS | `docker run -it -v $(pwd):/home/admin bapan/ocr:latest`

If running for the first time, it will automatically download the required image from Docker Hub. Then it will start the container and you will be inside the container's terminal.
> NOTE: at least 2GB of free space is required on your system for the image to be downloaded.

## Inside the Container's Terminal
The container's terminal looks like this:
```bash
admin@<container-id>:~$
```
This container is a minimal Ubuntu 22.04 environment with all the required dependencies installed. So you can run all the generic Linux commands inside it.

### Usage of the OCR script
The `main.py` script present in the repository is the required script to run the OCR. To see the usage of the script, run the following command:
```bash
python3 main.py --help
```
It will show the usage of the script, like this:
```bash
usage: main.py [-h] [-o OUTPUT] input

Converts Bengali PDFs to Text using Tesseract OCR

positional arguments:
  input                 Path to the input PDF file

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name of the output folder where OCR outputs will be saved. (Default: "ocr_outputs")
```

### Running the OCR on a Sample PDF
There are a couple of sample PDFs in the `sample_pdfs` directory of the repository. You can use them to test the OCR. To run the OCR on a sample PDF, run the following command (it may take a few minutes to complete for large PDFs):
```bash
python3 main.py sample_pdfs/<pdf-file-name>.pdf
```
By default, the OCR outputs will be saved in a folder named `ocr_outputs` in the current directory. You can change the output folder name by using the `-o` or `--output` option. For example:
```bash
python3 main.py sample_pdfs/<pdf-file-name>.pdf -o my_outputs
```
This will save the OCR outputs in a folder named `my_outputs` inside the current directory.
> NOTE: Before each run, the `ocr_outputs` folder is cleared to avoid any confusion with previous outputs. So, if you want to keep the previous outputs, you should move them to another directory before running the OCR again. Alternatively, you can change the output folder for the current run using the `-o` or `--output` option.

> NOTE: The output text is also split over multiple page ranges to avoid large text files, which can be difficult to handle.

You can also add your own PDFs to the `sample_pdfs` directory and run the OCR on them using the same command.


### Exiting the Container
To exit the container's terminal, run the following command:
```bash
exit
```
This will stop the container and you will be back in your system's terminal. The 

### Accessing the OCR Outputs
The OCR outputs (text files) are permanently saved in the output folder you specified, even if you exit the container. You can easily access them from your system's file manager inside the directory where you cloned the repository.