## modules
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import os

## env variables
load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
os.environ['TAVILY_API_KEY']=os.getenv("TAVILY_API_KEY")

## models
MODEL_NAMES = [
    "Deepseek-r1-distill-llama-70b",
    "Llama3-70b-8192"
]

## TavilySearchResults tool
tool_tavily=TavilySearchResults(max_results=2)

## TavilySearchResults into a list
tools = [tool_tavily, ]

## FastAPI Title
app = FastAPI(title='LangGraph AI Agent')

## Request schema
class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: list[str]

## API Endpoint
@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid model."}

    llm = ChatGroq(groq_api_key=groq_api_key, model_name=request.model_name) # Initializing the LLM

    agent = create_react_agent(llm, tools=tools, state_modifier=request.system_prompt) # Creating ReAct agent

    state = {"messages": request.messages} ## initializing state

    result = agent.invoke(state)  # Invoke the agent

    return result ##results


if __name__ == '__main__':
    import uvicorn 
    uvicorn.run(app, host='127.0.0.1', port=8000)