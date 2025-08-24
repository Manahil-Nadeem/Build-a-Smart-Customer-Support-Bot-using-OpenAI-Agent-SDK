from openai import Agent

human_agent = Agent(name="HumanAgent")

@human_agent.on_message
def handle_handoff(message, context):
    return "You've been connected to a human agent. How can I help you further?"
