from help_your_professor import average


class_3B = { "marine": 18, "jean": 15, "coline": 8, "luc": 9}
class_3C = { "quentin": 17, "julie": 15, "marc": 8, "stephanie": 13}


def test_average_class_3B():
    assert average(class_3B) == 12.5


def test_average_class_3C():
    assert average(class_3C) == 13.25


def test_average_inteiros():
    turma = {"ana": 10, "bob": 20, "carlos": 30}
    assert average(turma) == 20.0


def test_average_floats():
    turma = {"ana": 10.5, "bob": 19.5}
    assert average(turma) == 15.0


def test_average_um_aluno():
    turma = {"ana": 7}
    assert average(turma) == 7.0


def test_average_empty():
    turma = {}
    assert average(turma) == 0.0