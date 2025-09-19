import re
from typing import Callable, Dict, List, Optional

# ---------------------------------------------------------------------------
# Answering model: system & user prompts
# ---------------------------------------------------------------------------


def build_system_prompt() -> str:
    """
    System prompt for the answering model (not the rewriter).
    Sets the persona and output rules.
    """
    return (
        "You are a pragmatic, compliance-aware Chief People Officer (CPO) who advises startups.\n"
        "\n"
        "Rules:\n"
        "• Be concise and actionable; prefer bullet points and short checklists.\n"
        "• Ground non-trivial claims in the retrieved context; cite sources inline like [1], [2].\n"
        "• If the context is missing or contradictory, say: "
        '"Not enough evidence in the provided sources." Then list what else is needed.\n'
        "• Never fabricate laws, dates, or numbers. Flag jurisdictional differences (e.g., CA vs. federal) when relevant.\n"
        "• You are not legal counsel; include a brief compliance note when giving policy guidance.\n"
        "• For analytics answers, state key filters/assumptions (timeframe, population, exclusions).\n"
        "• If the user asks for templates or policies, output clean, copyable sections with placeholders where needed.\n"
        "• If the user explicitly asks for code/SQL, output only code fenced in triple backticks.\n"
    )


def build_user_prompt(query: str) -> str:
    """
    Build the final prompt text combining the system persona and the user question.
    This mirrors how callers typically construct prompts for single-shot calls
    and keeps compatibility with existing tests expecting the persona inline.
    """
    persona = build_system_prompt().strip()
    prompt = f"{persona}\n\nUser question:\n{query.strip()}\n"
    return prompt


# ---------------------------------------------------------------------------
# Rewriter: cautious multi-turn query rewriting (uses last Q/A only)

# System prompt used by the lightweight rewriter (NOT the answering model).
# Keeps rewrites conservative: preserve user intent, avoid inventing numbers/dates,
# emit a single-line rewritten query with no formatting or code fences.
REWRITE_SYSTEM_PROMPT = (
    "You are a careful query rewriter for an HR analytics assistant. "
    "When the new user message depends on the prior Q/A, rewrite it into a standalone query. "
    "Do not invent data; keep the user’s nouns, filters, and timeframes. "
    "Output one short line, no code blocks, no quotes."
)

# Few-shot pairs keep the rewriter style tight and conservative
REWRITE_FEW_SHOTS: List[Dict[str, str]] = [
    {
        "role": "user",
        "content": (
            "LAST_USER: show attrition by department\n"
            "LAST_ASSISTANT: Attrition is 12% overall. Sales 18%, Eng 10%, Ops 8%.\n"
            "NEW_USER: what about engineers only?"
        ),
    },
    {"role": "assistant", "content": "show attrition for engineers only by department"},
    {
        "role": "user",
        "content": (
            "LAST_USER: show headcount trends for 2023\n"
            "LAST_ASSISTANT: Grew from 60 to 90 employees.\n"
            "NEW_USER: filter to product team"
        ),
    },
    {"role": "assistant", "content": "show headcount trends for the product team in 2023"},
    {
        "role": "user",
        "content": (
            "LAST_USER: how do performance reviews work?\n"
            "LAST_ASSISTANT: Annual in Q4 with calibration.\n"
            "NEW_USER: and compensation?"
        ),
    },
    {
        "role": "assistant",
        "content": "how does compensation work relative to the performance review cycle?",
    },
    {
        "role": "user",
        "content": (
            "LAST_USER: show DEI metrics for Q2 2024\n"
            "LAST_ASSISTANT: Overall improved female leadership +3%.\n"
            "NEW_USER: just ICs"
        ),
    },
    {"role": "assistant", "content": "show DEI metrics for individual contributors in Q2 2024"},
    {
        "role": "user",
        "content": (
            "LAST_USER: open reqs by org and seniority\n"
            "LAST_ASSISTANT: 14 total, Eng 8 (3 Sr+), Sales 4 (1 Sr+), Ops 2.\n"
            "NEW_USER: include contractors"
        ),
    },
    {
        "role": "assistant",
        "content": "show open roles (including contractors) by org and seniority",
    },
]

# ----------------------- rewriter helpers ------------------------------------

_REFERENTIAL_SUBSTRINGS = [
    "what about",
    "how about",
    "just ",
    "only",
    "instead",
    "also",
    "same",
    "that too",
    "include",
    "exclude",
    "filter",
    "narrow",
    "broaden",
    "except",
    "w/o",
    "w/out",
    "remove",
    "vs ",
    "versus ",
]
_REFERENTIAL_PREFIXES = ("and ", "but ", "also ", "only ", "just ", "then ", "ok, ")

_CODE_LIKE_PAT = re.compile(
    r"```|{[\s\S]*}|\[[\s\S]*]|SELECT\s+|FROM\s+|WHERE\s+|WITH\s+\(|^#|\bdef\s+\w+\(|\bclass\s+\w+\(",
    re.IGNORECASE,
)
_WHITESPACE_PAT = re.compile(r"\s+")


def _normalize_whitespace(s: str) -> str:
    return _WHITESPACE_PAT.sub(" ", s or "").strip()


def _clamp(s: str, max_chars: int) -> str:
    if s and len(s) > max_chars:
        return s[:max_chars]
    return s


def _looks_code_like(s: str) -> bool:
    # Avoid rewriting code/JSON/SQL blocks or dev commands.
    return bool(_CODE_LIKE_PAT.search(s or ""))


def _looks_referential(text: str) -> bool:
    # Heuristic to decide if the input likely depends on prior context.
    if not text:
        return False
    t = text.lower().strip()
    if len(t) <= 40:
        return True
    if t.startswith(_REFERENTIAL_PREFIXES):
        return True
    if any(cue in t for cue in _REFERENTIAL_SUBSTRINGS):
        return True
    if t.startswith(("what ", "how ", "which ")) and (" only" in t or " instead" in t):
        return True
    return False


def _pack_context(last_user: str, last_assistant: str, new_user: str) -> str:
    # Clamp context to reduce prompt bloat and leakage.
    last_user_c = _clamp(_normalize_whitespace(last_user), 600)
    last_assistant_c = _clamp(_normalize_whitespace(last_assistant), 600)
    new_user_c = _clamp(_normalize_whitespace(new_user), 400)
    return (
        f"LAST_USER: {last_user_c}\n"
        f"LAST_ASSISTANT: {last_assistant_c}\n"
        f"NEW_USER: {new_user_c}"
    )


# ----------------------- public rewriter API ---------------------------------


def build_rewrite_messages(
    last_user: Optional[str],
    last_assistant: Optional[str],
    new_user: str,
) -> List[Dict[str, str]]:
    # Compose a messages array for chat-style LLMs implementing the rewriter.
    # Use directly with your LLM client (e.g., /chat/completions).
    if not last_user or not last_assistant:
        return [
            {"role": "system", "content": REWRITE_SYSTEM_PROMPT},
            *REWRITE_FEW_SHOTS,
            {"role": "user", "content": _normalize_whitespace(new_user)},
        ]
    packed = _pack_context(last_user, last_assistant, new_user)
    return [
        {"role": "system", "content": REWRITE_SYSTEM_PROMPT},
        *REWRITE_FEW_SHOTS,
        {"role": "user", "content": packed},
    ]


def maybe_rewrite_query(
    last_user: Optional[str],
    last_assistant: Optional[str],
    new_user: str,
    llm_call_fn: Callable[[List[Dict[str, str]]], str],
) -> str:
    # Decide if rewrite is needed; if yes, call the model and return the final query.
    # - If the new_user looks referential/elliptical, rewrite using last Q/A.
    # - Otherwise return new_user unchanged.
    # llm_call_fn(messages) -> str should return the model's text (final query only).
    new_user_norm = _normalize_whitespace(new_user)
    if not (last_user and last_assistant):
        return new_user_norm
    if _looks_code_like(new_user_norm):
        return new_user_norm
    if not _looks_referential(new_user_norm):
        return new_user_norm
    messages = build_rewrite_messages(last_user, last_assistant, new_user_norm)
    try:
        rewritten = (llm_call_fn(messages) or "").strip()
    except Exception:
        return new_user_norm
    if not rewritten or _looks_code_like(rewritten):
        return new_user_norm
    rewritten_norm = _normalize_whitespace(rewritten)
    if rewritten_norm.lower() == new_user_norm.lower():
        return new_user_norm
    return rewritten_norm


# Optional: make exported surface explicit
__all__ = [
    "build_system_prompt",
    "build_user_prompt",
    "REWRITE_SYSTEM_PROMPT",
    "REWRITE_FEW_SHOTS",
    "build_rewrite_messages",
    "maybe_rewrite_query",
]

if __name__ == "__main__":
    print("This module is not used by runtime. Retained for future rewrite-debug work.")
# TODO(rewrite-debug): This module is retained for a future rewrite-debug endpoint; not used by runtime.
