from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple

# A safe default if caller doesn't pass persona
DEFAULT_PERSONA = (
    "You are a pragmatic, fair Chief People Officer. You answer concisely and concretely, "
    "cite relevant policy/source passages, and flag compliance or legal risks without alarmism. "
    "Use plain language, structured bullets when helpful, and suggest next steps. "
    "If sources are weak or missing, say so and recommend how to strengthen them."
)

def _format_sources(top_chunks: List[Dict[str, Any]]) -> Tuple[str, List[Dict[str, str]]]:
    """
    Returns (formatted_text_for_prompt, citations_list).
    Each citation: {"chunk_id","source_path","title"}.
    """
    lines: List[str] = []
    citations: List[Dict[str, str]] = []
    for i, ch in enumerate(top_chunks, 1):
        title = str(ch.get("title") or "Untitled")
        path = str(ch.get("source_path") or "")
        snippet = str(ch.get("text") or "").strip()
        chunk_id = str(ch.get("chunk_id") or f"chunk-{i:03d}")
        # keep snippets compact
        if len(snippet) > 1200:
            snippet = snippet[:1200] + " ..."
        lines.append(f"[Source {i}: {title} — {path}]\n{snippet}\n")
        citations.append({"chunk_id": chunk_id, "source_path": path, "title": title})
    return ("\n".join(lines).strip(), citations)

def build_grounded_prompt(
    question: str,
    top_chunks: List[Dict[str, Any]],
    persona: Optional[str] = None,
    style_opts: Optional[Dict[str, Any]] = None,
) -> Tuple[List[Dict[str, str]], List[Dict[str, str]]]:
    """
    Returns (messages, citations).
    - messages: list of {"role": "system"|"user", "content": str}
    - citations: list of dicts aligning with the injected source order
    """
    persona_text = (persona or "").strip() or DEFAULT_PERSONA
    sources_text, citations = _format_sources(top_chunks or [])

    system_content = (
        persona_text
        + "\n\n"
        "Grounding rules:\n"
        "- Prefer the provided sources. Quote briefly when exact wording matters.\n"
        "- If the sources are insufficient, say so explicitly and provide a cautious best-effort answer.\n"
        "- Add clear, numbered citations like [1], [2] that map to the injected sources order.\n"
    )

    if sources_text:
        user_content = (
            f"Question:\n{question.strip()}\n\n"
            f"Context sources (use for grounding and citations):\n{sources_text}\n\n"
            "Respond directly to the question. When you use a source, include a bracketed number [n] "
            "that refers to the corresponding [Source n] above."
        )
    else:
        user_content = (
            f"Question:\n{question.strip()}\n\n"
            "No sources were provided. Answer cautiously; if policy is unclear, state assumptions and "
            "suggest how to find/ingest the relevant policy docs."
        )

    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]
    return messages, citations
