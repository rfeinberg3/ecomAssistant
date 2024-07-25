# Docker Postgres Database

## Introduction
This project sets up a PostgreSQL database using Docker, primarily for storing and managing fashion datasets. It includes tools for data manipulation and integration with an AI assistant.

## Setbuilder
The Setbuilder tool (`./setbuilder/setbuilder.py`) is designed to compress and extract necessary data from JSON files. It facilitates easy dataset creation and combination.

## Testing Setup

### Prerequisites
- Docker
- Python 3.x
- (Optional) Conda for environment management

### Installation

Install required Python libraries:
   
- Using conda:
```bash
conda create --file requirements.txt --name db
conda activate db
```

- OR using pip:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Database
- Initialize and run the Postgres DB container:
```bash
docker compose up db --detach
```

### Connecting to the Database
- Create the `eAssistant` database:
```bash
docker exec -it ebayautoseller-db-1 createdb -U postgres eAssistant
```

- Connect to the database from your local machine:
```bash
psql postgresql://postgres:1234@localhost:5431/eAssistant
```

You should see a prompt like this:
```bash
psql (16.0 (Homebrew), server 15.7 (Debian 15.7-1.pgdg120+1))
Type "help" for help.

eAssistant=#
```

### Initializing Tables
- Copy and paste the contents of `./bin/create-tables.sql` into the psql command-line to initialize the table.

### Adding Data
- Run the script to add the Fashion dataset to the database:
```bash
python ./bin/asos_data_to_db.py
```

Note: Ensure that the variables in the Docker Compose db service and the `psycopg2.connect()` method in `asos_data_to_db.py` are correctly set up.

### Usage Example
See `./tests/test_build.py` and its output `./tests/varied_dataset.csv` for an example of how to use Setbuilder.

## Developer Notes
- When adding new datasets, create separate tables for each.
- To update the dataset for the eAssistant, you'll need to rerun indexing (requires GPU support).