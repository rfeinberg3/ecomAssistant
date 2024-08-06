import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import lru_cache
import os
from dotenv import load_dotenv
from colbert import Searcher
#from transformers import GPT2LMHeadModel, GPT2Tokenizer


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
counter = {"api": 0}


# Load gpt2 pre-trained model and tokenizer
'''
model_name = "gpt2-large"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
'''

# For cleaning Search output
def clean_text(text):
    return text.replace('[', '').replace(']', '').replace('{', '\n\n').replace('}', '').replace('\'', '')[2:]


# Search Function
@lru_cache(maxsize=1000000)
def api_search_query(query, k):
    print(f"Query={query}")
    # Find the top-k passages for this query
    results = searcher.search(query, k=int(k))
    # Get information for top result
    topk = dict()
    topk['itemDescription'] = clean_text(collection[results[0][0]])
    topk['price'] = prices[results[0][0]]
    return topk


# Generation Function
@DeprecationWarning
def generate_product_description(prompt, max_length=800):
    
    # Encode the input prompt
    inputs = tokenizer.encode_plus(prompt, return_tensors="pt")
    input_ids = inputs['input_ids']

    # Generate text
    output = model.generate(
      input_ids,
      max_length=max_length,
      num_return_sequences=1,
      no_repeat_ngram_size=2,
      do_sample=True,
      temperature=0.7,
    )

    full_text = tokenizer.decode(output[0])

    # Extract only the generated extension
    generated_text = full_text[len(prompt):].strip()
    return generated_text


# API Call Function
@app.route("/api/search", methods=["GET"])
def api_search():
    if request.method == "GET":
        counter["api"] += 1
        print("API request count:", counter["api"])
        query = request.args.get("query")
        k = request.args.get("k", default=1, type=int)
        
        # Perform search
        search_result = api_search_query(query, k)
        
        # Generate description
        '''
        prompt = f"Product: {query} {search_result['itemDescription']}{search_result['itemDescription']}\n\nSelling Points:"
        generated_description = generate_product_description(prompt)
        

        # Combine results
        result = {
          "itemDescription": search_result['itemDescription'],
          "price": search_result['price'],
          "generatedDescription": generated_description
        }
        '''

        return jsonify(search_result)
    else:
        return ('', 405)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5050, debug=True)