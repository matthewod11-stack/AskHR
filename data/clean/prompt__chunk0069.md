# Prompt Engineering

Reducing the output length of the LLM doesn’t cause the LLM to become more stylistically or textually succinct in the output it creates, it just causes the LLM to stop predicting more

tokens once the limit is reached. If your needs require a sho(cid:457) output length, you’ll also

possibly need to engineer your prompt to accommodate.

Output length restriction is especially impo(cid:457)ant for some LLM prompting techniques, like

ReAct, where the LLM will keep emi(cid:459)ing useless tokens a(cid:454)er the response you want.

Be aware, generating more tokens requires more computation from the LLM, leading to higher energy consumption and potentially slower response times, which leads to