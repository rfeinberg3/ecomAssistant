import os
import json
import re
import pandas as pd

# Path to data files
data_dir = os.path.join('..', 'DataScraper', 'outputs')

def combine_data(directory_path):
# Combine all item data files into one json file
    combined_data = []
    for file_path in os.listdir(data_dir):
        file_path.replace('\n', '?')
        if file_path.endswith('.json'):
            with open(data_dir + '/' + file_path, 'r') as file:
                try:
                    # Read and combine JSON objects correctly
                    for line in file:
                        data = json.loads(line)
                        combined_data.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {file_path}: \n{e}")
    return combined_data # List of dictionaries

def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def filter_data(data_list):
    filtered_data = set()
    for item in data_list:
        title = normalize_whitespace(item.pop('title'))
        price = item.pop('price')['value'].strip()
        condition = item.pop('condition').strip()
        description = normalize_whitespace(item.pop('item_description'))
        filtered_data.add(f"{title}\t{price}\t{condition}\t{description}")
    filtered_data = list(filtered_data)
    return filtered_data # List of tab seperated filtered data

if __name__ == '__main__':
    combined_data = combine_data(data_dir)
    filtered_data = filter_data(combined_data)

    # Write to pandas Data Frame
    split_data = [line.split('\t') for line in filtered_data] # Split each line into a list of values
    df = pd.DataFrame(split_data, columns=['title', 'price', 'condition', 'description']) # Create a DataFrame

    # Save to CSV
    df.to_json('database.json', index=True, indent=4)