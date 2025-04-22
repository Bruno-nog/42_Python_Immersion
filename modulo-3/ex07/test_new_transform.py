from new_transform import square_even_nbrs_new_trans

def test_only_evens() -> None:
    assert square_even_nbrs_new_trans([2, 4, 6]) == [4, 16, 36]

def test_mixed_numbers() -> None:
    assert square_even_nbrs_new_trans([1, 2, 3, 4, 5]) == [4, 16]

def test_only_odds() -> None:
    assert square_even_nbrs_new_trans([1, 3, 5]) == []

def test_empty_list() -> None:
    assert square_even_nbrs_new_trans([]) == []

def test_negative_evens() -> None:
    assert square_even_nbrs_new_trans([-2, -4]) == [4, 16]
