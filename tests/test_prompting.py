from app.prompting import maybe_rewrite_query, build_user_prompt, build_rewrite_messages

def _echo_llm(msgs):
    # emulate a rewriter that returns the packed NEW_USER as-is
    text = msgs[-1]["content"]
    marker = "NEW_USER:"
    return text.split(marker, 1)[1].strip() if marker in text else text

def test_rewrite_and_prompt():
    last_user = "show attrition by department"
    last_assistant = "Attrition overall 12%. Eng 10%."
    new_user = "what about engineers only?"

    final_query = maybe_rewrite_query(last_user, last_assistant, new_user, _echo_llm)
    assert "engineer" in final_query.lower()

    prompt = build_user_prompt(final_query)
    assert "Chief People Officer" in prompt
    assert final_query in prompt
