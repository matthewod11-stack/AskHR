# Evaluating the Final Response

The final response evaluation boils down to a simple question: Does your agent achieve its

goals? You can define custom success criteria, tailored to your specific needs, to measure

this. For example, you could assess whether a retail chatbot accurately answers product

questions, or whether a research agent effectively summarizes findings with the appropriate

tone and style. To automate this process, you can use autorater. An autorater is an LLM

that acts as a judge. Given the input prompts and the generated response, it mirrors

human evaluation by assessing the response against a set of user-provided criteria. For

this evaluation to work, it is crucial to consider that given the absence of ground-truth, you

need to be very precise in defining your evaluation criteria, as this is the core of what your

evaluation is looking at. You find a number of predefined criteria in various libraries, treat

them as a starting point and tweak them to provide your definition of good.

20