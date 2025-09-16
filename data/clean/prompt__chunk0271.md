---
source_path: prompt.md
pages: n/a-n/a
chunk_id: e52aa12e607cebb43d72f1ea203410cefe271790
title: prompt
---
# Python

from langchain.agents import load_tools from langchain.agents import initialize_agent from langchain.agents import AgentType from langchain.llms import VertexAI

prompt = "How many kids do the band members of Metallica have?"

llm = VertexAI(temperature=0.1) tools = load_tools(["serpapi"], llm=llm)
