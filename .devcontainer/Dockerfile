# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Install system dependencies (including Git)
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*
# 3. Set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files to disk
# PYTHONUNBUFFERED: Ensures logs are sent straight to terminal without buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# 4. Set the working directory
WORKDIR /app

# 5. Create virtual environment and upgrade pip
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir --upgrade pip

# 6. Copy and install dependencies
# Doing this before copying the app code takes advantage of Docker's layer caching
COPY requirements.txt .
# Install your app deps + the linting tools
RUN pip install --no-cache-dir -r requirements.txt black flake8 pylint
# 7. Copy the rest of your application code
COPY ./app ./app

# 8. Command to run your app
CMD ["sleep", "infinity"]