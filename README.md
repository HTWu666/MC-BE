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
docker run -d -p <your_expose_port>:5000 <your_docker_image_name>
```

Now, you should be able to access the application by navigating to http://localhost:<your_export_port> in your web browser.

# Swagger API Documentation

This project provides Swagger documentation for easy exploration and testing of the API endpoints. Swagger is a powerful tool for visualizing and interacting with APIs.

### Accessing Swagger Documentation

To access the Swagger documentation, simply navigate to the following url in your web browser.

```
http://localhost:<your_export_port>/apidocs
```

# Unit Test Result

The project has a comprehensive suite of unit tests consisting of 24 items (Figure 1), achieving a test coverage of 99% (Figure 2).

![pytest-1](https://github.com/HTWu666/MC-BE/assets/126232123/6158f84a-0647-47fe-9646-a692bce84a05)

Figure 1

![pytest-2](https://github.com/HTWu666/MC-BE/assets/126232123/8de8fb52-5ec0-4650-957b-3b324f47f600)

Figure2
