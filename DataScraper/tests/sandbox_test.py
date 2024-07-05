import json
from datascraper import Scraper

if __name__ == '__main__':
    # Set keyset config file path
    keysetConfigPath = "./config/account-credentials.json"
    
    # Set path to keyword file you wish to use and read data
    keywords_path = "./keywords/keywords_large.txt" 
    with open(keywords_path, 'r') as keyword_file:
        keywords = keyword_file.readlines()

    # Call the data scraper and run as a generator
    datascraper = Scraper(environment='SANDBOX', keyset='DataScraper', keysetConfigPath=keysetConfigPath)
    for keyword in keywords:
        keyword = keyword.lower().replace('\n', '')
        print(f"Scraping items related to '{keyword}'...")
        # Use search_and_scrape() as a generator, aka itereator, that scrapes up to 200 items per key word.
        for data_dump in datascraper.search_and_scrape(keyword, limit='200'): 
            data_dump['keyword'] = keyword # May be important later.
            with open(f"./outputs/{keyword}_data.json", 'a') as outfile:
                json.dump(data_dump, outfile)
                outfile.write("\n")
