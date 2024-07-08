## Developer Note:
- Should contain a container for a PostgreSQL database which connects to DataScraper and stores scraped data.
- Should also be able to connect to eAS to update dataset (would need to rerun indexing which needs GPU support).

## Setbuilder
- `database/setbuilder`
- The purpose of This object is to compress the collected data from the DataScraper directory and extract only the necessary data.
