from src.preprocessing import clean_text


def test_clean_text():
    message = "WIN a FREE Prize!!! Visit https://example.com"

    result = clean_text(message)

    assert result == "win a free prize visit"


def test_empty_text():
    result = clean_text("")

    assert result == ""


def test_non_string_input():
    result = clean_text(None)

    assert result == ""