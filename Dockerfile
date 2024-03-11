# Use the official lightweight Python image with Python 3.10
FROM python:3.10.0-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Install a virtual environment in the container and upgrade pip
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip

# Prepend virtual environment binaries to PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Command to run app
CMD ["python", "app.py"]
