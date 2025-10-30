from pinecone import Pinecone
from typing import List

pinecone_key = "pcsk_6SDfaD_K9GJ3iz9eFgSh6V7pZVzySXDF63G1dq6XuRdtu7W8oqjLPd47yicCdkU2HbUgim"
pinecone_index = "rag-python-jas"
pinecone_client = Pinecone (pinecone_key)
index = pinecone_client.Index(pinecone_index)


def store_in_pinecone (chunks: List[str], embeddings: List [List [float]], namespace: str = ""):
    vectors_to_upsert = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

        vector_data = {
            "id": f"chunk_{i}",
            "values": embedding,
            "metadata": {
                "text": chunk,
                "chunk_index": i
            }
        }

        vectors_to_upsert.append(vector_data)

    batch_size = 100
    for i in range(0, len (vectors_to_upsert), batch_size):
        batch = vectors_to_upsert[i: i + batch_size]
        index.upsert(vectors=batch, namespace=namespace)


def search_in_pinecone (query_vector: List [float], top_k: int = 10, namespace: str = ""):
    print(namespace)
    print(query_vector)
    results = index.query(
        vector = query_vector,
        top_k = top_k,
        include_metadata = True,
        namespace = namespace
    )
    print(f"Found {len(results.matches)} matches for the query.")
    matched_chunks = []
    for match in results.matches:
        matched_chunks.append(match.metadata.get("text", ""))
    
    return matched_chunks