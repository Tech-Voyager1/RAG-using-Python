from gemeni_llm import query_llm_with_context
from vector_storings import search_in_pinecone
from embedding import embed_user_chunks

def process_user_query(query: str,namespace: str = ""):
# Embed the user's query to create a vector representation
    query_vector = embed_user_chunks(query)[0]
    print(query_vector)
    print("Query vector total vector =",len(query_vector))

# Search the vector DB to find top matching chunks related to the us
    matched_chunks = search_in_pinecone (query_vector,namespace=namespace)
# Send the user query and the search results (query + context) to th
    generated_response = query_llm_with_context(query, matched_chunks)
    print(generated_response)

if __name__ == "__main__":
    # user_query = "is there online delivery available ?"
    user_query = input("Enter the query => ")
    process_user_query(user_query,"Policy2") #Policy #College 