from transformers.pipelines import pipeline
from typing import List, Tuple, Optional

def few_shot_translation(prompt_text: str, target_language: str = "French") -> Optional[str]:
    try:
        generator = pipeline("text-generation", model="distilgpt2")

        result = generator(
            prompt_text,
            max_length=100,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.6,
            pad_token_id=generator.tokenizer.eos_token_id if generator.tokenizer else None,
            repetition_penalty=1.1
        )

        print(f"\n--- Few-Shot Translation Simulation ({target_language}) ---")
        print(f"Input prompt:\n{prompt_text}")

        if isinstance(result, list) and len(result) > 0:
            first_result = result[0]
            if isinstance(first_result, dict) and 'generated_text' in first_result:
                generated_text = first_result['generated_text']
                print(f"\nSimulated Translation Output: {generated_text}")
                return generated_text

        print("No output generated.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def create_translation_prompt(examples: List[Tuple[str, str]], target_text: str,
                              source_language: str = "English", target_language: str = "French") -> str:
    prompt = f"Translate the following {source_language} sentences to {target_language} (simulated):\n"
    for source, target in examples:
        prompt += f"{source_language}: {source}\n{target_language}: {target}\n"
    prompt += f"{source_language}: {target_text}\n{target_language}: "
    return prompt

if __name__ == "__main__":
    print("=== Few-Shot Prompting Examples ===\n")

    examples = [
        ("Hello, how are you?", "Bonjour, comment allez-vous?"),
        ("Thank you very much.", "Merci beaucoup."),
        ("What is your name?", "Comment vous appelez-vous?"),
        ("I love this city.", "J'aime cette ville."),
        ("The weather is beautiful today.", "Le temps est magnifique aujourd'hui.")
    ]
    target = "Can you help me find the nearest restaurant?"
    prompt = create_translation_prompt(examples, target)
    few_shot_translation(prompt)
