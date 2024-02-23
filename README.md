# Getting Started

This project is designed to provide CRUD (Create, Read, Update, Delete) operations for tasks.
These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Git - for cloning the repository.
- Docker - for building and running the Docker container.

## Installation

Follow these simple steps to get your development environment running:

### 1. Clone the repository

First, clone the project repository to your local machine using Git. Open a terminal and run the following command:

```
git clone https://github.com/HTWu666/MC-BE.git <new_folder_name>
```

### 2. Build the Docker image

Navigate to the project directory where the Dockerfile is located and build the Docker image using the following command:

```
cd <new_folder_name>
docker build -t <docker_image_name> .
```

### 3. Run the Docker container

After building the image, run the container in detached mode with port forwarding. This allows you to access the application via the specified port on your local machine. Use the command:

```
docker run -d -p <your_expose_port>:5000 <your_docker_image_name>
```

Now, you should be able to access the application by navigating to http://localhost:<your_expose_port> in your web browser.

# Swagger API Documentation

This project provides Swagger documentation for easy exploration and testing of the API endpoints.

### Accessing Swagger Documentation

To access the Swagger documentation, simply navigate to the following url in your web browser.

```
http://localhost:<your_expose_port>/apidocs
```

## Demo

https://github.com/HTWu666/MC-BE/assets/126232123/f9f91e71-0177-4f9c-8aa3-ec21b2cb70d5

# Unit Test Result

To run the unit tests and review the test coverage, you will need to install pytest and coverage. These tools help in executing the tests and generating detailed reports on the code coverage.

## Prerequisites

Before running the tests, make sure you have pytest and coverage installed. If not, you can install them using pip:

```
pip install pytest coverage
```

## Running the Tests

Once the prerequisites are installed, you can execute the unit tests and generate a coverage report by using the following commands:

```
coverage run -m pytest
```

This command runs all the unit tests in the project. After executing the tests, you can generate a coverage report to see detailed information on the test coverage, including which lines of code are not covered by tests:

```
coverage report --show-missing
```

https://github.com/HTWu666/MC-BE/assets/126232123/c24abd00-395f-49b8-9e72-63a24ada0574

## Test Results

Our project's unit test suite consists of 24 tests (Figure 1), achieving an impressive test coverage of 99% (Figure 2). These results underscore our commitment to code quality and reliability.

![pytest-1](https://github.com/HTWu666/MC-BE/assets/126232123/6158f84a-0647-47fe-9646-a692bce84a05)

Figure 1: Unit Test Execution Results

![pytest-2](https://github.com/HTWu666/MC-BE/assets/126232123/8de8fb52-5ec0-4650-957b-3b324f47f600)

Figure 2: Test Coverage Report
