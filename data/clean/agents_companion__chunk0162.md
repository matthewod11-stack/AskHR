# Better Search, Better RAG

Almost all RAG approaches require a search engine to index and retrieve relevant data. The

introduction of agents allows for refinement of query, filtering, ranking, and the final answer.

Agentic RAG agents are executing several searches to retrieve information.

For developers who are trying to optimize existing RAG implementations, it is usually most

valuable to improve search results (measured in recall) prior to introducing agents. Some of

the main techniques to improve search performance are:

- Parse source documents and chunk them: Vertex AI Layout Parser can handle complex

document layouts, embedded tables, and embedded images like charts, and uses a

semantic chunker to keep chunks on topic with a hierarchy of headings.

- Add metadata to your chunks: synonyms, keywords, authors, dates, tags and categories

allow your searches to boost, bury, and filter; these allow your users or your agents more