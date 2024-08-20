from typing import TYPE_CHECKING
import os
import time
import psycopg2
from datasets import load_dataset

from dbmanager import DatabaseManager

if TYPE_CHECKING:
    import pandas as pd

def db_table_init(dbname: str, user: str, password: str, host: str, port: str) -> None:
    ''' Initializes the ecomassistant db and clothing table (if not initialized) 
    for population below. 
    
    ### Returns:
        True if table already existed. False if table needed to be created.
    '''
    
    # SQL file path
    abs_path = os.path.abspath('./population')
    table_file_path = abs_path + '/create-tables.sql'

    # Create DatabaseManager instance
    db_util = DatabaseManager(dbname=dbname, user=user, password=password, host=host, port=port)

    # Create database if it doesn't exist
    if not db_util.is_db():
        db_util.create_db()

    # Execute SQL file to set up tables if it doesn't exist
    if not db_util.is_table('clothing'):
        db_util.execute_sql_file(table_file_path)
        return False
    
    return True

def process_data() -> 'pd.DataFrame':
    ''' Loads the asos-e-commerce-dataset fashion dataset and process.

    ### Returns:
        df: pandas.DataFrame object containing the dataset processed for our model scheme.
    '''
    
    # Load Fashion asos-e-commerce-dataset from HuggingFace
    ds = load_dataset("TrainingDataPro/asos-e-commerce-dataset")['train']

    # Convert to pandas DataFrame
    df = ds.to_pandas()

    # Drop rows with null values
    df = df.dropna()

    # Normalize price and convert from Pound Sterling to USD
    df['price'] = df['price'].replace(to_replace=r'[^\d.]', value="", regex=True) # Remove non digit and '.' chracters
    df['price'] = (df['price'].astype(float) * 1.29).round(2)

    return df

def data_to_db(df, dbname: str, user: str, password: str, host: str, port: str) -> None:
    ''' Pushed DataFrame to the clothing table in our PostgreSQL DB. '''

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
    
    time.sleep(10)

    host = os.environ.get('POSTGRES_HOST')
    port = os.environ.get('POSTGRES_PORT')
    dbname = os.environ.get('POSTGRES_DB')
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')

    print(f"Host = {host}\nDBName = {dbname}")

    if not db_table_init(dbname, user, password, host, port):
        df = process_data()
        data_to_db(df, dbname, user, password, host, port)

    else:
        print("Data previously committed")

    




