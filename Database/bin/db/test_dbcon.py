import psycopg2

if __name__ == '__main__':
    # Connect to postgreSQL database
    conn = psycopg2.connect("dbname=eas user=postgres password=test111 host=localhost port=5432")
    print("Connected successfully!")
    # Don't forget to close the connection when you're done
    conn.close()