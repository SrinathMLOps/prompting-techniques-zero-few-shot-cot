# prompting-techniques-zero-few-shot-cot
📘 Updated README.md
Here’s the improved version you can copy-paste into your repo’s README.md file:
# 🧠 Prompt Engineering Examples (Zero-Shot, Few-Shot, CoT)

This repository demonstrates **three core prompt engineering techniques** using Hugging Face Transformers in Python:

- 🔹 **Zero-Shot Prompting** – No prior examples are provided
- 🔸 **Few-Shot Prompting** – Few examples guide the model
- 🔁 **Chain-of-Thought Prompting (CoT)** – Encourages step-by-step reasoning

---

## 📁 Project Structure

```text
.
├── zero_shot.py      # Zero-shot classification using DistilBERT
├── few_shot.py       # Simulated translation using few-shot prompting
├── cot.py            # Chain-of-Thought reasoning with Flan-T5
├── requirements.txt  # Dependencies
├── todo.md           # Project task checklist
└── README.md         # Documentation



🛠️ Setup
✅ 1. Clone the repository
git clone https://github.com/<your-username>/prompt-engineering-examples.git
cd prompt-engineering-examples

✅ 2. Create a virtual environment (recommended)
python -m venv venv
source venv/Scripts/activate     # On Windows Git Bash
# OR
venv\Scripts\activate.bat        # On CMD/PowerShell
✅ 3. Install dependencies
pip install -r requirements.txt
🚀 Run Examples
🔹 Zero-Shot Prompting
python zero_shot.py
🔸 Few-Shot Prompting (Simulated Translation)
python few_shot.py
🔁 Chain-of-Thought Prompting
python cot.py
📦 Models Used
| Task             | Model                                   |
| ---------------- | --------------------------------------- |
| Zero-Shot        | `typeform/distilbert-base-uncased-mnli` |
| Few-Shot         | `distilgpt2` (used for text generation) |
| Chain-of-Thought | `google/flan-t5-small`                  |
💡 All models are downloaded automatically by transformers. Ensure you're connected to the internet the first time.
🧩 Project Roadmap
✅ Zero-Shot example (text classification)

✅ Few-Shot translation using examples

✅ Chain-of-Thought logic reasoning

✅ Model-agnostic prompt templates

⏳ Optionally add GUI with Streamlit

⏳ Support for OpenAI/GPT APIs

📋 Todo Progress
✅ Project setup
✅ All 3 prompting modes implemented
✅ Dependencies tested
✅ Ready for GitHub deployment
🛠️ Dependencies
transformers
torch
accelerate
sentencepiece
Install via:
pip install -r requirements.txt
🙌 Author
Made with passion by Srinath


---

## 🚧 Push to GitHub: Quick Commands

### 1. Create new GitHub repo (name: `prompt-engineering-examples`)

### 2. Push your code:

```bash
git init
git remote add origin https://github.com/<your-username>/prompt-engineering-examples.git
git add .
git commit -m "Initial commit: Zero-shot, Few-shot, CoT examples"
git push -u origin main
