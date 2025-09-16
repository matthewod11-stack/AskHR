---
source_path: prompt.md
pages: n/a-n/a
chunk_id: 08a05caf0ad7ed56335b8ce4f9dfd1e0f4d371c5
title: prompt
---
# JSON Repair

While returning data in JSON format o(cid:441)ers numerous advantages, it's not without its

drawbacks. The structured nature of JSON, while bene(cid:450)cial for parsing and use in

applications, requires signi(cid:450)cantly more tokens than plain text, leading to increased

processing time and higher costs. Fu(cid:457)hermore, JSON's verbosity can easily consume the entire output window, becoming especially problematic when the generation is abruptly cut

o(cid:441) due to token limits. This truncation o(cid:454)en results in invalid JSON, missing crucial closing braces or brackets, rendering the output unusable. Fo(cid:457)unately, tools like the json-repair

library (available on PyPI) can be invaluable in these situations. This library intelligently

a(cid:459)empts to automatically (cid:450)x incomplete or malformed JSON objects, making it a crucial ally when working with LLM-generated JSON, especially when dealing with potential
