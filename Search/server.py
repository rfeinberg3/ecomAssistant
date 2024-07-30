from flask import Flask, request
from flask_cors import CORS
from functools import lru_cache
import os
from dotenv import load_dotenv

from colbert import Searcher

from dbmanager import DatabaseManager

# Load environment variables
load_dotenv()

INDEX_NAME = os.getenv("INDEX_NAME")
INDEX_ROOT = os.getenv("INDEX_ROOT")

HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DBNAME = os.getenv("POSTGRES_DB")
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")

# Set Flask App
app = Flask(__name__)
CORS(app)

# Collect data from db and convert to pandas.DataFrame()
dbm = DatabaseManager(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
df = dbm.table_to_pandas("clothing")
#TODO: Add list of table names to .env and loop through them here. Possible create combine() method to combine datasets.

# Factor data points to collection
title = df['name']
prices = df['price']
collection = df['description']
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
    print(prices[results[0][0]])
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