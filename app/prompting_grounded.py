from typing import List, Dict


def build_grounded_prompt(question: str, top_chunks: List[Dict], persona: str) -> List[Dict]:
    """
    Build a prompt for the LLM that grounds the answer in retrieved context chunks.
    Each chunk is formatted for citation and clarity.
    Returns a list of messages for chat completion.
    """
    # Format context from chunks
    context_parts = []
    for i, chunk in enumerate(top_chunks, 1):
        title = chunk.get("title", "Untitled")
        pages = chunk.get("pages", "")
        content = chunk.get("content", "")
        context_parts.append(f"[Source {i}] {title} (pp. {pages})\n{content}")
    context_str = "\n\n".join(context_parts)
    # User message: context + question
    if context_str:
        user_msg = f"Context:\n{context_str}\n\nQuestion: {question}"
    else:
        user_msg = f"Question: {question}"
    return [{"role": "system", "content": persona}, {"role": "user", "content": user_msg}]
