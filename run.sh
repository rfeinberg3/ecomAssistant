#!/bin/bash
docker compose up --build --detach
docker attach ebay_auto_seller-retrieval-1
docker compose down