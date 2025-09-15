# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True) agent.run(prompt)

Snippet 1. Creating a ReAct Agent with LangChain and Ve(cid:457)exAI

Code Snippet 2 shows the result. Notice that ReAct makes a chain of (cid:450)ve searches. In fact,

the LLM is scraping Google search results to (cid:450)gure out the band names. Then, it lists the

results as observations and chains the thought for the next search.