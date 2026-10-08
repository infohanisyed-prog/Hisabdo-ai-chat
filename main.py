from fastapi import FastAPI
from .models import ChatRequest, ChatResponse
from .storage import add_message, get_messages
from .rag import retrieve, format_context
from .llm import generate_response

app = FastAPI(title="HisabDo AI Chat API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "hisabdo-ai-chat"}

@app.get("/conversations/{conversation_id}/messages")
def conversation_messages(conversation_id: str):
    return {"conversation_id": conversation_id, "messages": get_messages(conversation_id)}

@app.get("/knowledge-base/search")
def knowledge_base_search(q: str, top_k: int = 3):
    docs = retrieve(q, top_k)
    return {"query": q, "results": docs}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    history = get_messages(request.conversation_id)
    docs = retrieve(request.message)
    context = format_context(docs)

    add_message(request.conversation_id, "user", request.message)
    response = generate_response(history, request.message, context)
    add_message(request.conversation_id, "assistant", response)

    return ChatResponse(
        conversation_id=request.conversation_id,
        response=response,
        sources=[doc["id"] for doc in docs],
    )
