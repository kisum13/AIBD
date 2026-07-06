import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "training_data" / "reply_dataset.jsonl"

def search(keyword: str):
    keyword_lower = keyword.lower()
    results = []
    for line in DATASET.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        blob = json.dumps(item, ensure_ascii=False).lower()
        if keyword_lower in blob:
            results.append(item)
    return results

if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "fixed fee"
    for item in search(q):
        print(json.dumps(item, ensure_ascii=False, indent=2))
        print("-" * 40)
