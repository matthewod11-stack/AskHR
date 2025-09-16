import pytest
from eval.utils import score_keywords, normalize

def test_normalize_basic():
    assert normalize('Hello  World!') == 'hello world!'
    assert normalize('  Foo\nBar\tBaz  ') == 'foo bar baz'
    assert normalize('A.B,C') == 'a.b,c'

def test_score_keywords_all_present():
    answer = 'policy duration leave'
    keywords = ['policy', 'duration', 'leave']
    assert score_keywords(answer, keywords) == 100.0

def test_score_keywords_partial_present():
    answer = 'policy duration'
    keywords = ['policy', 'duration', 'leave']
    assert score_keywords(answer, keywords) == pytest.approx(66.666, 0.1)

def test_score_keywords_none_present():
    answer = 'foo bar'
    keywords = ['policy', 'duration', 'leave']
    assert score_keywords(answer, keywords) == 0.0

def test_score_keywords_punct_whitespace():
    answer = 'policy, duration; leave.'
    keywords = ['policy', 'duration', 'leave']
    assert score_keywords(answer, keywords) == 100.0
