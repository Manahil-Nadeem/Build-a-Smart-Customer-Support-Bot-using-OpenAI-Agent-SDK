from openai import Agent, ModelSettings
from tools import get_order_status
from guardrials import block_offensive_language
from human_agent import human_agent
import logging

logging.basicConfig(level=logging.INFO)

bot_agent = Agent(
    name="BotAgent",
    tools=[get_order_status],
    guardrails=[block_offensive_language],
    model_settings=ModelSettings(
        tool_choice="auto",
        metadata={"customer_id": "CUST001"}
    )
)

@bot_agent.on_message
def handle_bot_message(message, context):
    logging.info(f"[User] {message}")

    if "return policy" in message.lower():
        return "Our return policy allows returns within 30 days of purchase."
    
    elif "shipping time" in message.lower():
        return "Shipping typically takes 3-5 business days."
    
    elif any(word in message.lower() for word in ["angry", "frustrated", "not happy", "problem"]):
        logging.info("Escalating to human agent due to negative sentiment.")
        return context.handoff(to=human_agent)
    
    return "I'm not sure how to help with that. Let me connect you to a human agent."
