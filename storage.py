from datetime import datetime, timezone
from .models import Message

_CONVERSATIONS: dict[str, list[Message]] = {}

def add_message(conversation_id: str, role: str, content: str) -> Message:
    message = Message(
        role=role,
        content=content,
        timestamp=datetime.now(timezone.utc).isoformat()
    )
    _CONVERSATIONS.setdefault(conversation_id, []).append(message)
    return message

def get_messages(conversation_id: str) -> list[Message]:
    return _CONVERSATIONS.get(conversation_id, []).copy()
