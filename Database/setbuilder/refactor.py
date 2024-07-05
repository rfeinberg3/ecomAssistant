import os, json, re
import pandas as pd

class Setbuilder:
    def __init__(self, data_dir: str) -> None:
        self.data_dir = data_dir

    def build(self) -> pd:
        ''' 
        '''
        combined_data = self._combine_data(self.data_dir) # list of all JSON objects in self.dir
        filtered_dict = self._filter_data(combined_data) # dictionary of only price, value, condition, and description
        df = pd.DataFrame(filtered_dict, columns=['title', 'price', 'condition', 'description']) # Create a DataFrame

    ### FIXME: Make main function
    def _combine_data(self, data_dir: str) -> list:
        ''' Combine all item data files into one json file by 
        iterating through a directory (self.data_dir) of JSON files and 
        concatenating them.
        '''
        combined_data = list()
        for file_path in os.listdir(data_dir):
            if file_path.endswith('.json'):
                self._edit_filenames(file_path) # Change file name to standard format
                ### FIXME: Read data and filter here (seperate function) instead of iterating again later and filtering
                with open(self.data_dir + '/' + file_path, 'r') as file:
                    # Read and combine JSON objects into one JSON object
                    for line in file:
                        data = json.loads(line)
                        combined_data.append(data)
        return combined_data # List of dictionaries

    def _edit_filenames(self, file_path: str) -> None:
        ''' Helper function that standardizes filenames. '''
        old_file_path = os.path.join(self.data_dir, file_path)
        # Define the new filename (modify as needed)
        new_filename = file_path.replace(' ', '_')
        new_filename = new_filename.replace('\n', '')
        new_file_path = os.path.join(self.data_dir, new_filename)
        # Rename the file
        os.rename(old_file_path, new_file_path)

    def _normalize_whitespace(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def _filter_data(self, data_list: list[dict]) -> dict:
        ''' Filters the title, price, condition, and item description 
        from a JSON-like object, and returns the filtered items 
        as a single dictionary. '''
        filtered_data = dict()
        for item in data_list:
            filtered_data['title'] = self.normalize_whitespace(item.pop('title'))
            filtered_data['price'] = item.pop('price')['value'].strip()
            filtered_data['condition'] = item.pop('condition').strip()
            filtered_data['description'] = self.normalize_whitespace(item.pop('item_description')) # Need to reformat to itemDescription eventually
        return filtered_data # List of tab seperated filtered data