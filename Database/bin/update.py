import os, sys
sys.path.append('../setbuilder')

import psycopg2
from setbuilder import Setbuilder


if __name__ == '__main__':
    # Data Input dir from DastaScaper otuput
    os.path.join('volume/outputs')
    data_dir = 'volume/outputs'

    # Build dataset from raw scraped item data
    list_of_dicts = Setbuilder(data_dir).combine(['itemId', 'title', 'price', 'condition', 'itemDescription'])

    # Connect to postgreSQL database
    conn = psycopg2.connect("dbname=rfeinberg user=ryan password=test111")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Send data to postgreSQL database (update)
    for query in list_of_dicts:
        itemID = query['itemId']
        title = query['title']
        value = query['price'][0]
        condition = query['condition']
        itemDescription = query['itemDescription'][0:10000] # Truncate desription to max 10,000 characters to fit in database
        cur.execute(
            " INSERT INTO eAS (itemID, title, price, condition, itemDescription) "
            " VALUES (%s, %s, %s, %s, %s) "
            " ON CONFLICT (itemID) DO NOTHING ", # Ensures items with the same itemID aren't added multiple times or overwritten
            (itemID, title, value, condition, itemDescription)
        )
    conn.commit()

    ###############################
    # close cursor and database connection
    cur.close()
    conn.close()