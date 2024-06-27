# from ColBERT import colbert
from ColBERT.colbert import Searcher
from ColBERT.colbert.infra import Run, RunConfig #, ColBERTConfig
from DataCollator import DataCollator

if __name__ == "__main__":
    experiment_path = ''
    index_name = "collection.kmeans_4iters.2bits"
    dataset = DataCollator('output/dataset.json')
    collection = dataset.get_collection()
    prices = dataset.get_price()
    title = dataset.get_queries()

    # To create the searcher using its relative name (i.e., not a full path), set
    # experiment=value_used_for_indexing in the RunConfig.
    with Run().context(RunConfig(experiment=experiment_path)):
        searcher = Searcher(index=index_name, collection=collection)

    query = 'tmp'
    while query != '':
        query = input("\nGive a detailed name for your item, and I'll give you a good value for it, along with a description for an item similar to yours ;)\n")
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