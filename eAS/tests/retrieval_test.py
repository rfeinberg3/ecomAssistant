# from ColBERT import colbert
import os, sys
from ColBERT.colbert import Searcher
from ColBERT.colbert.infra import Run, RunConfig #, ColBERTConfig
from DataCollator import DataCollator

#def set_imports_path():


def set_indexFiles_path():
    index_name = "collection.kmeans_4iters.2bits"
    #experiment_path = full_path + '/' + 'experiments' 
    return index_name

if __name__ == "__main__":
    #set_imports_path()
    index_name = set_indexFiles_path()

    # Get dataset points and factor for Search
    dataset = DataCollator('./data/dataset.json')
    title = dataset.get_queries()
    prices = dataset.get_price()
    collection = dataset.get_collection()

    # To create the searcher using its relative name (i.e., not a full path), set
    # experiment=value_used_for_indexing in the RunConfig.
    with Run().context(RunConfig()):
        searcher = Searcher(index=index_name, collection=collection)

    query = 'tmp'
    while query != '':
        query = input("\nGive a detailed name for your item, and I'll give you a good value for it, along with a description for an item similar to yours ;)\n\n")
        #query =  # try with an in-range query or supply your own
        print(f"#> {query}")

        # Find the top-3 passages for this query
        results = searcher.search(query, k=3)

        # Print out the top-k retrieved passages
        #for passage_id, passage_rank, passage_score in zip(*results):
            #print(f"\t [{passage_rank}] \t\t {passage_score:.1f} \t\t {searcher.collection[passage_id]}")

        # Get average price from top 3 results
        print("\n----------------------------------------")
        print("Similar Item --> ", title[results[0][0]], sep='')
        print("Recommended Price --> ", (float(prices[results[0][0]])+float(prices[results[0][1]])+float(prices[results[0][2]])/3), sep='')
        print("Item Description: ", f"'{collection[results[0][0]]}'", sep='\n')
        print("----------------------------------------\n")
