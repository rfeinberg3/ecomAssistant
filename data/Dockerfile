# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy in source code and libraries
COPY /dbmanager /app/dbmanager
COPY /population /app/population
