from transform import square_even_numbers

def test_even_squares() -> None:
    assert square_even_numbers([1, 2, 3, 4, 5]) == [4, 16]

def test_empty() -> None:
    assert square_even_numbers([]) == []

def test_all_odd() -> None:
    assert square_even_numbers([1, 3, 5, 7]) == []

def test_all_even() -> None:
    assert square_even_numbers([2, 4, 6]) == [4, 16, 36]

def test_negatives() -> None:
    assert square_even_numbers([-2, -3, -4]) == [4, 16]
