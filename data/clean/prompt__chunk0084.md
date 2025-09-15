# Prompt Engineering

top-p se(cid:459)ings. This can occur at both low and high temperature se(cid:459)ings, though for di(cid:441)erent

reasons. At low temperatures, the model becomes overly deterministic, sticking rigidly to the highest probability path, which can lead to a loop if that path revisits previously generated

text. Conversely, at high temperatures, the model's output becomes excessively random, increasing the probability that a randomly chosen word or phrase will, by chance, lead back

to a prior state, creating a loop due to the vast number of available options. In both cases,

the model's sampling process gets "stuck," resulting in monotonous and unhelpful output

until the output window is (cid:450)lled. Solving this o(cid:454)en requires careful tinkering with temperature

and top-k/top-p values to (cid:450)nd the optimal balance between determinism and randomness.

Prompting techniques

LLMs are tuned to follow instructions and are trained on large amounts of data so they can

understand a prompt and generate an answer. But LLMs aren’t pe(cid:455)ect; the clearer your

prompt text, the be(cid:459)er it is for the LLM to predict the next likely text. Additionally, speci(cid:450)c

techniques that take advantage of how LLMs are trained and how LLMs work will help you get the relevant results from LLMs

Now that we understand what prompt engineering is and what it takes, let’s dive into some

examples of the most impo(cid:457)ant prompting techniques.

General prompting / zero shot

A zero-shot5 prompt is the simplest type of prompt. It only provides a description of a task

and some text for the LLM to get sta(cid:457)ed with. This input could be anything: a question, a

sta(cid:457) of a story, or instructions. The name zero-shot stands for ’no examples’.