#syntax=docker/dockerfile:1

# Load python image
FROM python:3.9

# Set working directory
WORKDIR /app

# clone or update colbert with git
COPY . /app
RUN chmod +x /app/Load_ColBERT.sh
RUN /app/Load_ColBERT.sh

# Create directory to store volume dataset
RUN mkdir /output

# Install dependencies
RUN pip install -r requirements.txt

# Run python script
ENTRYPOINT ["python", "retrieval.py"]


