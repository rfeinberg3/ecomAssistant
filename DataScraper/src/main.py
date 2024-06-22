import os, sys
sys.path.append('..')
import json
from scraper import scraper

def create_dir(directory): # Creates an empty directory if one doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__ == '__main__':
    # Set path to keyword file you wish to use and read data
    keywords_path = "./keywords/keywords_large.txt" 
    with open(keywords_path, 'r') as keyword_file:
        keywords = keyword_file.readlines()

    # Call the data scraper and run as a generator
    datascraper = scraper()
    for keyword in keywords:
        # Max limit is 200 and offset must be a multiple of limit or error will occur. deep_search=True helps to reduce search results that aren't related to the keyword.
        for data_dump in datascraper.search_and_scrape(keyword, limit='200', offset='0', deep_search=True): 
            create_dir("../outputs")
            keyword = keyword.lower().replace('\n', '')
            with open(f"../outputs/{keyword}_data.json", 'a') as outfile:
                json.dump(data_dump, outfile)
                outfile.write("\n")
                json.dumps(data_dump)
