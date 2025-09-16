---
source_path: agents_companion.md
pages: n/a-n/a
chunk_id: 5a544767a89f90259c0a91646ddaaf4108e1c134
title: agents_companion
---
## observability in the aggregate, a higher level perspective of your agents.

Human feedback is one of the more critical metrics to track as well. A simple 👍👎 or user feedback form, within the context of an agent or task can go a long way to understanding

where your agent does well and where it needs improvement. This feedback can come from

end users of a consumer system, but also employees, QA testers, and process or domain

experts reviewing the agent.

More detailed observability is also very important for agent building, being able to see and

understand what the agent is doing and why it’s doing that. An agent can be instrumented

with “trace” to log all of the inner workings of the agent, not only the critically important

tasks and user interactions. You could conceptually measure every internal step as metrics,

but that is rarely done. Instead these detailed traces are used to debug an agent when

metrics or manual testing show a problem, you can dig into details and see what went wrong.

13

Figure 3: An example of Cloud Observability showing traces for an agent with tools and LLM OpenTelemetry spans.15

So far we’ve been talking about business metrics, goals, tasks, human feedback, and traces

– those are all ways of understanding the actions and impact of your agents, in production.

While developing an agent, in addition to manual testing, automated testing will be much

more efficient in the long run and provide greater insights into the behavior of agents.
