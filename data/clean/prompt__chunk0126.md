# System, contextual and role prompting

System, contextual and role prompting are all techniques used to guide how LLMs generate

text, but they focus on di(cid:441)erent aspects:

- System prompting sets the overall context and purpose for the language model. It

de(cid:450)nes the ‘big picture’ of what the model should be doing, like translating a language,

classifying a review etc.

- Contextual prompting provides speci(cid:450)c details or background information relevant to

the current conversation or task. It helps the model to understand the nuances of what’s

being asked and tailor the response accordingly.

- Role prompting assigns a speci(cid:450)c character or identity for the language model to adopt. This helps the model generate responses that are consistent with the assigned role and its associated knowledge and behavior.

There can be considerable overlap between system, contextual, and role prompting. E.g. a

prompt that assigns a role to the system, can also have a context.