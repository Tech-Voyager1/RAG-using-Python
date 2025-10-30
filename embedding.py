
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List

client = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2') #all-MiniLM-L6-v2

# s = "hai im adithyan"
# print(len(client.embed_query(s)))

def embed_chunks(chunks: List[str]) -> List[List[float]]:
    """Embeds text chunks using Voyage AI's voyage-3-large model"""
    embeddings = []

    for chunk in chunks:
        response = client.embed_query(chunk)
        embeddings.append(response)

    print(f"Embedded first vector (truncated): {embeddings[0][:5]}")
    return embeddings

def embed_user_chunks(chunks: List[str]) -> List[List[float]]:
    """Embeds user query to chunks using Voyage AI's voyage-3-large model"""
    embeddings = []

    for chunk in chunks:
        response = client.embed_query(chunk)
        embeddings.append(response)

    # print(f"Embedded first vector (truncated): {embeddings[0][:5]}")
    # print(len(embeddings[0]))
    return embeddings
# import cohere
# from typing import List

# # You can either set the key here directly or via environment variable
# cohere_key = "cKHGcmxv4ofYIqVWVXR1FbjU6S79nyWYyQseAMii"
# client = cohere.Client(cohere_key)

# EMBEDDING_MODEL = "embed-english-v3.0"

# def embed_chunks(chunks: List[str]) -> List[List[float]]:
#     """Embeds text chunks using Voyage AI's voyage-3-large model"""
#     embeddings = []

#     for chunk in chunks:
#         response = client.embed(
#             model=EMBEDDING_MODEL,
#             texts=chunk , # must be a list
#             input_type = "text"
#         )
#         embeddings.append(response.embeddings[0])

#     print(f"Embedded first vector (truncated): {embeddings[0][:5]}")
#     return embeddings

# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# from typing import List

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# EMBEDDING_MODEL = "text-embedding-3-small"

# def embed_chunks(chunks: List[str]) -> List[List[float]]:
#     "Embeds chunks using OpenAi embedding model"
#     embeddings = {}
#     for chunk in chunks:
#         response = client.embeddings.create(
#             input = chunk,
#             model = EMBEDDING_MODEL
#         )
#         embeddings.append(response.data[0].embedding)

#     print(f"Embedded 2:", embeddings[0][:1])
#     return embeddings

# # pa-O46OGMi9O9mxLBmVk5doQTO7MKAK6VhuDk4Z8dsOK_8