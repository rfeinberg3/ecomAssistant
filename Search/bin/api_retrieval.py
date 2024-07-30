#import os, sys
#sys.path.append('..')

from flask import Flask, request
from flask_cors import CORS
from functools import lru_cache
import math

from ColBERT.colbert.infra import Run, RunConfig, ColBERTConfig
from ColBERT.colbert import Searcher
from datacollator import DataCollator

# Set Indexer data path
index_name = "collection.kmeans_4iters.2bits"

# Get dataset points and factor for Search
dataset = DataCollator('volume/sets/dataset.json')
title = dataset.get_queries()
prices = dataset.get_price()
collection = dataset.get_collection()
print("\nLength of collection =", len(prices), '\n')

# Set Searcher
with Run().context(RunConfig()):
        searcher = Searcher(index=index_name, collection=collection)

# Set Flask App
app = Flask(__name__)
CORS(app)


# Set api call counter
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