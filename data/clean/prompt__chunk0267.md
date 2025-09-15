# approaches in a variety of domains.

ReAct prompting works by combining reasoning and acting into a thought-action loop. The

LLM (cid:450)rst reasons about the problem and generates a plan of action. It then pe(cid:455)orms the

actions in the plan and observes the results. The LLM then uses the observations to update

its reasoning and generate a new plan of action. This process continues until the LLM

reaches a solution to the problem.

To see this in action, you need to write some code. In code Snippet 1 I am using the langchain framework for Python, together with Ve(cid:457)exAI (google-cloud-aiplatform) and the google-search-results pip packages.