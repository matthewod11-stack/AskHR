---
source_path: prompt.md
pages: n/a-n/a
chunk_id: 6d37ea48e82b878a8f8448d19daae5b4a3143e5d
title: prompt
---
# (cid:450)nal answer.

With CoT and self-consistency you need to be able to extract the (cid:450)nal answer from your

prompt, separated from the reasoning.

For CoT prompting, set the temperature to 0.

Chain of thought prompting is based on greedy decoding, predicting the next word in a

sequence based on the highest probability assigned by the language model. Generally

speaking, when using reasoning, to come up with the (cid:450)nal answer, there’s likely one single

correct answer. Therefore the temperature should always set to 0.
