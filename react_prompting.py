
from transformers import pipeline

def react_prompt():
    try:
        generator = pipeline("text-generation", model="distilgpt2")
        prompt_text = """Task: Find the capital of the country with the largest population in South America.
Thought 1: Identify the most populated country.
Action 1: Search('most populated country in South America')
Observation 1: Brazil
Thought 2: Now find the capital of Brazil.
Action 2: Search('capital of Brazil')
Observation 2: Brasília
Final Answer: """
        result = generator(prompt_text, max_length=100, do_sample=True, temperature=0.7)
        print("\n--- ReAct Prompting ---")
        print("Prompt:", prompt_text)
        print("Output:", result[0]['generated_text'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    react_prompt()
