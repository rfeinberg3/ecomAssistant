# syntax=docker/dockerfile:1


# Load python image
FROM python:3.10


# Set working directory
WORKDIR /app


# Clone in the ColBERT repository
RUN git clone https://github.com/stanford-futuredata/ColBERT.git


# Install dependencies
COPY search/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


# Copy in DatabaseManger
COPY db/dbmanager /app/ColBERT/dbmanager


# Copy Search Source Code
COPY .env /app/ColBERT/.env
COPY search/server.py /app/ColBERT/server.py
COPY search/setup.py /app/ColBERT/setup.py

COPY search/start.sh /app/start.sh
RUN chmod +x /app/start.sh


# Run start.sh
ENTRYPOINT ["/bin/sh"]
CMD ["/app/start.sh"]


