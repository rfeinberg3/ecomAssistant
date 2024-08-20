#!/bin/bash

# Run retrieval API server
cd eAS
docker compose up retrieval &
cd ..

# Run frontend
cd Frontend
npx http-server --cors --port 8080 &
sleep 2
open http://localhost:8080

# Wait for user input before closing
read -p "Press CTRL+C to stop the server"

# Kill the server process
kill $!
