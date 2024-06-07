# Retrieval-Augmented Generation

## Overview

## Method

### Basic Flow of our RAG Service

1. **Knowledge Base Development**: 
   - Before the model is ready for deployment, a knowledge base must be developed. This was done via the eBay datascraper I created. See the `Datascraper` directory for details.
   - The knowledge base will be organized into a collection. In the case of using ColBERT as a retrieval model, this entails creating a list of strings (aka documents) that can be passed to the Indexer.
  
2. **Querying the RAG Service**: 
   - Once the collection is indexed, the Searcher can now take a query, which it compares to the documents in the indexed collection to find the n best fit documents based on the query.


### ColBERTv2
- [ColBERT on GitHub](https://github.com/stanford-futuredata/ColBERT?tab=readme-ov-file)
- [ColBERTv2.0 on Hugging Face](https://huggingface.co/colbert-ir/colbertv2.0)
- This model is fast, lightweight, and can produce state-of-the-art results.
  - Param count = 110M
  - Uses PyTorch and Safetensors
  - Model size is 438MB
- [ColBERT intro colab](https://colab.research.google.com/github/stanford-futuredata/ColBERT/blob/main/docs/intro2new.ipynb#scrollTo=JRiOnzxtwI0j)


### Data processing for ColBERT
- We must process our data into a database that will work with the ColBERT retrieval model. This entails processing the data that we collected into a column seperated file. Considering the eBay datascraper outputs a json file for each keyword prompted, we will have to combine all these into one file.
- ColBERT's Indexer requires us to feed it data as a list of text strings called a collection. So we'll have to figure out exactly what data we want to use for each item, and the best way to format that all into one text string. Remember that these text strings will eventually be fed to some generative model after retrieval. 


### Look into Optimizing ColBERT for OpenQA Tasks
- [Relevance-guided Supervision for OpenQA with ColBERT](https://arxiv.org/abs/2007.00814)


### Look into Generative Model Options
- [GPT-2 for text generation](https://huggingface.co/openai-community/gpt2/tree/main)
- BERT for fill-in-mask generation or question-answer generation? The masked part could be the item descriptions!
  - [BERT-base-uncased on Hugging Face](https://huggingface.co/google-bert/bert-base-uncased/tree/main)
- Mistral for text generation
  - [Mistral-7B-v0.1 on Hugging Face](https://huggingface.co/mistralai/Mistral-7B-v0.1?text=My+name+is+Julien+and+I+like+to)
- Phi-3 mini for text generation
  - [Phi-3 mini on Hugging Face](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct?text=Give+a+seller+description+for+the+following+item+‘Apple+Watch’)

**Other Models**
- There are other open-source models for RAG architecture out there that could be used as well.
- One such example is Facebook's RAG-Token Model, a neat tokenizer-retriever-model pipeline. However, this pipeline would require lots of reconstruction to set up for our use case and doesn't have much supporting documentation (any really) to aid in this endeavor.
- Constructing a pipeline from scratch with the RAGatouille library seems to be a much more efficient process, provided the large amount of resources present in their framework.

## Other Resources
**The RAGatouille Library**
- [RAGatouille on GitHub](https://github.com/bclavie/ragatouille)
- This library is designed to work with ColBERT, provide modularity and ease-of-use, and is backed by research.
