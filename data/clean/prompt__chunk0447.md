---
source_path: prompt.md
pages: n/a-n/a
chunk_id: 0389d551154fd2758dba8ad3c54bd3b6287fe22a
title: prompt
---
# Experiment with output formats

Besides the prompt input format, consider experimenting with the output format. For non- creative tasks like extracting, selecting, parsing, ordering, ranking, or categorizing data try

having your output returned in a structured format like JSON or XML.

There are some bene(cid:450)ts in returning JSON objects from a prompt that extracts data. In

a real-world application I don’t need to manually create this JSON format, I can already

return the data in a so(cid:457)ed order (very handy when working with datetime objects), but most

impo(cid:457)antly, by prompting for a JSON format it forces the model to create a structure and
