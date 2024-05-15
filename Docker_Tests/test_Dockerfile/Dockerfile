# Load image
FROM ubuntu:latest

# Set the containers working directory
WORKDIR /app 

# Copy local application into container
COPY hello.py /app 

# Install Packages upon container startup
RUN apt update
RUN apt install -y python3

# Run the application
CMD ["python3", "hello.py"]
  




