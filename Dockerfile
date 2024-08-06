# syntax=docker/dockerfile:1

# Load python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Clone in the ColBERT repository
RUN git clone https://github.com/stanford-futuredata/ColBERT.git

# Install dependencies
COPY Search/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy in DatabaseManger
COPY /db/dbmanager /app/ColBERT/dbmanager

# Copy Search Source Code
COPY /.env /app/ColBERT/.env
COPY /Search/server.py /app/ColBERT/server.py

ENTRYPOINT ["python", "ColBERT/server.py"]


