---
source_path: a_p_r_a_c_t_i_c_a_l.md
pages: n/a-n/a
chunk_id: 8081cac20fe37e97538acad897e9d18dbd28ce84
title: a_p_r_a_c_t_i_c_a_l
---
# Introduction

Large language models are becoming increasingly capable of handling complex, multi-step tasks. Advances in reasoning, multimodality, and tool use have unlocked a new category of LLM-powered systems known as agents(cid:16)

This guide is designed for product and engineering teams exploring how to build their (cid:11)rst agents, distilling insights from numerous customer deployments into practical and actionable best practices. It includes frameworks for identifying promising use cases, clear patterns for designing agent logic and orchestration, and best practices to ensure your agents run safely, predictably,( and e(cid:9)ectively.’

After reading this guide, you’ll have the foundational knowledge you need to con(cid:11)dently start building your (cid:11)rst agent.

3

A practical guide to building agents

What is an agent?

While conventional software enables users to streamline and automate work#ows, agents are able to perform the same work#ows on the users’ behalf with a high degree of independence.

Agents are systems that independently accomplish tasks on your behalf.

A work^ow is a sequence of steps that must be executed to meet the user’s goal, whether that's resolving a customer service issue, booking a restaurant reservation, committing a code change,g or generating a reportG

Applications that integrate LLMs but don’t use them to control work^ow execution—think simple chatbots, single-turn LLMs, or sentiment classiEers—are not agentsG

More concretely, an agent possesses core characteristics that allow it to act reliably and consistently on behalf of a user:

01

It leverages an LLM to manage work#ow execution and make decisions. It recognizes when a work#ow is complete and can proactively correct its actions if needed. In caseg of failure, it can halt execution and transfer control back to the user.

02

It has access to various tools to interact with external systems—both to gather context and to take actions—and dynamically selects the appropriate tools depending on the work#ow’s current state, always operating within clearly de(cid:143)ned guardrails.

4

A practical guide to building agents

When should you build an agent?

Building agents requires rethinking how your systems make decisions and handle complexity. Unlike conventional automation, agents are uniquely suited to work(cid:24)ows where traditional deterministic and rule-based approaches fall short(cid:26)

Consider the example of payment fraud analysis. A traditional rules engine works like a checklist, (cid:24)agging transactions based on preset criteria. In contrast, an LLM agent functions more like a seasoned investigator, evaluating context, considering subtle patterns, and identifying suspicious activity even when clear-cut rules aren’t violated. This nuanced reasoning capability is exactly what enables agents to manage complex, ambiguous situations e(cid:23)ectively.
