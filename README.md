# HisabDo AI Chat API

Starter implementation combining:
- Functional AI chat endpoint
- Core HisabDo system prompt
- Conversation history
- Knowledge Base
- Initial RAG retrieval
- Groq LLM integration
- Basic tests

## Setup

1. Create a virtual environment:
   `python -m venv .venv`
2. Activate it on Windows:
   `.venv\\Scripts\\activate`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your Groq API key.
5. Run:
   `uvicorn app.main:app --reload`
6. Open Swagger at `http://127.0.0.1:8000/docs`

If GROQ_API_KEY is not configured, the API still runs and returns a deterministic fallback response so the RAG pipeline can be tested.

## Main endpoint

`POST /chat`

Example body:
```json
{
  "conversation_id": "demo-1",
  "message": "How do I add an expense?"
}
```

## Knowledge Base

Edit `data/knowledge_base.json` to add or update approved HisabDo product content. The current retrieval layer is a lightweight lexical baseline suitable for the initial RAG stage.

## Flow

User -> /chat -> conversation history -> KB retrieval -> system prompt + context -> Groq/fallback -> store messages -> response
