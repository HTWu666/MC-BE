# Base image with Python 3.10 Alpine
FROM python:3.10.0-alpine

# Set working directory
WORKDIR /app

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Use non-root user
USER appuser

# Update PATH for user-level binaries
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Upgrade pip and verify version
RUN pip install --upgrade pip --user && pip --version

# Copy and own requirements.txt
COPY --chown=appuser:appgroup requirements.txt /app/

# Install dependencies
RUN pip install --user -r requirements.txt

# Copy app files and change ownership
COPY --chown=appuser:appgroup . /app/

# Expose port 5000
EXPOSE 5000

# Command to run app
CMD ["python3", "app.py"]
