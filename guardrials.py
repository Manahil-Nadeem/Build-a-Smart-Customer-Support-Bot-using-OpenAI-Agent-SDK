from openai import guardrail

offensive_keywords = ["stupid", "idiot", "hate", "worst"]

@guardrail
def block_offensive_language(message: str):
    if any(word in message.lower() for word in offensive_keywords):
        return "Please be respectful. Let me know how I can assist you!"
