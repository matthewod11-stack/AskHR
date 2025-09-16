---
source_path: a_p_r_a_c_t_i_c_a_l.md
pages: n/a-n/a
chunk_id: 736cee3d9bbc1f19ef5ef87c6fa8f954635471be
title: a_p_r_a_c_t_i_c_a_l
---
# Agents.run(agent, [UserMessage(

"What's the capital of the USA?"

)])

This concept of a while loop is central to the functioning of an agent. In multi-agent systems, as you’ll see next, you can have a sequence of tool calls and handošs between agents but allow the model to run multiple steps until an exit condition is met¸

An ešective strategy for managing complexity without switching to a multi-agent framework is to use prompt templates. Rather than maintaining numerous individual prompts for distinct use cases, use a single ™exible base prompt that accepts policy variables. This template approach adapts easily to various contexts, signi–cantly simplifying maintenance and evaluation. As new use cases arise, you can update variables rather than rewriting entire work™ows.
