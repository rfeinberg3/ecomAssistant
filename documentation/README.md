# Project Notes

## User Stories
- As an e-commerce user looking to sell used items, I would like to list my items at a reasonable price, to attract potential buyers quickly.
- As a developer (especially one new to this program's code) I would like to easily integrate this program with another e-commerce API, another RAG model, or a different database service.

## Next Steps

### Postgres db in Docker container
- I want db service to be fully containerized to facilitate operation on any system.
- Docker compose + volume support can allow for in memory data usage by RAG model. i.e no need to save dataset as a file.

### ecomAssistant
- Create dataset in memory by pulling data from item table in Docker postgres database.
- Index embedding need to be created before Search API will work. Use same exact data from item table (in colab indexing notebook).
- !! See if models can be loaded in memory (ColBERT with HuggingFace).

### Look into Generative Model Options for Generating Item Descriptions
- [GPT-2 for text generation](https://huggingface.co/openai-community/gpt2/tree/main)
- BERT for fill-in-mask generation or question-answer generation? The masked part could be the item descriptions!
  - [BERT-base-uncased on Hugging Face](https://huggingface.co/google-bert/bert-base-uncased/tree/main)
- Mistral for text generation
  - [Mistral-7B-v0.1 on Hugging Face](https://huggingface.co/mistralai/Mistral-7B-v0.1?text=My+name+is+Julien+and+I+like+to)
- Phi-3 mini for text generation
  - [Phi-3 mini on Hugging Face](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct?text=Give+a+seller+description+for+the+following+item+‘Apple+Watch’)

## Notes on RAG

### ColBERTv2
- [ColBERT on GitHub](https://github.com/stanford-futuredata/ColBERT?tab=readme-ov-file)
- [ColBERTv2.0 on Hugging Face](https://huggingface.co/colbert-ir/colbertv2.0)
- This model is fast, lightweight, and can produce state-of-the-art results.
  - Param count = 110M
  - Uses PyTorch and Safetensors
  - Model size is 438MB
  - Trained on MS MARCO Passage Ranking
- [ColBERT intro colab](https://colab.research.google.com/github/stanford-futuredata/ColBERT/blob/main/docs/intro2new.ipynb#scrollTo=JRiOnzxtwI0j)

#### Searching ColBERTv2
- This will be the main mechanism for the RAG portion of this project, and involves finding relevant data within an indexed database given a user query.
- Development of search on CPU is possible given a pre-indexed database, and will be developed before GPU search due to versatility of CPU-based programs. 

#### Indexing ColBERTv2
- Indexing requires a list of passage strings to be fed to the indexer.
- The index file contained in the experiment folder can then be saved and used with the Searcher class at any point.
- Indexing a dataset 

#### Training ColBERTv2
- ColBERTv2 is trained on the MS MARCO Passage Ranking dataset. 
- Training requires a JSONL triples file with a [qid, pid+, pid-] list per line. The query IDs and passage IDs correspond to the specified queries.tsv and collection.tsv files respectively.
    - pid+: positive_passage_id
    - pid-: negative_passage_id
- Remember that Queries and Collections must be formatted as TSV files:
    - Queries: each line is qid \t query text.
    - Collection: each line is pid \t passage text.
- So setting up a triples file entails pairing a query with a corresponding positive and negative passage such that:
	-	Positive Passage: A passage that correctly and relevantly answers the query.
	-	Negative Passage: A passage that is either irrelevant or less relevant to the query compared to the positive passage.

### Other Models
- Other open-source models for RAG architecture out there could be used as well.
- One such example is Facebook's RAG-Token Model, a neat tokenizer-retriever-model pipeline. However, this pipeline would require lots of reconstruction to set up for our use case and doesn't have much supporting documentation (any really) to aid in this endeavor.
- Constructing a pipeline from scratch with the RAGatouille library seems to be a much more efficient process, provided the large amount of resources present in their framework.

## Data

### Fashion/Clothing Dataset
[Link to dataset](https://huggingface.co/datasets/TrainingDataPro/asos-e-commerce-dataset)
- Size: 56.3 MB
- Important columns:
    - SKU: Item ID
    - Name: Title of item
    - Price: USD
    - Description: Description of item

