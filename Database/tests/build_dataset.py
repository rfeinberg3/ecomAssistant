import psycopg2

if __name__ == '__main__':
    # Connect to postgreSQL database
    conn = psycopg2.connect("dbname=eas user=ryan1 password=test111 host=localhost port=5432")

    # Open a cursor to perform database operations
    cur = conn.cursor()
    
    # Get up-to-date data from database
    #cur.execute("SELECT * FROM eas;")
    #list_of_items = cur.fetchall()
    #print(len(list_of_items))