from functions_everywhere import shrink, enlarge

def test_shrink() -> None:
    assert shrink("abcdefghi") == "abcdefgh"
    assert shrink("123456789") == "12345678"
    assert shrink("eight888") == "eight888"

def test_enlarge() -> None:
    assert enlarge("lol") == "lolZZZZZ"
    assert enlarge("1234567") == "1234567Z"
    assert enlarge("") == "ZZZZZZZZ"