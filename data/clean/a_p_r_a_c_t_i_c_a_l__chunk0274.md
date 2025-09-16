---
source_path: a_p_r_a_c_t_i_c_a_l.md
pages: n/a-n/a
chunk_id: 7f2b26f16a0d3ce24e5ae273dffa2a5d0f31a2be
title: a_p_r_a_c_t_i_c_a_l
---
# Plan for human interventioQ

Human intervention is a critical safeguard enabling you to improve an agent’s real-world performance without compromising user experience. It’s especially important early} in deployment, helping identify failures, uncover edge cases, and establish a robust evaluation cycle@

Implementing a human intervention mechanism allows the agent to gracefully transfer control when it can’t complete a task. In customer service, this means escalating the issue} to a human agent. For a coding agent, this means handing control back to the user@

Two primary triggers typically warrant human intervention<

Exceeding failure thresholds: Set limits on agent retries or actions. If the agent exceedN these limits (e.g., fails to understand customer intent after multiple attempts), escalat(cid:131) to human intervention@

High-risk actions: Actions that are sensitive, irreversible, or have high stakes shoulc trigger human oversight until con2dence in the agent’s reliability grows. ExampleN include canceling user orders, authorizing large refunds, or making payments.

31

A practical guide to building agents
