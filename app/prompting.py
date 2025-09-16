from typing import Dict, List

def build_system_prompt() -> str:
    return (
        "You are a pragmatic, compliance-aware Chief People Officer. "
        "Always answer ONLY in compact bullet points—no paragraphs or narrative text. "
        "Structure every answer in three sections: Summary, Actions, Risks/Caveats. "
        "Each section must be a bullet list (•), with each bullet concise and actionable. "
        "Include brief risks/caveats when relevant. "
        "If the provided context lacks the answer, say what additional info is needed. "
        "Cite sources inline like [1], [2] next to the bullets they support. "
        "Do not use any paragraphs or prose—bullets only."
    )

def format_context(chunks: List[Dict], max_chars: int = 1200) -> str:
    blocks=[]
    for i,ch in enumerate(chunks,1):
        src = ch.get("meta",{}).get("source_path","unknown")
        blocks.append(f"[{i}] SOURCE: {src}\n{ch.get('text','')[:max_chars]}")
    return "\n\n".join(blocks)

def build_user_prompt(question: str, chunks: List[Dict], grounded_only: bool = False) -> str:
    ctx = format_context(chunks)
    grounding = (
        "Use ONLY the provided context below. If it does not contain the answer, say so and list the missing inputs."
        if grounded_only
        else "Prefer the provided context. If you infer beyond it, label those bullets as 'Inference'."
    )
    return (
        f"Question:\n{question}\n\n"
        f"{grounding}\n"
        "Your answer MUST be strictly formatted as three bullet sections—no paragraphs or narrative text:\n"
        "- Summary:\n  • (1–2 concise bullets, each with inline citations [1], [2] as needed)\n"
        "- Actions:\n  • (3–7 imperative bullets, each with inline citations [1], [2] as needed)\n"
        "- Risks/Caveats:\n  • (1–3 concise bullets, each with inline citations [1], [2] as needed; omit if none)\n"
        "Do NOT use any paragraphs or prose. Every bullet must cite supporting context inline as [1], [2], etc.\n\n"
        f"Context blocks:\n{ctx}\n"
    )