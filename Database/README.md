# Docker Postgres Database

## Testing Setup

### Install External Libraries
- Using conda:
```bash
conda create --file requirements.txt --name db
conda activate db
```
- Using pip:
```bash
pip install -r requirements.txt
```

## Usage
- In the main directory, initialize/run the postgres db container:
```sh
docker compose up db --detach
```
- In a seperate terminal, create `eAssistant` db:
```sh
docker exec -it ebayautoseller-db-1 createdb -U postgres eAssistant
```
- Now we can connect from our local machine with postgres uri:
```sh
psql postgresql://postgres:1234@localhost:5431/eAssistant

# You should see:
psql (16.0 (Homebrew), server 15.7 (Debian 15.7-1.pgdg120+1))
Type "help" for help.

eAssistant=#
```
- Copy and paste the contents of `./bin/create-tables.sql` into the command-line to initialize the table.
- Now run `./bin/asos_data_to_db.py` to add the Fashion dataset to the db.
    - Note how variables are setup in the compose db service and the psycopg2.connect() method within `asos_data_to_db.py` respectively. It's crucial they are both setup this way to work properly.

## Setbuilder
- `./setbuilder/setbuilder.py`
- The purpose of This object is to compress collected data from any directory containing json file(s) and extract only the necessary data.
- Allows for ease of dataset collation/creation with its combine() method.
- See `./tests/test_build.py` amd its output `./tests/varied_dataset.csv` for example.


## Developer Note:
- More datasets to be added should go in seperate tables.
- Should also be able to connect to eassistant to update dataset (would need to rerun indexing which needs GPU support).

