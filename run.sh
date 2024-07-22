#!/bin/bash
cd eAS
docker build -t eas:v1 .
docker run -it eas:v1
docker stop eas:v1
docker rm eas:v1