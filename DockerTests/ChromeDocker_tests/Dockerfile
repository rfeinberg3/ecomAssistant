# Get the latest ubuntu image
FROM ubuntu:latest

# Set the containers working directory
WORKDIR /app

# Copy the scripts into the working directory
COPY python ./src



# Install packages with apt and python3
RUN apt update && \
    apt install -y python3-pip && \
    apt install -y python3-pytest && \
    apt install -y python3-selenium && \
    apt install -y python3-requests	