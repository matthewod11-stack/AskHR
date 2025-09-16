---
source_path: a_p_r_a_c_t_i_c_a_l.md
pages: n/a-n/a
chunk_id: 97d018fcad52a10f4f029a255d02e164430424de
title: a_p_r_a_c_t_i_c_a_l
---
# Selecting your models

Di/erent models have di/erent strengths and tradeo/s related to task complexity, latency, and cost. As we’ll see in the next section on Orchestration, you might want to consider using a variety- of models for di/erent tasks in the work(ow(cid:23)

Not every task requires the smartest model—a simple retrieval or intent classi(cid:17)cation task may be handled by a smaller, faster model, while harder tasks like deciding whether to approve a refund may bene(cid:17)t from a more capable model(cid:23)

An approach that works well is to build your agent prototype with the most capable model for every task to establish a performance baseline. From there, try swapping in smaller models to see- if they still achieve acceptable results. This way, you don’t prematurely limit the agent’s abilities, and you can diagnose where smaller models succeed or fail.

In summary, the principles for choosing a model are simple:

01

Set up evals to establish a performance baseline

02

Focus on meeting your accuracy target with the best models available

03

Optimize for cost and latency by replacing larger models with smaller ones- where possible

You can ¶nd a comprehensive guide to selecting OpenAI models here.

8

A practical guide to building agents
