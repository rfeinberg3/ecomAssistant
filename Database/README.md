## Developer Note:
- Should contain a container for a postgreSQL database which connects to DataScraper and stores scraped data.
- Should also be able to connect to eAS to update dataset (would need to rerun indexing which needs GPU support).

## DatasetBuilder
- `database/setbuilder`
- This objects purpose is compress the collected data from the DataScraper directory, and extract only necessary data.
