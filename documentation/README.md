# Project Overview

## Key Aspects
- **Retrieval-Augmented Generation (RAG)**: Fast and size efficient document retrieval.
- **Microservice Architecture**: Using Docker-compose to orchestrate containerization.
- **REST APIs**: Scalable and efficient API calls for knowledge base development.

## User Stories
- As an e-commerce user looking to sell used items, I would like to list my item at a reasonable price, as to attract potiental buyers quickly.
- As an AI developer I would like a tool that allows me to easily scrape useful data about items from e-commerece websites.
- As a developer (especially one new to this programs code) I would like to be able to easily integrate this program with another e-commerce API, another RAG model, or a different database service.


## Why Microservices?

1.	**Scalability**: Microservices architecture allows different parts of the application to scale independently. For example, if the demand for image processing increases, only the image processing microservice needs to be scaled up, without affecting other parts of the application. This ensures efficient resource utilization and cost management.
2.	**Flexibility**: Each microservice can be developed, deployed, and maintained independently. This modular approach means that different teams can work on different microservices simultaneously, leading to faster development cycles and easier integration of new features or updates.
3.	**Resilience**: Microservices improve the resilience of the application. If one microservice fails, it does not bring down the entire system. Other microservices can continue to function, ensuring that the application remains available and operational, which is critical for maintaining user trust and satisfaction.


## Why eBay?

With numerous e-commerce websites available, why choose eBay? While it may not be everyone's favorite e-commerce platform, I believe eBay is the best choice for this application for several important reasons.

1. **Open-Source API Support:** eBay is the most well-known e-commerce website that supports open-source RESTful API calls. Although more popular services like Facebook Marketplace and OfferUp exist, they don’t offer public APIs.

2. **Extensive Developer Support:** eBay has extensive developer support, evident through consistent updates, maintenance, and community engagement events. This robust support ensures a reliable and up-to-date API service.

3. **Vast and High-Quality Data:** eBay provides a vast quantity and quality of data, superior to other e-commerce sites like Etsy or Shopify. High-quality data is crucial for training a model to generate descriptions of everyday items people may wish to resell. Unlike Shopify and Etsy, which cater more to entrepreneurial startups, eBay's data is well-suited for this purpose.

## Why RAG?
1.	**Minimizes Hallucinations**: Retrieval-Augmented Generation (RAG) significantly reduces the problem of hallucinations in generated text. By leveraging a retrieval mechanism to pull in relevant documents or information before generating a response, RAG ensures that the generated descriptions are grounded in actual data. This is crucial for maintaining accuracy and trustworthiness in item descriptions.

2.	**Enhanced Data Communication**: RAG allows models to essentially communicate with data repositories. This means that users can input queries or item images, and the model can fetch the most relevant information from a knowledge base or vector database before generating a coherent and contextually accurate description. This approach enhances the quality and relevance of the generated content.

## Notes for ColBERT

### Searching ColBERTv2
- This will be the main mechanism for the RAG portion of this project, and involves finding relevant data within an indexed database given a user query.
- Development of search on CPU is possible given a preindexed database, and will be developed before GPU search due to versitility of CPU-based programs. 

### Indexing ColBERTv2
- Indexing requires a list of passage strings to be fed to the indexer.
- The index file contained in the experiment folder can then be saved and used with the Searcher class at any point.
- Indexing a dataset 

### Training ColBERTv2
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

## Notes for Data Scraper

### Selenium Docker Image
- The datascraper needs Selenium and Chrome drivers to by installed to run. Creating a docker container for this will be difficult, but extremely useful, as installing Chrome drivers on a machine that doesn't have them is a less than trivial issue for setting up this program.
- [Docker Selenium Standalone Chrome Image Documentation](https://hub.docker.com/r/selenium/standalone-chrome)