# Retrieval-Augmented Generation (RAG) Service

## Abstract
Retrieval-Augmented Generation (RAG) has gained significant traction recently, thanks to many open-source pretrained models like Google’s T5 and Facebook’s BART. Companies are adopting this technology to enhance response accuracy and data fluency.

RAG models stand out from other query-answer generative models, such as GPTs, by utilizing a retriever or search model to query a database—whether proprietary or containing new information—before generating answers. This approach leads to more accurate and reliable responses, as opposed to non-RAG models, which risk generating “hallucinations” when answering questions beyond their training. Essentially, RAG addresses the issue of knowledge cut-off dates.

Additionally, organizations are investing in RAG models to reduce the high costs associated with training large language models (LLMs) and the continual retraining required for maintaining proprietary knowledge accuracy. RAG mitigates these costs by connecting to a database, where simply adding new data ensures ongoing response accuracy.

## Usage

### Indexing and Search
- This project uses ColBERT for Indexing and Searching the clothing dataset (~40MB of e-commerece clothing data). Indexing required GPU support, so Google Colab was leveraged to create the index embeddings of the dataset. You can see how I did this in the notebook `ColBERT_eAs_Indexing.ipynb` in the main directory.
- The embeddings are then downloaded at run time (setup with the main `Dockfile`) and used with ColBERTs Search class, and the respective dataset, to search for the topk similar documents. 

## Issues 
- Due to loading issues with the Indexing files, the directory needs to be labeled `experiments/default/indexes/INDEX_NAME` to be properly registered by the `RunConfig()`. It also needs to be in the same directory as the file running it.





