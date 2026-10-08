import json
import re
from pathlib import Path

KB_PATH = Path(__file__).resolve().parent.parent / "data" / "knowledge_base.json"

with KB_PATH.open("r", encoding="utf-8") as f:
    KNOWLEDGE_BASE = json.load(f)

def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def retrieve(query: str, top_k: int = 3) -> list[dict]:
    q = _tokens(query)
    scored = []
    for doc in KNOWLEDGE_BASE:
        text = f"{doc['title']} {doc['content']}"
        tokens = _tokens(text)
        score = len(q & tokens)
        if score:
            scored.append((score, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored[:top_k]]

def format_context(docs: list[dict]) -> str:
    if not docs:
        return "No relevant approved knowledge-base content was found."
    return "\n\n".join(
        f"[{doc['id']}] {doc['title']}: {doc['content']}" for doc in docs
    )
