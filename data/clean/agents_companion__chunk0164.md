---
source_path: agents_companion.md
pages: n/a-n/a
chunk_id: 0e68d0dadaaa7965ada63efd5841f23876bc0e4c
title: agents_companion
---
# control over search results.

- Fine tune the embedding model or add a search adaptor which changes embedding

space: these allow the searchable index of vectors to represent your domain better than a

general purpose embedding model.

- A faster vector database can improve search quality: to search embeddings, you must

make a tradeoff between speed and accuracy, upgrading to an ultra-fast Vertex AI

Vector Search can improve both latency and quality

- Use a ranker: vector searches are fast but approximate, they should return dozens or

hundreds of results which need to be re-ranked by a more sophisticated system to ensure

the top few results are the most relevant or best answer.

Implement check grounding: as a safeguard on grounded generation, you can ensure

each phrase is actually citable by retrieved chunks.

36

Figure 10: A diagram of common RAG and search components, showing Vertex AI Search26, search builder APIs27, and RAG Engine.28

Vertex AI Search26 is a powerful search engine providing Google quality search for your

data and can be used with any RAG or Agentic RAG implementation. Each of the above

components is automatically available within Vertex AI Search, without any development

time at all. For developers who want to build their own search engine, each of the above

components is exposed as a standalone API27, and RAG Engine28 can orchestrate the whole
