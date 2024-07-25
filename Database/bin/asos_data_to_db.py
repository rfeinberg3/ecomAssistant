import psycopg2
from datasets import load_dataset

if __name__ == '__main__':
    
    # Load Fashion asos-e-commerce-dataset from HuggingFace
    ds = load_dataset("TrainingDataPro/asos-e-commerce-dataset")['train']

    # Convert to pandas DataFrame
    df = ds.to_pandas()

    # Remove useless columns
    df = df.drop(columns=['url', 'size', 'color', 'images', 'category'])

    # Normalize price and convert from Pound sterling to USD
    df['price'] = df['price'].replace(to_replace=r'[^\d.]', value="", regex=True) # Remove non digit and '.' chracters
    df['price'] = (df['price'].astype(float) * 1.29).round(2)

    # Connect to postgreSQL database
    conn = psycopg2.connect(dbname='eAssistant', host='localhost', port='5431', user='postgres', password='1234')
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

    # Close db connection
    cur.close()
    conn.close()



