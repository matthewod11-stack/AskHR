"""
Prompting utilities for HR Ask Local RAG system.
Persona: pragmatic, compliance-aware Chief People Officer.
"""
from typing import List, Dict

def build_system_prompt() -> str:
    """
    Returns the system prompt for the LLM, describing the persona and requirements.
    """
    return (
        "You are a pragmatic, compliance-aware Chief People Officer. "
        "Give succinct, actionable steps and practical examples. "
        "Be explicit when the context doesn’t contain an answer. "
        "Use inline citations like [1], [2] that refer to provided context blocks. "
        "Avoid legal/medical advice disclaimers unless relevant."
    )

def format_context(chunks: List[Dict], max_chars: int = 1200) -> str:
    """
    Formats retrieved context chunks for the LLM prompt.
    Each block is numbered [i], includes SOURCE, and is clipped to max_chars.
    """
    blocks = []
    for i, chunk in enumerate(chunks, 1):
        text = chunk.get("text", "")[:max_chars]
        source = chunk.get("meta", {}).get("source", "")
        blocks.append(f"[{i}] {text}\nSOURCE: {source}")
    return "\n\n".join(blocks)

def build_user_prompt(question: str, chunks: List[Dict]) -> str:
    """
    Builds the user prompt for the LLM, including the question and formatted context.
    Requests output structure: summary, actionable steps, risks/caveats, citations.
    """
    context_str = format_context(chunks)
    return (
        f"Context blocks:\n{context_str}\n\n"
        f"Question: {question}\n\n"
        "Please answer using the provided context when relevant. "
        "Structure your response as follows:\n"
        "- Brief summary (1–2 sentences)\n"
        "- Actionable steps (bullets)\n"
        "- Risks / caveats (bullets)\n"
        "- Inline citations like [1], [3] referring to context blocks.\n"
        "If the context does not contain an answer, say so explicitly."
    )# app/prompting.py
from typing import List, Dict

def build_system_prompt() -> str:
    return (
        "You are a pragmatic, compliance-aware Chief People Officer. "
        "Answer succinctly with clear, actionable steps. "
        "Prefer policies, first principles, and practical examples. "
        "If the context lacks an answer, say what else you’d need. "
        "Always cite sources inline with bracketed indices like [1], [2] "
        "that correspond to the provided context blocks."
    )

def format_context(chunks: List[Dict], max_chars: int = 1200) -> str:
    """
    chunks: list of dicts {text, meta, distance}. We number them [1], [2]…
    We clip each chunk for prompt budget hygiene.
    """
    blocks = []
    for i, ch in enumerate(chunks, start=1):
        src = ch["meta"].get("source", "unknown")
        text = ch["text"][:max_chars]
        blocks.append(f"[{i}] SOURCE: {src}\n{text}")
    return "\n\n".join(blocks)

def build_user_prompt(question: str, chunks: List[Dict]) -> str:
    ctx = format_context(chunks)
    return (
        f"User question:\n{question}\n\n"
        "Use only the context blocks below when relevant. "
        "If you infer, label it clearly. "
        "Cite with the block index like [1], [2].\n\n"
        f"Context blocks:\n{ctx}\n\n"
        "Now write your answer as:\n"
        "- Brief summary (1–2 sentences)\n"
        "- Actionable steps (bullets)\n"
        "- Risks / caveats (bullets)\n"
        "- If applicable, a short policy template or outline\n"
        "Include citations like [1], [3] next to claims."
    )
