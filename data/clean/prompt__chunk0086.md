# Prompt Engineering

Let’s use Ve(cid:457)ex AI Studio (for Language) in Ve(cid:457)ex AI,6 which provides a playground to test

prompts. In Table 1, you will see an example zero-shot prompt to classify movie reviews.

The table format as used below is a great way of documenting prompts. Your prompts will

likely go through many iterations before they end up in a codebase, so it’s impo(cid:457)ant to keep

track of your prompt engineering work in a disciplined, structured way. More on this table

format, the impo(cid:457)ance of tracking prompt engineering work, and the prompt development process is in the Best Practices section later in this chapter (“Document the various prompt

a(cid:459)empts”).

The model temperature should be set to a low number, since no creativity is needed, and we

use the gemini-pro default top-K and top-P values, which e(cid:441)ectively disable both se(cid:459)ings

(see ‘LLM Output Con(cid:450)guration’ above). Pay a(cid:459)ention to the generated output. The words disturbing and masterpiece should make the prediction a li(cid:459)le more complicated, as both

words are used in the same sentence.