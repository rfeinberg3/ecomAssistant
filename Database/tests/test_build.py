import os
import pandas as pd
from setbuilder import Setbuilder

if __name__ == '__main__':
    # Ensure the output directory exists
    output_dir = 'volume/sets'
    os.makedirs(output_dir, exist_ok=True)

    # Input dir
    data_dir = 'volume/outputs'

    # Build dataset
    list_of_dicts = Setbuilder(data_dir).combine(['itemId', 'title', 'price', 'condition', 'itemDescription'])

    df = pd.DataFrame(list_of_dicts)

    # Write to json file
    df.to_json('volume/sets/dataset.json', indent=1, index=False)

    # Write to csv
    df.to_csv('volume/sets/dataset.csv', sep=',', index=False)