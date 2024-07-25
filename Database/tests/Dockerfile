# syntax=docker/dockerfile:1

FROM python:3.9

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

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

# Set environment variables for database connection
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5431
ENV POSTGRES_DB=eas
ENV POSTGRES_USER=ryan1
#ENV POSTGRES_PASSWORD=

CMD ["sh", "-c", "while ! pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT; do sleep 1; done && python update.py"]
