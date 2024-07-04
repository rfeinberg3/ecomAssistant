# Retrieval-Augmented Generation (RAG) Service

## Abstract
Retrieval-Augmented Generation (RAG) has gained significant traction recently, thanks to many open-source pretrained models like Google’s T5 and Facebook’s BART. Companies are adopting this technology to enhance response accuracy and data fluency.

RAG models stand out from other query-answer generative models, such as GPTs, by utilizing a retriever or search model to query a database—whether proprietary or containing new information—before generating answers. This approach leads to more accurate and reliable responses, as opposed to non-RAG models, which risk generating “hallucinations” when answering questions beyond their training. Essentially, RAG addresses the issue of knowledge cut-off dates.

Additionally, organizations are investing in RAG models to reduce the high costs associated with training large language models (LLMs) and the continual retraining required for maintaining proprietary knowledge accuracy. RAG mitigates these costs by connecting to a database, where simply adding new data ensures ongoing response accuracy.

## Introduction

We will use data collected with the eBay API datascraper and utilize ColBERT as a retrieval model to gather relevant documents at query time.
<!--
## Usage
### Quick Start
- Only supports CPU right now!
- Download Docker Desktop [here](https://www.docker.com/products/docker-desktop/).
- Build and run the container
```sh
docker build -t user:colbert .
docker run -it user:colbert
```
  - This takes some time load initially (~1-2 minutes). Once loaded though answering queries is extremely quick!
- Or follow the `Testing` section below to test with conda.
-->
## Testing
- Creating a conda environement:
```sh
cd ColBERT
conda env create -f conda_env_cpu.yml
conda activate colbert
```
- With pip:
```sh
pip install install -e ColBERT\[faiss-cpu,torch\]
```
- Open retrieval.py and change the path to `path/to/your/dataset.json` in the DataCollator() initialization.
- Run script
```sh
cd tests
python retrieval.py
```

## Issues 
- Due to strange loading issues with the Indexing files, the directory needs to be labeled `experiments/default/indexes/INDEX_NAME` in ordered to be properly registered by the `RunConfig()`. It also needs to be in the same directory as the file runnign it.

## References

### ColBERTv2
- [ColBERT on GitHub](https://github.com/stanford-futuredata/ColBERT?tab=readme-ov-file)
- [ColBERTv2.0 on Hugging Face](https://huggingface.co/colbert-ir/colbertv2.0)
- This model is fast, lightweight, and can produce state-of-the-art results.
  - Param count = 110M
  - Uses PyTorch and Safetensors
  - Model size is 438MB
  - Trained on MS MARCO Passage Ranking
- [ColBERT intro colab](https://colab.research.google.com/github/stanford-futuredata/ColBERT/blob/main/docs/intro2new.ipynb#scrollTo=JRiOnzxtwI0j)

## Future work
- GPU python script for ColBERT search.

### Look into Generative Model Options for Generating item Descriptions
- [GPT-2 for text generation](https://huggingface.co/openai-community/gpt2/tree/main)
- BERT for fill-in-mask generation or question-answer generation? The masked part could be the item descriptions!
  - [BERT-base-uncased on Hugging Face](https://huggingface.co/google-bert/bert-base-uncased/tree/main)
- Mistral for text generation
  - [Mistral-7B-v0.1 on Hugging Face](https://huggingface.co/mistralai/Mistral-7B-v0.1?text=My+name+is+Julien+and+I+like+to)
- Phi-3 mini for text generation
  - [Phi-3 mini on Hugging Face](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct?text=Give+a+seller+description+for+the+following+item+‘Apple+Watch’)

### Look into Optimizing ColBERT for OpenQA Tasks
- [Relevance-guided Supervision for OpenQA with ColBERT](https://arxiv.org/abs/2007.00814)

## Discussion

**Other Models**
- There are other open-source models for RAG architecture out there that could be used as well.
- One such example is Facebook's RAG-Token Model, a neat tokenizer-retriever-model pipeline. However, this pipeline would require lots of reconstruction to set up for our use case and doesn't have much supporting documentation (any really) to aid in this endeavor.
- Constructing a pipeline from scratch with the RAGatouille library seems to be a much more efficient process, provided the large amount of resources present in their framework.

