from flask import Flask, request
from flask_cors import CORS
from functools import lru_cache
import os
from dotenv import load_dotenv

import torch
from huggingface_hub import hf_hub_download

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
#TODO: Add list of table names to .env and loop through them here. Possibly create combine() method to combine datasets.

# Factor data points to title, price, and collection
title = df['name'].to_list()
prices = df['price'].to_list()
collection = df['description'].to_list()
print("\nLength of collection =", len(prices), '\n')


# Load Index Embeddings and config files from Hugging Face for Search use
pt_filenames = ["0.codes.pt", "0.residuals.pt", "1.codes.pt", "1.residuals.pt", "avg_residual.pt", "buckets.pt", "centroids.pt", "ivf.pid.pt"]
json_filenames = ["0.metadata.json", "1.metadata.json", "doclens.0.json", "doclens.1.json", "metadata.json", "plan.json"]

def load_pt_files(dir: str) -> None:
  ''' Loads pt index files from Hugging Face and saves them to disk. '''
  os.makedirs(dir, exist_ok=True)

  for filename in pt_filenames:
    file_path = hf_hub_download(repo_id="ryfye181/clothing_embeddings", filename=filename)

    with open(file_path, "rb") as pt:
      embedding = torch.load(pt, map_location=torch.device('cpu'))
    with open(dir + '/' + filename, "wb") as pt:
      torch.save(embedding, pt)

def load_json_files(dir: str) -> None:
  ''' Loads json index files from Hugging Face and saves them to disk. '''
  os.makedirs(dir, exist_ok=True)

  for filename in json_filenames:
    file_path = hf_hub_download(repo_id="ryfye181/clothing_embeddings", filename=filename)
        
    with open(file_path, "r") as json:
      data = json.read()
    with open(dir + '/' + filename, "w") as json:
      json.write(data)

load_pt_files('index/clothing.kmeans_4iters.2bits')
load_json_files('index/clothing.kmeans_4iters.2bits')


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