---
source_path: prompt.md
pages: n/a-n/a
chunk_id: cb00775d49b2709a6163ec9246201e05728aad80
title: prompt
---
# Prompt Engineering

We recommend creating a Google Sheet with Table 21 as a template. The advantages of this approach are that you have a complete record when you inevitably have to revisit your

prompting work–either to pick it up in the future (you’d be surprised how much you can

forget a(cid:454)er just a sho(cid:457) break), to test prompt pe(cid:455)ormance on di(cid:441)erent versions of a model,

and to help debug future errors.

Beyond the (cid:450)elds in this table, it’s also helpful to track the version of the prompt (iteration),

a (cid:450)eld to capture if the result was OK/NOT OK/SOMETIMES OK, and a (cid:450)eld to capture

feedback. If you’re lucky enough to be using Ve(cid:457)ex AI Studio, save your prompts (using the same name and version as listed in your documentation) and track the hyperlink to the saved

prompt in the table. This way, you’re always one click away from re-running your prompts.

When working on a retrieval augmented generation system, you should also capture the

speci(cid:450)c aspects of the RAG system that impact what content was inse(cid:457)ed into the prompt,

including the query, chunk se(cid:459)ings, chunk output, and other information.

Once you feel the prompt is close to pe(cid:455)ect, take it to your project codebase. And in the

codebase, save prompts in a separate (cid:450)le from code, so it’s easier to maintain. Finally, ideally

your prompts are pa(cid:457) of an operationalized system, and as a prompt engineer you should rely on automated tests and evaluation procedures to understand how well your prompt
