import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms.openai import OpenAI
from langchain.vectorstores import Neo4jVector
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
load_dotenv()

url="neo4j+s://1b46e771.databases.neo4j.io"
username="neo4j"
password="insert password"

if __name__ == '__main__':
    print("hi Neo4j")

    pdf_path = 'Indian_history.pdf'
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 30, separator='\n')
    docs = text_splitter.split_documents(documents)

    llm = OpenAI()

    # Instantiate Neo4j vector from documents
    neo4j_vector = Neo4jVector.from_documents(
        docs,
        OpenAIEmbeddings(),
        url= url,
        username= username,
        password= password
        )
    
    qa = RetrievalQA.from_chain_type(llm, 
                                     chain_type='stuff', 
                                     retriever = neo4j_vector.as_retriever())
    
    res = qa.run('summarize on Pala-Sena Art')
    print(res)