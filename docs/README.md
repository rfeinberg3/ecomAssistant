# Documentation

## User Stories

- As an e-commerce user looking to sell used items, I would like to list my items at a reasonable price, to attract potential buyers quickly.
- As a developer (especially one new to this program's code) I would like to easily integrate this program with another e-commerce API, another RAG model, or a different database service.

## Datasets

### Fashion/Clothing Dataset

[Link to dataset](https://huggingface.co/datasets/TrainingDataPro/asos-e-commerce-dataset)

- Size: 56.3 MB
- Important columns:
  - SKU: Item ID
  - Name: Title of item
  - Price: USD
  - Description: Description of item

## Models

### ColBERTv2

- [ColBERT on GitHub](https://github.com/stanford-futuredata/ColBERT?tab=readme-ov-file)
- [ColBERTv2.0 on Hugging Face](https://huggingface.co/colbert-ir/colbertv2.0)
- This model is fast, lightweight, and can produce state-of-the-art results.
  - Param count = 110M
  - Uses PyTorch and Safetensors
  - Model size is 438MB
  - Trained on MS MARCO Passage Ranking

### GPT2

- [GPT2 LMHead for text generation](https://huggingface.co/openai-community/gpt2/tree/main)

## Database

### PostgreSQL 16

#### Local Testing

After setting up the postgres image with `docker compose up db --build`, you can toy with the database on you local machine if desired. Here are some commands below to get you started.

Create the `eassistant` database:

```bash
docker exec -it ecomassistant-db-1 createdb -U postgres eassistant
```

To connect to the database from your local machine ensure that `ports` are uncommented in the `db` service within the `compose.yaml` file. Then you can run this in your local terminal to connect:

```bash
psql postgresql://postgres:1234@localhost:5431/eassistant
```

You can replace `eassistant` with the database of your choice.

You should see a prompt like this:

```bash
psql (16.0 (Homebrew), server 15.7 (Debian 15.7-1.pgdg120+1))
Type "help" for help.

eassistant=#
```