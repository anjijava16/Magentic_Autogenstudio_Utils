import importlib

from autogen_agentchat.agents import AssistantAgent
import os

from autogen_ext.models.openai import OpenAIChatCompletionClient
from langchain.llms import OpenAI


module_path, function_name = "app.process.tools.cust_tools.get_weather".rsplit(".", 1)
print(f"module_path= {module_path}")
print(f"function_name ={function_name}")
module = importlib.import_module(module_path)
print(f" module ={module}")
print(f"type:  {type(module)}")
get_weather_func = getattr(module, function_name)
print(get_weather_func)
print(type(get_weather_func))
tools = [get_weather_func]
print(tools)
print(type(tools))
# if get_weather_func:
#     print(f"Tool '{tool_config['name']}' imported successfully!")
# else:
#     print("Failed to import the function from the specified location.")

model_client = OpenAIChatCompletionClient(
    model="gpt-4o"
    # api_key="YOUR_API_KEY",
)
writing_agent = AssistantAgent(
    name="AssistantAgent",
    model_client=model_client,
    tools=[get_weather_func],  # Pass the tool directly to the agent
)


async def weather_agent():
    # Simulate a conversation where the agent uses the tool
    response = await writing_agent.run(task="What is the weather in New York?")
    return response


import asyncio

print(asyncio.run(weather_agent()))
