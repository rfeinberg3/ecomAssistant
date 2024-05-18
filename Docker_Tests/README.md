# Test Documentation

This document provides guidance on setting up Docker containers and microservices for testing purposes.

## References

### Dockerfile Tutorial

To create Docker images with Dockerfile, follow this tutorial:
- [How to Create Docker Images with Dockerfile](https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/)

For deploying microservices using Docker Compose, refer to this guide:
- [Deploying Microservices with Docker](https://www.linode.com/docs/guides/deploying-microservices-with-docker/)

For a step-by-step guide on creating Dockerfile, see:
- [Step-by-Step Guide to Create Dockerfile](https://medium.com/@anshita.bhasin/a-step-by-step-guide-to-create-dockerfile-9e3744d38d11)

## Sample Dockerfile

Navigate to the `Sample_Dockerfile` folder to see a simple Dockerfile example which containerizes and runs the program `hello.py`.

To run the Dockerfile:

1. Navigate to `Sample_Dockerfile`.
2. Build the Docker image:
```docker build -t testing:v1 .
3. Run the Docker container:

docker run testing:v1


