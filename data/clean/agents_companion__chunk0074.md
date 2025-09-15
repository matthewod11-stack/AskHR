# Agent Success Metrics

Metrics are critical to building, monitoring, and comparing revisions of Agents. Business

metrics, like revenue or user engagement, are probably outside of the scope of the agent

itself but these should be the north star metric for your agents.

Most Agents are designed around accomplishing goals, so goal completion rate is a key

metric to track. Similarly, a goal might be broken down into a few critical tasks or critical

user interactions. Each of these critical tasks and interactions should be independently

instrumented and measured.

So before we get into the details of the Agent itself, we already have several metrics

identified which you should be able to easily track on a dashboard. Each business metric,

goal, or critical interaction, will be aggregated in a familiar fashion: attempts, successes,

rates, etc. Additionally, metrics you should be able to get from any application telemetry

system are very important to track for agents as well, metrics like latency, errors, etc.

12

None of these metrics are specific to Agents, you could track them for any software, but they

are even more important for Agent builders. Deterministic code does only what you tell it to

do, whereas an agent can do a lot more, relying on LLMs which are trained on huge amounts

of data. Instrumentation of these high level metrics is an important part of observability.

You can think of them as Key Performance Indicators (KPI) for the agent, and they allow for