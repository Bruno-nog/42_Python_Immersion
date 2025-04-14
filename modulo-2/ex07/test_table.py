import pytest
from table import gen_table

def test_table() -> None:
    given = gen_table(9)
    expected = [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
    assert expected == given
