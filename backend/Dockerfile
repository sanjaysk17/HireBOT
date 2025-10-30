# -------------------------------------
# HireBOT Backend - FastAPI Dockerfile
# -------------------------------------

# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Install system dependencies (for PostgreSQL, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend source code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Default command to run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
