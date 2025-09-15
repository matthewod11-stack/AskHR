# Python

from langchain.agents import load_tools from langchain.agents import initialize_agent from langchain.agents import AgentType from langchain.llms import VertexAI

prompt = "How many kids do the band members of Metallica have?"

llm = VertexAI(temperature=0.1) tools = load_tools(["serpapi"], llm=llm)