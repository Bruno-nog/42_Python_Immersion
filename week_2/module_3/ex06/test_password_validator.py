import pytest
from password_validator import is_valid_password

# def test_uppercase():
#     given = "senha12345!"
#     result = is_valid_password(given)
#     assert result is False

@pytest.mark.parametrize("password, expected", [
    ("Sh0rt!", False),
    ("JKDNsddfghfdhgshgksfdfjf1@", False),
    ("WithoutDigit@", False),
    ("WSpecialC#", False),
    ("123WUPPER%", False),
    ("4398lower*", False),
    ("White sp4ce#", False)
])

def test_is_valid_password(password, expected):
    assert is_valid_password(password) == expected