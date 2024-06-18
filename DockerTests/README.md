# Test Documentation

## Setup
- install docker: []() Mac, Linux, Windows
- Ensure the docker daemon is running

## Method
- 

1. Build the Docker image:
```docker build -t testing:v1 .```
2. Run the Docker container:
```docker run testing:v1``` 
    - Test with `docker run -it testing:v1`


## Challenges
- How to connect a driver to a docker container?


This document provides guidance on setting up Docker containers and microservices for testing purposes.

## Importance of Docker Containerization and Microservice Architecture

### Docker Containerization

Docker containerization is a lightweight virtualization method that allows developers to package applications and their dependencies into a single, portable container. These containers can run consistently across various computing environments. The importance of Docker containerization includes:

- **Consistency and Isolation**: Containers ensure that an application runs the same way regardless of where it is deployed. Each container is isolated from others, which helps avoid conflicts between dependencies.
- **Portability**: Docker containers can run on any platform that supports Docker, including local machines, on-premises servers, and cloud environments.
- **Efficiency**: Containers share the host system's kernel and resources, which makes them more efficient and faster to start than traditional virtual machines.
- **Scalability**: Docker containers can be easily scaled up or down, making it simpler to handle varying loads and improve resource utilization.

### Microservice Architecture
Microservice architecture is an architectural style that structures an application as a collection of loosely coupled services. Each service is self-contained and focuses on a specific business function. By breaking down applications into smaller, manageable services, microservices promote better organization and separation of concerns.

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


## References

### Dockerfile Tutorials

To create Docker images with Dockerfile, follow this tutorial:
- [How to Create Docker Images with Dockerfile](https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/)

For deploying microservices using Docker Compose, refer to this guide:
- [Deploying Microservices with Docker](https://www.linode.com/docs/guides/deploying-microservices-with-docker/)

For a step-by-step guide on creating Dockerfile, see:
- [Step-by-Step Guide to Create Dockerfile](https://medium.com/@anshita.bhasin/a-step-by-step-guide-to-create-dockerfile-9e3744d38d11)
