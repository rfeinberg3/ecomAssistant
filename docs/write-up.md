# Notes on Microservices and RAG

## Why Microservices?

1. **Scalability**: Microservices architecture allows different parts of the application to scale independently. For example, if the demand for image processing increases, only the image processing microservice needs to be scaled up, without affecting other parts of the application. This ensures efficient resource utilization and cost management.
2. **Flexibility**: Each microservice can be developed, deployed, and maintained independently. This modular approach means that different teams can work on different microservices simultaneously, leading to faster development cycles and easier integration of new features or updates.
3. **Resilience**: Microservices improve the resilience of the application. If one microservice fails, it does not bring down the entire system. Other microservices can continue to function, ensuring that the application remains available and operational, which is critical for maintaining user trust and satisfaction.

## Why RAG?

1. **Minimizes Hallucinations**: Retrieval-Augmented Generation (RAG) significantly reduces the problem of hallucinations in generated text. By leveraging a retrieval mechanism to pull in relevant documents or information before generating a response, RAG ensures that the generated descriptions are grounded in actual data. This is crucial for maintaining accuracy and trustworthiness in item descriptions.

2. **Enhanced Data Communication**: RAG allows models to essentially communicate with data repositories. This means that users can input queries or item images, and the model can fetch the most relevant information from a knowledge base or vector database before generating a coherent and contextually accurate description. This approach enhances the quality and relevance of the generated content.

## Why this Architecture?

### Other Models

- Other open-source models for RAG architecture out there could be used as well.
- One such example is Facebook's RAG-Token Model, a neat tokenizer-retriever-model pipeline. However, this pipeline would require lots of reconstruction to set up for our use case and doesn't have much supporting documentation to aid in this endeavor.

## Model Specifics

### ColBERT

#### Searching ColBERTv2

- This will be the main mechanism for the RAG portion of this project, and involves finding relevant data within an indexed database given a user query.
- Development of search on CPU is possible given a pre-indexed database, and will be developed before GPU search due to versatility of CPU-based programs.

#### Indexing ColBERTv2

- Indexing requires a list of passage strings to be fed to the indexer.
- The index file contained in the experiment folder can then be saved and used with the Searcher class at any point.
- Indexing a dataset.

#### Training ColBERTv2

- ColBERTv2 is trained on the MS MARCO Passage Ranking dataset.
- Training requires a JSONL triples file with a [qid, pid+, pid-] list per line. The query IDs and passage IDs correspond to the specified queries.tsv and collection.tsv files respectively.
  - pid+: positive_passage_id
  - pid-: negative_passage_id
- Remember that Queries and Collections must be formatted as TSV files:
  - Queries: each line is qid \t query text.
  - Collection: each line is pid \t passage text.
- So setting up a triples file entails pairing a query with a corresponding positive and negative passage such that:
  - Positive Passage: A passage that correctly and relevantly answers the query.
  - Negative Passage: A passage that is either irrelevant or less relevant to the query compared to the positive passage.
