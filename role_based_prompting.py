
from transformers import pipeline

def role_based_prompt():
    try:
        generator = pipeline("text-generation", model="distilgpt2")
        prompt_text = """You are a Senior MLOps Engineer with 10 years of experience.
Explain how to deploy a FastAPI machine learning model using Docker and Kubernetes:"""
        result = generator(prompt_text, max_length=100, do_sample=True, temperature=0.7)
        print("\n--- Role-Based Prompting ---")
        print("Prompt:", prompt_text)
        print("Output:", result[0]['generated_text'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    role_based_prompt()
