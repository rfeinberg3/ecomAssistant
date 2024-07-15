# Frontend for eAS

## Retrieving Data
- The Flask app uses arguments in the GET request to configure the eAS inference input.

## Plotting Response
- Once the JSON eAS dictionary is received from the backend, use plotting methods to display a line plot similarly to how you would with matplotlib.

## Creating an HTTP Server with Node.js
- Run the server with Node.js http-server module:
```bash
npm install http-server -g
cd /Frontend
npx http-server --cors --port 8080
```
- The port must match the exposed port from the API backend.