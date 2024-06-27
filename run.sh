#!/bin/bash
docker compose up --build --detach
docker attach ebayautoseller-retrieval-1
docker compose down