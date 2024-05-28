import os, sys
sys.path.append('..')
import json
from src.scraper import scraper

if __name__ == '__main__':
    with open('keywords.txt', 'r') as keyword_file:
        keywords = keyword_file.readlines()

    datascraper = scraper()
    for keyword in keywords:
        for data_dump in datascraper.search_and_scrape(keyword.lower(), limit='200', offset='0'):
            with open(f'data/{keyword.lower()}_data.json', 'a') as outfile:
                json.dump(data_dump, outfile)
                outfile.write("\n")