# Dockerized Python Project

## Overview

This project uses Docker to containerize a Python application. The `Dockerfile` provided outlines the necessary steps to build and run the Docker image, including installing dependencies and configuring the application.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) must be installed on your machine.

## Build the Docker Image

To build the Docker image, follow these steps:

1. Open a terminal and navigate to the root directory of your project, where the `Dockerfile` is located.

2. Run the following command to build the Docker image:

```sh
   docker build -t my-python-app .
```
- my-python-app is the tag for your Docker image. You can choose a different name if you prefer.

## Run the Docker Container

Once the image is built, you can run a container from it:

1. Execute the following command to start the container:
   ```sh
     docker run -d --name my-running-app my-python-app
   ```
   - -d runs the container in detached mode.
   - --name my-running-app gives the container a name. You can choose a different name if desired.
   - my-python-app is the name of the image you built.
2. If your application exposes a port, map the container’s port to your host machine’s port. For example, to map port 8000 in the container to port 8000 on your host, use:
   ```sh
      docker run -d -p 8000:8000 --name my-running-app my-python-app
   ```
   Replace 8000 with the port number used by your application.

## Stop and Remove the Container
To manage the container:
1. To stop the running container, use:
   ```sh
    docker stop my-running-app
   ```
2. To remove the stopped container, use:
   ```sh
    docker rm my-running-app
   ```

## Dockerfile Explanation

Here is a brief explanation of the Dockerfile:

- FROM python:3: Uses the official Python 3 image as the base for the Docker image.
- WORKDIR /usr/src/app: Sets the working directory inside the container to /usr/src/app.
- COPY requirements.txt ./: Copies the requirements.txt file from your local machine into the working directory in the container.
- RUN pip install --no-cache-dir -r requirements.txt: Installs the Python dependencies listed in requirements.txt without caching.
- COPY . .: Copies the rest of your application files into the working directory in the container.
- CMD [ "python", "./your-daemon-or-script.py" ]: Defines the command to run your Python script or application.

## Troubleshooting

- 401 Unauthorized Error:

  - Solution: Ensure you are logged into Docker with appropriate permissions. Re-login with docker login if needed.
  
- Container Not Running:

  - Solution: Check the container logs for errors using docker logs my-running-app and resolve any issues.

For more information on Docker, refer to the [official Docker documentation](https://docs.docker.com).
