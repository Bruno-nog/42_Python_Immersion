from person import Person

def test_person_initialization():
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30

def test_person_none():
    p = Person("", None)
    assert p.name == ""
    assert p.age == None