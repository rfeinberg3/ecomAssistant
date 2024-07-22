# Database

## Usage
To run in docker environment, assuming the volume has been created and DataScraper container has run for a reasonable amount of time. (Quick run all containers with the global `compose.yaml` file to obtain the volume. See main README for how to do that.)

- Open a terminal in this directory, and run the following commands.
```sh
docker build -t database:v1 .
docker run -v ebayautoseller_vol-input-data:/app/volume database:v1
```
- This will automatically send all new data collected from the DataScraper to our postgreSQL database.


## Developer Note:
- Should contain a container for a PostgreSQL database which connects to DataScraper and stores scraped data.
- Should also be able to connect to eAS to update dataset (would need to rerun indexing which needs GPU support).

## Setbuilder
- `database/setbuilder`
- The purpose of This object is to compress the collected data from the DataScraper directory and extract only the necessary data.
