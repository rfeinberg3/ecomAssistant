# Retrieval-Augmented Generation (RAG) Service

## Abstract
Retrieval-Augmented Generation (RAG) has gained significant traction recently, thanks to many open-source pretrained models like Google’s T5 and Facebook’s BART. Companies are adopting this technology to enhance response accuracy and data fluency.

RAG models stand out from other query-answer generative models, such as GPTs, by utilizing a retriever or search model to query a database—whether proprietary or containing new information—before generating answers. This approach leads to more accurate and reliable responses, as opposed to non-RAG models, which risk generating “hallucinations” when answering questions beyond their training. Essentially, RAG addresses the issue of knowledge cut-off dates.

Additionally, organizations are investing in RAG models to reduce the high costs associated with training large language models (LLMs) and the continual retraining required for maintaining proprietary knowledge accuracy. RAG mitigates these costs by connecting to a database, where simply adding new data ensures ongoing response accuracy.

## Testing Setup
- Creating a conda environment:
```sh
cd ColBERT
conda env create -f conda_env_cpu.yml
conda activate colbert
```
- And install the required path dependencies with pip:
```sh
pip install -e ColBERT\[faiss-cpu,torch\]
```
- Open retrieval.py and change the path to `path/to/your/dataset.json` in the DataCollator() initialization.
- Run script
```sh
cd tests
python retrieval_test.py
```

## Issues 
- Due to loading issues with the Indexing files, the directory needs to be labeled `experiments/default/indexes/INDEX_NAME` to be properly registered by the `RunConfig()`. It also needs to be in the same directory as the file running it.





