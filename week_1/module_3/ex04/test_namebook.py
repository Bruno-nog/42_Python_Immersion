from your_namebook import list_of_names

def test_list_of_names_normal() -> None:
    persons = {
        "jean": "valjean",
        "grace": "hopper"
    }
    assert list_of_names(persons) == ["Jean Valjean", "Grace Hopper"]

def test_list_of_names_empty() -> None:
    assert list_of_names({}) == []

def test_list_of_names_case_mix() -> None:
    persons = {
        "JOHN": "doe",
        "mary": "SMITH"
    }
    assert list_of_names(persons) == ["John Doe", "Mary Smith"]
