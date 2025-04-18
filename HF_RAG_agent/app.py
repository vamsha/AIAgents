import gradio as gr
import random
from smolagents import GradioUI, CodeAgent, HfApiModel, LiteLLMModel
import os 

# Import our custom tools from their modules
from tools import DuckDuckGoSearchTool, WeatherInfoTool, HubStatsTool
from retriever import load_guest_dataset



# Initialize the Hugging Face model
# model = HfApiModel()
# model = HfApiModel(model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud/')
model = LiteLLMModel(model_id="gemini/gemini-2.0-flash-lite", api_key="*********")

# # Initialize the web search tool
search_tool = DuckDuckGoSearchTool()

# Initialize the weather tool
weather_info_tool = WeatherInfoTool()

# Initialize the Hub stats tool
hub_stats_tool = HubStatsTool()

# Load the guest dataset and initialize the guest info tool
guest_info_tool = load_guest_dataset()

# Create Alfred with all the tools
alfred = CodeAgent(
    tools=[guest_info_tool, weather_info_tool, hub_stats_tool, search_tool], 
    model=model,
    add_base_tools=False,  # Add any additional base tools
    planning_interval=100   # Enable planning every 3 steps
)

if __name__ == "__main__":
    GradioUI(alfred).launch()