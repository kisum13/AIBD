import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "training_data" / "reply_dataset.jsonl"

def append_example(example: dict):
    example.setdefault("date", str(date.today()))
    with DATASET.open("a", encoding="utf-8") as f:
        f.write(json.dumps(example, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    append_example({
        "id": "new_example_001",
        "language": "English",
        "category": "pricing_negotiation",
        "stage": "pricing_discussion",
        "emotion": "interested",
        "creator_message": "Can you increase the fixed fee?",
        "context": "Fixed fee cannot increase; recommend Revenue Share.",
        "recommended_reply": "Thank you so much for your reply...",
        "chinese_translation": "谢谢回复……",
        "notes": "Redirect to Revenue Share.",
        "result": "pending"
    })
    print("Added example.")
