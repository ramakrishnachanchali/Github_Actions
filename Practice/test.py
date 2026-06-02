from app import get_message

def test_message():
    assert "Hello GitHub Actions" in get_message()