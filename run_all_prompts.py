import os
import subprocess

# List of all prompt simulation files
files = [
    "zero_shot_prompting.py",
    "cot_prompting.py",
    "react_prompting.py",
    "reflexion_prompting.py",
    "tree_of_thought_prompting.py",
    "role_based_prompting.py",
    "auto_cot_prompting.py",
    "prompt_chaining.py"
]

print("🚀 Running all prompt simulation files...\n")

for file in files:
    print(f"🔄 Executing: {file}")
    subprocess.run(["python", file], check=True)
    print("\n" + "-"*40 + "\n")

print("✅ All prompts executed.")
