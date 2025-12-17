from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Agent to answer questions using Google Search.",
    instruction="You are an expert researcher. Use Google Search to find accurate information and provide detailed answers.",
    tools=[google_search],
)
