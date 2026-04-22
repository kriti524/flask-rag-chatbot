from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(context_chunks, question):
    context = " ".join(context_chunks)
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    result = generator(prompt, max_new_tokens=200)
    return result[0]["generated_text"]