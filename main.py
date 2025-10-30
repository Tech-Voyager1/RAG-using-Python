from pdf_reader import read_pdf
from chunk_creation import chunk_pages
from embedding import embed_chunks
from vector_storings import store_in_pinecone
from typing import List

pdf_path = "./resources/policy2.pdf"
def run():

    pages = read_pdf(pdf_path)
    print("No of pages in pdf =",len(pages),pages)

    print("---Creating Chunks----")
    chunks = chunk_pages(pages,chunk_size=800, chunk_overlap=150)
    print("Total chunks created =",len(chunks))
    
    print("--Creating embeddings--")
    embeddings = embed_chunks(chunks)
    print("Total chunks created =",len(embeddings))
    
    print("--Stroing vectors in Pinecone--")
    store_in_pinecone(chunks, embeddings,namespace="Policy2")

if __name__ == "__main__":
    run()