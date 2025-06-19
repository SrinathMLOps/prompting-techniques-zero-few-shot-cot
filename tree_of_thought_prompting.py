
from transformers import pipeline

def tree_of_thought():
    try:
        generator = pipeline("text-generation", model="distilgpt2")
        prompt_text = """Q: How can a mobile app increase revenue?
Explore multiple strategies:
- Strategy A: Improve customer retention through loyalty programs.
- Strategy B: Introduce premium in-app purchases.
- Strategy C: Expand user base via marketing.
Evaluate and select the best combination:"""
        result = generator(prompt_text, max_length=150, do_sample=True, temperature=0.7)
        print("\n--- Tree-of-Thought Prompting ---")
        print("Prompt:", prompt_text)
        print("Output:", result[0]['generated_text'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    tree_of_thought()
