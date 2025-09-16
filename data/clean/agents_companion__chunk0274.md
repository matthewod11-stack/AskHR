---
source_path: agents_companion.md
pages: n/a-n/a
chunk_id: d83a1b2a88afd2cbcfc58a3f539c4a82227066d5
title: agents_companion
---
# Example scenario:

- 1. User asks: "Find a place to eat sushi nearby"

- 2. The Orchestrator correctly routes this to the Conversational Navigation Agent, which

provides information about nearby sushi restaurants.

- 3. User follows up: "How big is New York's Central Park?"

- 4. The Orchestrator might initially route this to the Conversational Navigation Agent again

(based on the previous navigation-related conversation).

62

- 5. However, the Conversational Navigation Agent recognizes this as a general knowledge

question rather than a navigation request, and hands it off to the General Knowledge

Agent, which can provide factual information about Central Park's size.

Advantages of peer-to-peer hand-off compared to centralized orchestration:

- 1. Resilience to misclassification: Even if the central orchestrator makes an error in

routing, specialized agents can recognize when a query falls outside their domain and
