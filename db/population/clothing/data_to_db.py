import os
import psycopg2
from datasets import load_dataset

from dbmanager import DatabaseManager


def db_table_init(dbname: str, user: str, password: str, host: str, port: str) -> None:
    ''' Initializes the ecomassistant db and clothing table (if not initialized) 
    for population below. '''
    
    # SQL file path
    abs_path = os.path.abspath('./population')
    table_file_path = abs_path + '/create-tables.sql'

    # Create DatabaseManager instance
    db_util = DatabaseManager(dbname, user, password, host, port)

    # Create database if it doesn't exist
    if not db_util.is_db():
        db_util.create_db()

    # Execute SQL file to set up tables if it doesn't exist
    if not db_util.is_table('clothing'):
        db_util.execute_sql_file(table_file_path)
        return False
    
    return True

def data_to_db(dbname: str, user: str, password: str, host: str, port: str) -> None:
    ''' Loads the asos-e-commerce-dataset fashion dataset and pushed to the 
    clothing table in our PostgreSQL DB.
    '''
    
    # Load Fashion asos-e-commerce-dataset from HuggingFace
    ds = load_dataset("TrainingDataPro/asos-e-commerce-dataset")['train']

    # Convert to pandas DataFrame
    df = ds.to_pandas()

    # Normalize price and convert from Pound Sterling to USD
    df['price'] = df['price'].replace(to_replace=r'[^\d.]', value="", regex=True) # Remove non digit and '.' chracters
    df['price'] = (df['price'].astype(float) * 1.29).round(2)

    # Connect to postgreSQL database
    conn = psycopg2.connect(dbname=dbname, host=host, port=port, user=user, password=password)
    cur = conn.cursor()

    # Send data to postgreSQL database
    for index, row in df.iterrows():
        sku = row['sku']
        name = row['name']
        price = row['price']
        description = row['description']  # Truncate description to max 10,000 characters
        # Execute the INSERT statement
        cur.execute("""
            INSERT INTO clothing (sku, name, price, description)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (sku) DO NOTHING
        """, (sku, name, price, description))

    conn.commit()
    print("asos Data Committed")

    # Close db connection
    cur.close()
    conn.close()

if __name__ == '__main__':

    host = os.environ.get('POSTGRES_HOST')
    port = os.environ.get('POSTGRES_PORT')
    dbname = os.environ.get('POSTGRES_DB')
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')

    db_table_init(dbname, user, password, host, port)
    data_to_db(dbname, user, password, host, port)

    




