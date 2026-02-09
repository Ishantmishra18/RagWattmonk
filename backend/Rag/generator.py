from transformers import pipeline

# Load LLM
generator = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=200
)

def generate_answer(query, context_chunks):
    """
    Generates final answer using retrieved context.
    """
    context = "\n".join(context_chunks)

    prompt = f"""
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    return generator(prompt)[0]["generated_text"]
