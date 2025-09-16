---
source_path: a_p_r_a_c_t_i_c_a_l.md
pages: n/a-n/a
chunk_id: 4be3dbc176a40f7ed517560734ee65c098dd4f10
title: a_p_r_a_c_t_i_c_a_l
---
# Manager pattern

The manager pattern empowers a central LLM—the “manager”—to orchestrate a network of specialized agents seamlessly through tool calls. Instead of losing context or control, the manager intelligently delegates tasks to the right agent at the right time, e(cid:12)ortlessly synthesizing the results into a cohesive interaction. This ensures a smooth, uni(cid:10)ed user experience, with specialized capabilities always available on-demand(cid:15)

This pattern is ideal for work(cid:11)ows where you only want one agent to control work(cid:11)ow execution and have access to the user.

Translate ‘hello’ to Spanish, French and Italian for me!
