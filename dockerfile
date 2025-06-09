# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install Flask

# Set entrypoint
CMD ["python", "app.py"]
