# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Git - for cloning the repository.
- Docker - for building and running the Docker container.

## Installation

Follow these simple steps to get your development environment running:

### 1. Clone the repository

First, clone the project repository to your local machine using Git. Open a terminal and run the following command:

```
git clone https://github.com/HTWu666/MC-BE.git
```

### 2. Build the Docker image

Navigate to the project directory where the Dockerfile is located and build the Docker image using the following command:

```
docker build -t <docker_image_name> .
```

### 3. Run the Docker container

After building the image, run the container in detached mode with port forwarding. This allows you to access the application via the specified port on your local machine. Use the command:

```
docker run -d -p <your-expose-port>:5000 <your-docker-image-name>
```

Now, you should be able to access the application by navigating to http://localhost:your-expose-port in your web browser.
