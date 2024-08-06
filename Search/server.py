import pandas as pd
from flask import Flask, request
from flask_cors import CORS
from functools import lru_cache
import os
from dotenv import load_dotenv

from colbert import Searcher


# Load environment variables
load_dotenv()

INDEX_NAME = os.getenv("INDEX_NAME")
INDEX_ROOT = os.getenv("INDEX_ROOT")
DATA = os.getenv("DATA")


# Set Flask App
app = Flask(__name__)
CORS(app)


# Load and factor data points to title, price, and collection
df = pd.read_json(DATA, typ='frame')
title = df['name'].to_list()
prices = df['price'].to_list()
collection = df['description'].to_list()
print("\nLength of collection =", len(prices), '\n')


# Set Search object
searcher = Searcher(index=INDEX_NAME, index_root=INDEX_ROOT, collection=collection)
counter = {"api" : 0}


# For cleaning Search output
def clean_text(text):
    return text.replace('[', '').replace(']', '').replace('{', '\n\n').replace('}', '').replace('\'', '')[2:]


# Main Function
@lru_cache(maxsize=1000000)
def api_search_query(query, k):
    print(f"Query={query}")
     # Find the top-3 passages for this query
    results = searcher.search(query, k=int(k))
    # Get average price from top 3 results
    topk = dict()
    topk['itemDescription'] = clean_text(collection[results[0][0]])
    print(prices[results[0][0]])
    topk['price'] = prices[results[0][0]] # (float(prices[results[0][0]][0])+float(prices[results[0][1]][0])+float(prices[results[0][2]][0])/3)
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