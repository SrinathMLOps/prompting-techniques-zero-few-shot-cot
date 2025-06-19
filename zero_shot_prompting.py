from transformers import pipeline

def zero_shot_prompting(text, candidate_labels=None):
    if candidate_labels is None:
        candidate_labels = ["politics", "finance", "technology", "entertainment"]

    classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")
    result = classifier(text, candidate_labels)

    print(f"\nZero-Shot Classification for: '{text}'")
    print(f"Candidate Labels: {candidate_labels}")
    print(f"Predicted labels: {result['labels']}")
    print(f"Scores: {result['scores']}")

if __name__ == "__main__":
    print("--- Zero-Shot Prompting Example ---")
    zero_shot_prompting("The new iPhone was announced today with several innovative features.")
    zero_shot_prompting("Interest rates are expected to rise next quarter.")
