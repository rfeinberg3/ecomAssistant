# Test Documentation

This document provides guidance on setting up Docker containers and microservices for testing purposes.

## References

### Dockerfile Tutorials

To create Docker images with Dockerfile, follow this tutorial:
- [How to Create Docker Images with Dockerfile](https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/)

For deploying microservices using Docker Compose, refer to this guide:
- [Deploying Microservices with Docker](https://www.linode.com/docs/guides/deploying-microservices-with-docker/)

For a step-by-step guide on creating Dockerfile, see:
- [Step-by-Step Guide to Create Dockerfile](https://medium.com/@anshita.bhasin/a-step-by-step-guide-to-create-dockerfile-9e3744d38d11)

## Sample Containerized Program (w/ Dockerfile)

Navigate to the `Sample_Dockerfile` folder to see a simple Dockerfile example which containerizes and runs the program `hello.py`.

To run the Dockerfile:

1. Navigate to the `Sample_Dockerfile` folder.
2. Build the Docker image:
```docker build -t testing:v1 .```
3. Run the Docker container:
```docker run testing:v1```

## Sample Microservice Architecture (w/ Docker Compose)
This test example utilizes a microservices architecture with two services: `hello.py` and `goodbye.py`.
Navigate to the `Sample_Compose` folder to see the Dockerfiles that make up these two services. You'll also notice a file called `docker-compose.yml`, this file is responsible for running all the microservices and ensuring they execute properly.

To run the microservice program:
1. Build the services: `docker-compose build`
2. Start the services: `docker-compose up`

What you should see:

![image](https://github.com/rfeinberg3/ebay_Auto_Seller/assets/95943957/3b738fe0-4cb5-42f3-9bd3-cb191850d56f)
