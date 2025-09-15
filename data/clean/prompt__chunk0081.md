# Prompt Engineering

If you set temperature to 0, top-K and top-P become irrelevant–the most probable

token becomes the next token predicted. If you set temperature extremely high (above 1–generally into the 10s), temperature becomes irrelevant and whatever tokens make

it through the top-K and/or top-P criteria are then randomly sampled to choose a next

predicted token.

If you set top-K to 1, temperature and top-P become irrelevant. Only one token passes the

top-K criteria, and that token is the next predicted token. If you set top-K extremely high,

like to the size of the LLM’s vocabulary, any token with a nonzero probability of being the

next token will meet the top-K criteria and none are selected out.

If you set top-P to 0 (or a very small value), most LLM sampling implementations will then

only consider the most probable token to meet the top-P criteria, making temperature and

top-K irrelevant. If you set top-P to 1, any token with a nonzero probability of being the

next token will meet the top-P criteria, and none are selected out.

As a general sta(cid:457)ing point, a temperature of .2, top-P of .95, and top-K of 30 will give you

relatively coherent results that can be creative but not excessively so. If you want especially

creative results, try sta(cid:457)ing with a temperature of .9, top-P of .99, and top-K of 40. And if you

want less creative results, try sta(cid:457)ing with a temperature of .1, top-P of .9, and top-K of 20.

Finally, if your task always has a single correct answer (e.g., answering a math problem), sta(cid:457)