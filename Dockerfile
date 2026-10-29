# Lightweight Python base image
FROM python:alpine

# Set working directory
WORKDIR /app

# Copy application script
COPY hello.py .

# Run application
CMD ["python", "hello.py"]
