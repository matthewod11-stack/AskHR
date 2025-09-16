---
source_path: building.md
pages: n/a-n/a
chunk_id: 629c2772fa717086269c8c551ec01b448f5a7f04
title: building
---
# OPTIMIZATION

Once you have run your evaluation tests, you can start to implement optimizations. Here are two improvement strategies that should be part of your toolkit.

- 1. Few shot examples This technique involves teaching Claude how to perform the task based on providing a few examples (i.e. more than one) as part of the prompt. Providing examples is one of the most effective ways to improve output quality, especially if you’re already following other prompting best practices.

- You can provide examples in context or use RAG for dynamic
