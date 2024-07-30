# syntax=docker/dockerfile:1

# Load python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Clone in the ColBERT repository
RUN git clone https://github.com/stanford-futuredata/ColBERT.git

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Expose Port
EXPOSE 5050:5050

# Copy in index embeddings, .env, and server.py
COPY /indexes /app/indexes
COPY /.env /app/ColBERT/.env
COPY /server.py /app/ColBERT/server.py

ENTRYPOINT ["python", "ColBERT/server.py"]


