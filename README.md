# Simple Math Operations Python Project

## Project Description
A simple Python project demonstrating basic math operations with CI/CD workflow using GitHub Actions.

## Features
- Addition of numbers
- Subtraction of numbers
- Automated testing
- Docker containerization
- CI/CD pipeline

## Prerequisites
- Python 3.9+
- Docker (optional)

## Local Setup
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Tests
```
python -m pytest test.py
```

## Docker Usage
1. Build the image:
   ```
   docker build -t math-operations .
   ```
2. Run the container:
   ```
   docker run math-operations
   ```

## CI/CD Workflow
This project uses GitHub Actions for:
- Running tests
- Building Docker image
- Pushing to Docker Hub

## License
MIT License
