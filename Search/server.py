from flask import Flask, request
from flask_cors import CORS
from functools import lru_cache
import os
from dotenv import load_dotenv

#from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Searcher

import pandas
import psycopg2
from psycopg2.extras import RealDictCursor

load_dotenv()

INDEX_NAME = os.getenv("INDEX_NAME")
INDEX_ROOT = os.getenv("INDEX_ROOT")

# Set Flask App
app = Flask(__name__)
CORS(app)

# Collect data from db and convert to pandas.DataFrame()
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT'),
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )

def table_to_json(table_name, output_file):
    conn = get_db_connection()
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        
        # Convert rows to a list of dictionaries
        data = [dict(row) for row in rows]
        data = pandas.DataFrame(data)
        conn.close()
    return data

table_name = "clothing"
output_file = f"{table_name}_data.json"
dataset = table_to_json(table_name, output_file)

# Factor data points to collection
title = dataset['name']
prices = dataset['price']
collection = dataset['description']
print("\nLength of collection =", len(prices), '\n')

# Set Search object
searcher = Searcher(index=INDEX_NAME, index_root=INDEX_ROOT)
counter = {"api" : 0}

# Main Function
@lru_cache(maxsize=1000000)
def api_search_query(query, k):
    print(f"Query={query}")
     # Find the top-3 passages for this query
    results = searcher.search(query, k=int(k))
    # Get average price from top 3 results
    topk = dict()
    topk['itemDescription'] = collection[results[0][0]]
    print(prices[results[0][0]][0])
    topk['price'] = (float(prices[results[0][0]][0])+float(prices[results[0][1]][0])+float(prices[results[0][2]][0])/3)
    return topk


# API Call Function
@app.route("/api/search", methods=["GET"])
def api_search():
    if request.method == "GET":
        counter["api"] += 1
        print("API request count:", counter["api"])
        return api_search_query(request.args.get("query"), request.args.get("k"))
    else:
        return ('', 405)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5050, debug=True)