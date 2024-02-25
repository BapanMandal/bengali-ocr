# Bengali OCR using Tesseract
Install [docker](https://docs.docker.com/get-docker/#supported-platforms) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for your platform. Then follow the instructions below to run the OCR.

## Clone the repository
You can clone the repository on your system using the following command. The second line of the command will change the current directory to the cloned repository.
```bash
git clone https://github.com/BapanMandal/bengali-ocr && \
cd bengali-ocr
```

## Running the Docker container
> NOTE: The current directory (where you cloned the bengali-ocr repository) needs to be mounted inside the container at /home/admin (the default home directory of the container).
> This allows you to access (both read and write) the files in the current directory from inside the container. The following commands achieve this.

Platform | Command
--- | ---
Linux|`sudo docker run -it -v "$(pwd)":/home/admin bapan/ocr:latest`
Windows|`docker run -it -v ${PWD}:/home/admin bapan/ocr:latest`
MacOS|`docker run -it -v $(pwd):/home/admin bapan/ocr:latest`

If running for the first time, it will automatically fetch the required image from Docker Hub. Then it will start the container and you will be inside the container's terminal. You are now ready to run the OCR commands.
