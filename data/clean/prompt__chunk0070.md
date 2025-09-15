# higher costs.

Sampling controls

LLMs do not formally predict a single token. Rather, LLMs predict probabilities for what the

next token could be, with each token in the LLM’s vocabulary ge(cid:459)ing a probability. Those

token probabilities are then sampled to determine what the next produced token will be.

Temperature, top-K, and top-P are the most common con(cid:450)guration se(cid:459)ings that determine

how predicted token probabilities are processed to choose a single output token.