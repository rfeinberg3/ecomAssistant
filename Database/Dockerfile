# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy in source code and library
COPY /setbuilder /app/setbuilder
COPY /bin/update.py /app/update.py

# Create directory to retrieve volume dataset
RUN mkdir /volume && \
    cd /volume && \
    mkdir /sets && \
    cd /..

ENTRYPOINT ["python", "update.py"]
