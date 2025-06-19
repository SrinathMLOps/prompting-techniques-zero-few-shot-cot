from transformers import pipeline

def cot_prompting(question, model_name="google/flan-t5-small"):
    # Use a text2text-generation model to simulate CoT
    generator = pipeline("text2text-generation", model=model_name)

    prompt = f"""Question: {question}
Let's think step by step.
"""
    print(f"\nChain-of-Thought Prompting for question: '{question}'")
    print(f"Prompt used:\n{prompt}")

    result = generator(prompt, max_length=100, num_return_sequences=1)
    print(f"Generated thought process and answer: {result[0]['generated_text']}")
    return result[0]['generated_text']

if __name__ == "__main__":
    print("--- Chain-of-Thought Prompting Example ---")
    cot_prompting("What is the capital of France? What is the population of that city?")
    cot_prompting("If a car travels at 60 miles per hour for 3 hours, how far does it travel?")
