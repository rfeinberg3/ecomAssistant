import os, sys
sys.path.append('..')
import json
from src.scraper import scraper

if __name__ == '__main__':
    with open('keywords.txt', 'r') as keyword_file:
        keywords = keyword_file.readlines()
    for keyword in keywords:
        for i in range(3):
            with open(f'data/{keyword.lower()}_data.json', 'a') as outfile:
                json.dump(scraper().search_and_scrape(keyword.lower(), offset=i), outfile)
                outfile.write("\n")