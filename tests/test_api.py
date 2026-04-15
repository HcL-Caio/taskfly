from src.api import get_advice


def test_get_advice():
    advice = get_advice()
    assert isinstance(advice, str)
    assert len(advice) > 0
