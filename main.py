from openai import Runtime
from bot_agent import bot_agent
from human_agent import human_agent

runtime = Runtime(agents=[bot_agent, human_agent])
runtime.run()
