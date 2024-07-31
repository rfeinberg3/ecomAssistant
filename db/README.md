# Docker Postgres Database

## Introduction
This directory is meant for setting up and populating tables in a PostgreSQL database using Docker, primarily for storing and managing ecommerce datasets. It includes tools for data manipulation and integration with the AI ecomAssistant.

## Prerequisites
- Docker
- Python 3.x

## Usage

### Starting the Database
- Initialize and run the Postgres DB container:
```bash
docker compose up db --detach
```

### Populating the Database
```bash
docker compose up populator --build
```