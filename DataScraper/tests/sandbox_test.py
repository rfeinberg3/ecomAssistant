import json
import os
from datascraper import Scraper, ScraperUtil


if __name__ == '__main__':
        
        # Ensure the output directory exists
        output_dir = "volume/outputs"
        os.makedirs(output_dir, exist_ok=True)

        # Set keyset config file path
        keysetConfigPath = "config/account-credentials.json"
        
        # Get name of each keywords file in keywords directory
        util = ScraperUtil()
        keywords_dir = 'keywords'
        file_names = util.get_filenames(directory=keywords_dir, file_type='.md')

        # Read data from each file in file_names
        keywords = util.read_files(directory=keywords_dir, list_of_filenames=file_names)
        print(f"Keywords to Scrape: {len(keywords)}\n")

        # Call the data scraper and run as a generator
        datascraper = Scraper(environment='SANDBOX', keyset='DataScraper', keysetConfigPath=keysetConfigPath)
        for keyword, i in enumerate(keywords):
            keyword = keyword.lower().replace('\n', '')
            print(f"Scraping items related to '{keyword}'... {len(keywords)-i} keywords left.")
            # Use search_and_scrape() as a generator, aka itereator, that scrapes up to 200 items per key word.
            for data_dump in datascraper.search_and_scrape(keyword, limit='200'): 
                data_dump['keyword'] = keyword # May be important later.
                with open(f"{output_dir}/data_{keyword}.json", 'a') as outfile:
                    json.dump(data_dump, outfile)
                    outfile.write("\n")

