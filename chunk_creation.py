from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_pages(pages: List[str], chunk_size: int = 900, chunk_overlap: int = 150) -> List[str]:
    """Splits PDF pages into clean text chunks without breaking sentences."""
    
    # Join all pages into one string
    full_text = " ".join(pages).strip()

    # Initialize the text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", ",", " "]
    )

    # Split text into chunks
    chunks = splitter.split_text(full_text)

    print(f"Created {len(chunks)} clean chunks")
    return chunks



# from typing import List

# def chunk_pages(pages: List[str], chunk_size: int = 900, chunk_overlap: int = 150) -> List[str]:
#     chunks: List[str] = []
#     full_text = " ".join(pages)
#     text_length = len(full_text)
#     i=0
    
#     if text_length == 0:
#         return chunks
#     start = 0
#     while start < text_length:

#         end = min(start + chunk_size, text_length)

#         chunk = full_text[start:end].strip()
#         if chunk: 
#             chunks.append(chunk)

#         if end >= text_length:
#             break

#         start = end - chunk_overlap
#         print(f"Starting new {i} chunk from index:", start)
#         i=i+1
#     return chunks



















# # from typing import List,Tuple
# # def chunk_pages(pages: List[str], chunk_size: int = 900, chunk_overlap: int = 150) -> List[str]:
    
# #     """Takes pages from read_pdf and retruns chunks and page_map"""
# #     chunks: List[str] = []
# #     for text in pages:
# #         start = 0
# #         n = len(text)
# #         while start < n:
# #             end = min(start + chunk_size, n)
# #             chunk = text[start:end]
# #             last_period = chunk.rfind(". ")
# #             if last_period != -1 and end < n and (last_period > chunk_size * 0.5):
# #                 end = start + last_period + 2
# #                 chunk = text[start:end]
# #             chunks.append(chunk.strip())
# #             start = max(end - chunk_overlap, end)
# #     return chunks



