
import google.generativeai as genai


genai.configure(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxx")  # replace with your key #free key

# 2️⃣ Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.5-pro")  # free-tier supported model

def query_llm_with_context(query: str, context: str) -> str:
    """
    Query Gemini LLM using a provided context.
    Returns the LLM's response as a string.
    """
    system_content = (
        "You are a helpful assistant that answers user queries based only on the provided context.\n"
        "Consider you are the chat bot assistance of that particular sector example it the data is balout hospital  then consider you are a part of that , similarly if bakery data , then consider you are one of that baker member , so have that in mind and respond in such way"
        "Use the context to give accurate and relevant answers.\n"
        "If the context does not contain enough information to answer, respond clearly that you cannot answer based on the given context."
    )
    print(context)
    # Combine system prompt, context, and user query
    prompt = f"{system_content}\n\nCONTEXT:\n{context}\n\nUSER QUERY:\n{query}"

    # Generate response from Gemini
    response = model.generate_content(prompt)


    return response.text.strip()


