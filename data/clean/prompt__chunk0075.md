# Top-K and top-P

Top-K and top-P (also known as nucleus sampling)4 are two sampling se(cid:459)ings used in LLMs

to restrict the predicted next token to come from tokens with the top predicted probabilities.

Like temperature, these sampling se(cid:459)ings control the randomness and diversity of

generated text.

- Top-K sampling selects the top K most likely tokens from the model’s predicted

distribution. The higher top-K, the more creative and varied the model’s output; the

lower top-K, the more restive and factual the model’s output. A top-K of 1 is equivalent to