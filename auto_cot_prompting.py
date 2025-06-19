
from transformers import pipeline

def auto_cot_prompt():
    try:
        generator = pipeline("text-generation", model="distilgpt2")
        prompt_text = """Solve the equation: 5x + 3 = 18
Step-by-step reasoning:
1. Subtract 3 from both sides → 5x = 15
2. Divide both sides by 5 → x = """
        result = generator(prompt_text, max_length=60, do_sample=True, temperature=0.7)
        print("\n--- Auto-CoT Prompting ---")
        print("Prompt:", prompt_text)
        print("Output:", result[0]['generated_text'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    auto_cot_prompt()
