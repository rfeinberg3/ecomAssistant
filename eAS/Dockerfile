#syntax=docker/dockerfile:1

# Load python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy in ColBERT library
COPY ColBERT /app/ColBERT

# Create directory to retrieve volume dataset
RUN mkdir /outputs

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Expose Port
EXPOSE 5050:5050

# Run python script
COPY /bin /app
COPY /experiments /app/experiments
ENTRYPOINT ["python", "api_retrieval.py"]


