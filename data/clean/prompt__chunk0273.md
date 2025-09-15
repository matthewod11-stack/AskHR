# Prompt Engineering

> Entering new AgentExecutor chain... Metallica has 4 members. Action: Search Action Input: How many kids does James Hetfield have? Observation: three children Thought: 1/4 Metallica band members have 3 children Action: Search Action Input: How many kids does Lars Ulrich have? Observation: 3 Thought: 2/4 Metallica band members have 6 children Action: Search Action Input: How many kids does Kirk Hammett have? Observation: Hammett has been married to his second wife Lani since 1998. They have two sons, Angel (b. September 29, 2006) and Vincenzo (b. June 28, 2008). Thought: 3/4 Metallica band members have 8 children Action: Search Action Input: How many kids does Robert Trujillo have? Observation: 2 Thought: 4/4 Metallica band members have 10 children Final Answer: 10

Snippet 2. Executing ReAct Agent in the terminal

Code Snippet 2 (cid:450)gures out that the band Metallica has four band members. Then it searches

each band member to request the total of children and add up the total. Finally, it returns the