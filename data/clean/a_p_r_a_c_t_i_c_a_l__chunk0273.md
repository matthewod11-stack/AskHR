---
source_path: a_p_r_a_c_t_i_c_a_l.md
pages: n/a-n/a
chunk_id: 639f2a78e45d1080941699be61a0d7aeaead5c22
title: a_p_r_a_c_t_i_c_a_l
---
# print

(

"Churn detection guardrail tripped"

0

A practical guide to building agents

The Agents SDK treats guardrails as (cid:20)rst-class concepts, relying on optimistic execution by default. Under this approach, the primary agent proactively generates outputs while guardrails(cid:22) run concurrently, triggering exceptions if constraints are breached.(cid:21)

Guardrails can be implemented as functions or agents that enforce policies such as jailbreak prevention, relevance validation, keyword (cid:20)ltering, blocklist enforcement, or safety classi(cid:20)cation. For example, the agent above processes a math question input optimistically until the math_homework_tripwire guardrail identi(cid:20)es a violation and raises an exception.
