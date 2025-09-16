---
source_path: agents_companion.md
pages: n/a-n/a
chunk_id: ba8257a1d339af97c138bc0d7aebd844b41377cf
title: agents_companion
---
# Multi-Agent Evaluation

Luckily, the evaluation of multi-agent systems is a clear progression of evaluating single

agent systems. Agent Success Metrics are unchanged, business metrics as your north star,

goals and critical task success metrics, application telemetry metrics like latency and errors.

Instrumenting the multi-agent system with trace will help debug and understand what is

happening during complex interactions.

In the Agent Evaluation section we discussed Evaluating Trajectories and Evaluating the Final

Response as the 2 best approaches to automated evaluation of an agent, and this remains

the case for multi-agent systems. For a multi-agent system, a trajectory of actions might

include several or even all of your agents. Even though several agents may collaborate on a

task, a single final answer is returned to the user at the end and can be evaluated in isolation.

Because a multi-agent system probably has more steps, you can drill down and evaluate at

every step. You can evaluate each of your agents in isolation and the system as a whole.

Trajectory evaluations are a scalable approach to do exactly this.

There are some questions you need to ask, which are unique to multi-agent

systems, including:

- Cooperation and Coordination: How well do agents work together and coordinate their

actions to achieve common goals?

- Planning and Task Assignment: Did we come up with the right plan, and did we stick to

it? Did child agents deviate from the main plan or get lost in a cul-de-sac?

- Agent Utilization: How effectively do agents select the right agent and choose to use the

agent as a tool, delegate a background task, or transfer the user?

32

- Scalability: Does the system's quality improve as more agents are added? Does the

latency go down? Are we being more efficient or less?

These types of questions can guide developers to identify areas for improvement in the

multi-agent system. You will answer these questions using the same tools you use for single

agent systems, but the complexity of the analysis goes up.
