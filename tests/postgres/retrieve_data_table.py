import os, sys
sys.path.append('../../data')

import pandas as pd
from dbmanager import DatabaseManager

if __name__ == '__main__':
    dbm = DatabaseManager(dbname="eassistant", user="postgres", password="1234", host="localhost", port=5431)
    df = dbm.table_to_pandas("clothing")

    df.to_json("dataset.json", indent=2)