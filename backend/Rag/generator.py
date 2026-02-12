import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(query: str, context: str):

    prompt = f"""
You are an intelligent assistant.

Use ONLY the provided context to answer the question.
If the answer is not found in the context, say "I don't know".

Context:
{context}

Question:
{query}

Answer:
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"
