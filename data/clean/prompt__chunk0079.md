---
source_path: prompt.md
pages: n/a-n/a
chunk_id: 385b24f06bae4835dd17a406f3866de72727ee18
title: prompt
---
# Prompt Engineering

- Top-P sampling selects the top tokens whose cumulative probability does not exceed

a ce(cid:457)ain value (P). Values for P range from 0 (greedy decoding) to 1 (all tokens in the

LLM’s vocabulary).

The best way to choose between top-K and top-P is to experiment with both methods (or

both together) and see which one produces the results you are looking for.

Pu(cid:350)ing it all together

Choosing between top-K, top-P, temperature, and the number of tokens to generate,

depends on the speci(cid:450)c application and desired outcome, and the se(cid:459)ings all impact one

another. It’s also impo(cid:457)ant to make sure you understand how your chosen model combines

the di(cid:441)erent sampling se(cid:459)ings together.

If temperature, top-K, and top-P are all available (as in Ve(cid:457)ex Studio), tokens that meet both the top-K and top-P criteria are candidates for the next predicted token, and then

temperature is applied to sample from the tokens that passed the top-K and top-P criteria. If

only top-K or top-P is available, the behavior is the same but only the one top-K or P se(cid:459)ing

is used.

If temperature is not available, whatever tokens meet the top-K and/or top-P criteria are then

randomly selected from to produce a single next predicted token.

At extreme se(cid:459)ings of one sampling con(cid:450)guration value, that one sampling se(cid:459)ing either
