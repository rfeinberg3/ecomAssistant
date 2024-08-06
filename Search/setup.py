import os
from dotenv import load_dotenv
import torch
from huggingface_hub import hf_hub_download

from dbmanager import DatabaseManager

# Load environment variables
load_dotenv()

HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DBNAME = os.getenv("POSTGRES_DB")
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")

# Collect data from db and save to disk
dbm = DatabaseManager(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
df = dbm.table_to_pandas("clothing")
df.to_json('dataset.json', indent=2)
#TODO: Add list of table names to .env and loop through them here. Possibly create combine() method to combine datasets.

# Load Index Embeddings and config files from Hugging Face for Search use
pt_filenames = ["0.codes.pt", "0.residuals.pt", "1.codes.pt", "1.residuals.pt", "avg_residual.pt", "buckets.pt", "centroids.pt", "ivf.pid.pt"]
json_filenames = ["0.metadata.json", "1.metadata.json", "doclens.0.json", "doclens.1.json", "metadata.json", "plan.json"]

def load_pt_files(dir: str) -> None:
    ''' Loads pt index files from Hugging Face and saves them to disk. '''
    os.makedirs(dir, exist_ok=True)

    for filename in pt_filenames:
        file_path = hf_hub_download(repo_id="ryfye181/clothing_embeddings", filename=filename)

        with open(file_path, "rb") as pt:
            embedding = torch.load(pt, map_location=torch.device('cpu'))
        with open(dir + '/' + filename, "wb") as pt:
            torch.save(embedding, pt)

def load_json_files(dir: str) -> None:
    ''' Loads json index files from Hugging Face and saves them to disk. '''
    os.makedirs(dir, exist_ok=True)

    for filename in json_filenames:
        file_path = hf_hub_download(repo_id="ryfye181/clothing_embeddings", filename=filename)
            
        with open(file_path, "r") as json:
            data = json.read()
        with open(dir + '/' + filename, "w") as json:
            json.write(data)

load_pt_files('index/clothing.kmeans_4iters.2bits')
load_json_files('index/clothing.kmeans_4iters.2bits')