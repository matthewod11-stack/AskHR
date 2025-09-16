---
source_path: prompt.md
pages: n/a-n/a
chunk_id: d6eeba578eee4fc006e3ee348033580320fc1b1b
title: prompt
---
# Working with Schemas

Using structured JSON as an output is a great solution, as we've seen multiple times in this paper. But what about input? While JSON is excellent for structuring the output the LLM generates, it can also be incredibly useful for structuring the input you provide. This is where

JSON Schemas come into play. A JSON Schema de(cid:450)nes the expected structure and data

types of your JSON input. By providing a schema, you give the LLM a clear blueprint of the data it should expect, helping it focus its a(cid:459)ention on the relevant information and reducing

the risk of misinterpreting the input. Fu(cid:457)hermore, schemas can help establish relationships

between di(cid:441)erent pieces of data and even make the LLM "time-aware" by including date or

timestamp (cid:450)elds with speci(cid:450)c formats.

Here's a simple example:

Let's say you want to use an LLM to generate descriptions for products in an e-commerce

catalog. Instead of just providing a free-form text description of the product, you can use a

JSON schema to de(cid:450)ne the product's a(cid:459)ributes:

{ "type": "object", "properties": { "name": { "type": "string", "description": "Product name" }, "category": { "type": "string", "description": "Product category" }, "price": { "type": "number", "format": "float", "description": "Product price" }, "features": { "type": "array", "items": { "type": "string" }, "description": "Key features of the product" }, "release_date": { "type": "string", "format": "date", "description": "Date the product was released"} },
