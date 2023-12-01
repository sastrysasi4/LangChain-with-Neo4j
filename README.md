# Langchain with Neo4j

In this project, we will see how to use a Graph database (Neo4j) instead of a Vector database.
## Installation

These are the required packages

* Langchain
* Langchain_experimental
* OpenAI
* Tiktoken
* Neo4j

## Documentation


Here, we are going to see how to store the user data. (PDF data) into Graph Database and use RetrievalQA to ask questions about that data.

We have taken a PDF file that contains Indian ART History information. Then we passed this text data into a text splitter with a chunk size of 1000 and chunk overlap of 30. and we took embeddings and model from OpenAI.

For the Graph Database, we chose Neo4j, where we passed chunked text and OpenAI embeddings to change into a vector and store it. then using RetrievalQA to query the questions.
## Features

* Model -- OpenAI API
* Embeddings -- OpenAI API
* Document loader -- Pypdf loader
* Text splitter -- CharacterTextSplitter
* Graph DB -- Neo4j
* QA chain -- qa_retriable



## Authors

- [@sasidhar](https://github.com/sastrysasi4)

