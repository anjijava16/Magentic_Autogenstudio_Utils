import json
import importlib
import importlib

from autogen_agentchat.agents import AssistantAgent
import os

from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from langchain.llms import OpenAI


# Sample JSON configuration (replace with your actual JSON string)
config_json = """
{
  "name": "weather_team",
  "component_type": "team",
  "participants": [
    {
      "name": "writing_agent",
      "component_type": "agent",
      "model_client": {
        "model": "gpt-4o-2024-08-06",
        "model_type": "OpenAIChatCompletionClient",
        "component_type": "model"
      },
      "tools": [
        {
          "name": "get_temperature",
          "description": "Get the temperature for a city.",
          "location": "app.process.tools.cust_tools.get_temperature",
          "tool_type": "PythonFunction",
          "component_type": "tool"
        },
        {
          "name": "langchain_example_tool",
          "description": "An example LangChain tool that processes a query.",
          "location": "app.process.tools.langchain_tools.langchain_tool.app_tool",
          "tool_type": "LangChainTool",
          "component_type": "tool"
        },
        {
          "name": "tavily_search",
          "description": "A LangChain tool that performs web searches using Tavily.",
          "location": "app.process.tools.langchain_tools.tavily_ex_search.tavily_search",
          "tool_type": "LangChainTool",
          "component_type": "tool"
        }
      ],
      "agent_type": "AssistantAgent"
    }
  ],
  "termination_condition": {
    "termination_type": "MaxMessageTermination",
    "max_messages": 5,
    "component_type": "termination"
  },
  "team_type": "RoundRobinGroupChat",
  "model_client": null
}
"""

# Load the JSON configuration
config = json.loads(config_json)

# Extract the agent and tool configurations
agent_config = next(p for p in config["participants"] if p["component_type"] == "agent")
tool_configs = [t for t in agent_config["tools"]]

# Load tools dynamically
tools = []
for tool_config in tool_configs:
    module_path, function_name = tool_config["location"].rsplit(".", 1)
    module = importlib.import_module(module_path)
    tool = getattr(module, function_name)
    tools.append(tool)
    print(f"Tool '{tool_config['name']}' imported successfully!")
print(tools)
print(type(tools))
model_client = OpenAIChatCompletionClient(
    model="gpt-4o"
    # api_key="YOUR_API_KEY",
)
# Create the agent with the registered tools
writing_agent = AssistantAgent(
    name=agent_config["name"],
    model_client=model_client,
    tools=tools,  # Pass all tools to the agent
    max_consecutive_auto_reply=5,
)


async def search_end_to_end_old():
    # Simulate a conversation where the agent uses the tool
    response = await writing_agent.run(
        task="What is the temperature in New York, process this query: 'Hello, world!', and search for 'latest AI news'.")
    return response

    # import asyncio
    # print(asyncio.run(search_end_to_end()))

    # Define a termination condition that stops the task if the critic approves.

    # text_termination = TextMentionTermination("APPROVE")
    #
    # # Create a team with the primary and critic agents.
    # team = RoundRobinGroupChat([writing_agent], termination_condition=text_termination)

# Define the termination condition
termination_condition = MaxMessageTermination(max_messages=5)


async def search_end_to_end():
    result = await writing_agent.run(
        task="What is the temperature in New York, process this query: 'Hello, world!', and search for 'latest AI news'.")
    return result
    # Simulate a conversation where the agent uses the tool
    # response = await writing_agent.run(task="What is the temperature in New York, process this query: 'Hello, world!', and search for 'latest AI news'.")
    # return response


# result = await team.run(task="Write a short poem about the fall season.")
# print(result)
# Example usage of the agent
# The agent will now be able to use all tools when prompted.

print(search_end_to_end)
