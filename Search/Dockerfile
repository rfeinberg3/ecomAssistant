#syntax=docker/dockerfile:1

# Load python image
FROM python:3.10

RUN git clone 


# Set working directory
WORKDIR /app

# Copy in ColBERT library
COPY /ColBERT /app/ColBERT

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Expose Port
EXPOSE 5050:5050

# Run python scripts
COPY /datacollator /app/datacollator
COPY /bin /app

ENTRYPOINT ["python", "api_retrieval.py"]


