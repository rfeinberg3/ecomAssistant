import docker
import psycopg2
import pandas as pd
from datasets import load_dataset

if __name__ == '__main__':
    
    # Load asos-e-commerce-dataset from HuggingFace
    ds = load_dataset("TrainingDataPro/asos-e-commerce-dataset")['train']

    # Convert to pandas DataFrame
    df = ds.to_pandas()

    # Remove useless columns
    df = df.drop(columns=['url', 'size', 'color', 'images', 'category'])

    # Normalize price and convert from Pound sterling to USD
    df['price'] = df['price'].replace(to_replace=r'[^\d.]', value="", regex=True) # Remove non digit and '.' chracters
    df['price'] = (df['price'].astype(float) * 1.29).round(2)

    # Connect to postgreSQL database
    conn = psycopg2.connect(database="eAssistant", host="::", password="test111")

    # Open a cursor to perform database operations
    cur = conn.cursor() 

    # Send to db
    df.to_sql()

    # Docker
    #docker.APIClient.exec_create()

    # Convert dataset to pandas DataFrame
    ##df.to_csv('./test.csv')





