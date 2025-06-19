# Prompt Engineering Examples

This repository contains Python scripts demonstrating three common prompt engineering techniques:

- **Zero-Shot Prompting:** Performing tasks without any examples.
- **Few-Shot Prompting:** Providing a few examples to guide the model.
- **Chain-of-Thought (CoT) Prompting:** Encouraging the model to think step-by-step.

## Setup

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd prompt_engineering_examples
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run each script individually to see the examples in action:

- **Zero-Shot Prompting:**

  ```bash
  python3 zero_shot.py
  ```

- **Few-Shot Prompting:**

  ```bash
  python3 few_shot.py
  ```

- **Chain-of-Thought Prompting:**

  ```bash
  python3 cot.py
  ```

## Models Used

- Zero-Shot: `typeform/distilbert-base-uncased-mnli`
- Few-Shot: `distilgpt2` (used here for simulated translation)
- Chain-of-Thought: `google/flan-t5-small`

> Note: These models are automatically downloaded by the `transformers` library when you run the scripts. Ensure you are connected to the internet the first time.

