
from transformers import pipeline

def reflexion_prompt():
    try:
        generator = pipeline("text-generation", model="distilgpt2")
        prompt_text = """Q: What is the capital of France?
Answer: Berlin
Critique: That doesn’t seem right.
Let me try again.
Revised Answer:"""
        result = generator(prompt_text, max_length=60, do_sample=True, temperature=0.7)
        print("\n--- Reflexion Prompting ---")
        print("Prompt:", prompt_text)
        print("Output:", result[0]['generated_text'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    reflexion_prompt()
