
from transformers import pipeline

def prompt_chaining():
    try:
        generator = pipeline("text-generation", model="distilgpt2")
        step1 = "Step 1: Extract key points from the article: 'The stock market rose sharply today due to tech gains.'"
        step2 = "Step 2: Summarize the extracted point: 'Tech stocks led market gains today.'"
        step3 = "Step 3: Classify this summary under one category: [Economy, Sports, Politics, Technology]"
        full_prompt = f"{step1}\n{step2}\n{step3}\nCategory:"

        result = generator(full_prompt, max_length=100, do_sample=True, temperature=0.7)
        print("\n--- Prompt Chaining ---")
        print("Prompt:", full_prompt)
        print("Output:", result[0]['generated_text'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    prompt_chaining()
