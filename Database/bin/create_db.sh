#!/bin/bash

docker compose up db --detach
docker exec -it ebayautoseller-db-1 createdb -U postgres eas

# Connect to db
## docker exec -it ebayautoseller-db-1 psql -U postgres eas