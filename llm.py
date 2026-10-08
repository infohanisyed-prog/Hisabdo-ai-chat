from .config import GROQ_API_KEY, GROQ_MODEL
from .prompts import SYSTEM_PROMPT

try:
    from groq import Groq
except ImportError:
    Groq = None

def generate_response(history, user_message: str, context: str) -> str:
    if not GROQ_API_KEY or Groq is None:
        if "expense" in user_message.lower():
            return "To add an expense, open the Expenses area, choose the option to add a new expense, enter the required details, and save it."
        if "income" in user_message.lower():
            return "Use the income section and the available add-income workflow, then enter the required details and save the record."
        return "I can help with HisabDo product questions using the current knowledge base. Please ask about expenses, income, reports, account/settings, or another supported feature."

    client = Groq(api_key=GROQ_API_KEY)
    messages = [{"role": "system", "content": SYSTEM_PROMPT + "\n\nApproved knowledge-base context:\n" + context}]
    messages.extend({"role": m.role, "content": m.content} for m in history[-10:])
    messages.append({"role": "user", "content": user_message})
    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        temperature=0.2,
    )
    return completion.choices[0].message.content.strip()
