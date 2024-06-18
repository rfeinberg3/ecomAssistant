# Get the latest ubuntu image
FROM ubuntu:latest

# Set the containers working directory
WORKDIR /app

# Copy the scripts into the working directory
COPY src ./src

# Install packages with apt and python3
RUN apt update && \
    #apt install -y wget && \
    #apt install -y tar && \
    apt install -y python3-pip && \
    #apt install -y firefox && \
    apt install -y python3-selenium && \
    apt install -y python3-requests	
   

# Download and extract Driver
#RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux-#aarch64.tar.gz && \
  #  tar -xvf geckodriver-v0.34.0-linux-aarch64.tar.gz && \
    #rm geckodriver-v0.34.0-linux-aarch64.tar.gz && \
   # mv geckodriver /usr/local/bin/geckodriver && \
    #chmod +x /usr/local/bin/geckodriver && \
   # export PATH=$PATH:/usr/local/bin/

# Run the script
#CMD 