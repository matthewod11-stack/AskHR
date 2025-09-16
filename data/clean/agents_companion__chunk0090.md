---
source_path: agents_companion.md
pages: n/a-n/a
chunk_id: b2502012f92c22e5a6f0256f169e04bfd29b4a2b
title: agents_companion
---
# the expected path.

- 2. In-order match: This metric assesses an agent's ability to complete the expected

trajectory, while accommodating extra, unpenalized actions. Success is defined by

completing the core steps in order, with flexibility for additional actions.

- 3. Any-order match: Compared to in-order match, this metric now disregards the order. It

asks if the agent included all necessary actions, but does not look into the order of actions

taken and also allows for extra steps.

18

- 4. Precision: How many of the tool calls in the predicted trajectory are actually relevant or

correct according to the reference trajectory?

- 5. Recall: How many of the essential tool calls from the reference trajectory are actually

captured in the predicted trajectory?

- 6. Single-tool use: Understand if a specific action is within the agent's trajectory. This

metric is useful to understand if the agent has learned to utilize a particular tool yet.

Figure 6: A radar chart plotting a single trajectory evaluation with a few metrics.24

19

Consider these metrics as different lenses for analyzing and debugging your agent's

trajectory. Each metric offers a unique perspective, but not all will be relevant to every

situation. For instance, some use cases demand strict adherence to the ideal trajectory, while

others allow for more creative deviations. A clear limitation of this evaluation approach is that

you need to have a reference trajectory in place for this to work. While ground-truth-based

automated trajectory evaluations that are discussed here are prevalent in popular libraries.

Research is advancing the use of agent autoraters for more efficient evaluation, for example
