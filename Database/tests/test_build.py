import os
import json
import pandas as pd
from database import Setbuilder

if __name__ == '__main__':
    # Data Directory Path
    data_dir = '../DataScraper/outputs'
    os.path.join(data_dir)

    # Build dataset
    list_of_dicts = Setbuilder(data_dir).combine(['itemId', 'title', 'price', 'condition', 'itemDescription'])

    df = pd.DataFrame(list_of_dicts)

    # Write to json file
    df.to_json('outputs/dataset.json', indent=1, index=False)

    # Write to csv
    df.to_csv('outputs/dataset.csv', sep=',', index=False)