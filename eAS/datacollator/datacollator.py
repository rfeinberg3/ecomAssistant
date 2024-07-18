import json

class DataCollator:
    def __init__(self, data_path):
        with open(data_path, 'r') as file:
            self.data = json.load(file)

    def get_collection(self):
        return [passage for passage in self.data['itemDescription'].values()]

    def get_queries(self):
        return [query for query in self.data['title'].values()]
    
    def get_price(self):
        return [price for price in self.data['price'].values()]
    
    def get_condition(self):
        return [condition for condition in self.data['condition'].values()]
    
    


