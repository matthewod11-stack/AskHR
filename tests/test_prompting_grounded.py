from app.prompting_grounded import build_grounded_prompt


def test_build_grounded_prompt_smoke():
    chunks = [
        {
            "title": "Doc 1",
            "pages": "1",
            "content": "Alpha",
            "chunk_id": "chunk1",
            "source_path": "doc1.md",
        },
        {
            "title": "Doc 2",
            "pages": "2",
            "content": "Beta",
            "chunk_id": "chunk2",
            "source_path": "doc2.md",
        },
    ]
    question = "What is X?"
    persona = "You are a helpful assistant."
    prompt = build_grounded_prompt(question, chunks, persona=persona)
    assert isinstance(prompt, list)
    assert any(m["role"] == "system" for m in prompt)
    user_msgs = [m for m in prompt if m["role"] == "user"]
    assert user_msgs
    user_content = user_msgs[0]["content"]
    assert "[Source 1]" in user_content
    assert "[Source 2]" in user_content
    assert question in user_content
