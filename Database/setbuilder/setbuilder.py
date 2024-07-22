import os
import json
import re
from typing import Union

class Setbuilder:
    ''' 
    Args:
        data_dir (str): directory containing JSON data files you'd like collated.
    '''
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir

    def combine(self, fields: Union['list[str]', None] = None) -> 'list[dict]':
        ''' `Combine` all item data files into one json file by 
        iterating through a `directory` of `JSON files`, filtering specified `fields`, 
        and concatenating them.
        ## Args:
            fields: list of strings, each string representing a field to extract from the JSON objects. If `None` don't filter.
        ## Return:
            combined_data: list of dicts, containing all the data from each JSON file.
        '''
        combined_data = list()
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                filename = self._edit_filename(filename) # Change file name to standard format
                with open(self.data_dir + '/' + filename, 'r') as file:
                    # Read and combine JSON objects into one JSON object
                    for line in file:
                        data = json.loads(line)
                        data = self._filter_data(data, fields) if fields else data # Extract fields keys only
                        combined_data.append(data)
        return combined_data

    def _edit_filename(self, filename: str) -> str:
        ''' Helper function that standardizes filenames. 
        ## Args:
            filename: Name of the file to rename.
        ## Returns:
            new_filename: Name ofthe renamed file.
        '''
        old_file_path = os.path.join(self.data_dir, filename)
        # Define the new filename
        new_filename = filename.replace(' ', '_')
        new_filename = new_filename.replace('\n', '')
        new_file_path = os.path.join(self.data_dir, new_filename)
        os.rename(old_file_path, new_file_path) # Rename the file
        return new_filename

    def _normalize_whitespace(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def _filter_data(self, item_dict: dict, fields: list) -> dict:
        ''' Filters data from a JSON-like dictionary. You can filter the first 
        instance of a key from the item_dict dictionary with a simple string, 
        e.g. ['field_to_extract', 'other_field_to_extract', ...].
        ## Args:
            item_dict: dictionary with data for field extraction.
            fields: List of key names you'd like to extract from item_dict. 
        ## Returns:
            new_dict: Field filtered version of item_dict.
        '''
        new_dict = dict()
        for field in fields:
            if isinstance(item_dict[field], str): # {key : str} pair
                new_dict[field] = self._normalize_whitespace(item_dict[field])
            elif isinstance(item_dict[field], dict): # {key : dict} pair
                new_dict[field] = [value for value in item_dict[field].values()]
            else:
                raise TypeError("Field returned a type that isn't a str or dict.")
        return new_dict