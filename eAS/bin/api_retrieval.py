from flask import Flask, render_template, request
from flask_cors import CORS
from functools import lru_cache
import math

from ColBERT.colbert.infra import Run, RunConfig, ColBERTConfig
from ColBERT.colbert import Searcher
#from datacollator import DataCollator

# Set Flask App
app = Flask(__name__)
CORS(app)

# Set Indexer data path
index_name = "collection.kmeans_4iters.2bits"

# Set Searcher
with Run().context(RunConfig()):
        searcher = Searcher(index=index_name) #collection=collection !! Add this parameter most likely!!

# Set api call counter
counter = {"api" : 0}

# Main Function
@lru_cache(maxsize=1000000)
def api_search_query(query, k):
    print(f"Query={query}")
    if k == None: k = 10
    k = min(int(k), 100)
    pids, ranks, scores = searcher.search(query, k=100)
    pids, ranks, scores = pids[:k], ranks[:k], scores[:k]
    passages = [searcher.collection[pid] for pid in pids]
    probs = [math.exp(score) for score in scores]
    probs = [prob / sum(probs) for prob in probs]
    topk = []
    for pid, rank, score, prob in zip(pids, ranks, scores, probs):
        text = searcher.collection[pid]            
        d = {'text': text, 'pid': pid, 'rank': rank, 'score': score, 'prob': prob}
        topk.append(d)
    topk = list(sorted(topk, key=lambda p: (-1 * p['score'], p['pid'])))
    return {"query" : query, "topk": topk}

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