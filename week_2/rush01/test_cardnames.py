from cardnames import toupper, fit_pinto, fit_junior, fit_filho, fit_neto, fit_prep, name_chop


def test_toupper():
    given = "matheus vieira"
    expected = "MATHEUS VIEIRA"
    result = toupper(given)
    assert expected == result
    
def test_fit_junior():
    given = "MATHEUS JUNIOR"
    expected = "MATHEUS JR"
    result = fit_junior(given)
    assert expected == result
    
    given = "MATHEUS FILHO"
    expected = "MATHEUS FL"
    result = fit_filho(given)
    assert expected == result
    
    given = "MATHEUS NETO"
    expected = "MATHEUS NT"
    result = fit_neto(given)
    assert expected == result
    
def test_fit_pinto():
    given = "MATHEUS PINTO"
    expected = "MATHEUS P"
    result = fit_pinto(given)
    assert expected == result

def test_fit_prep():
    given = "MATHEUS DOS SANTOS"
    expected = "MATHEUS SANTOS"
    result = fit_prep(given)
    assert expected == result
    
def test_name_size():
    given = "MATHEUS FEREIRA DOS SANTOS PINTO NETO DAS NOBREGA DA SILVA ALBUQUERQUE DOSVALODS NOGUEIRA"
    expected = False
    result = name_chop(given)
    assert result == expected
    
    given = "JHULIA CARVALHO"
    expected = True
    result = name_chop(given)
    assert result == expected
    
def test_size26():
    given = "MATHEUS FEREIRA DOS SANTOS PINTO NETO DAS NOBREGA DA SILVA ALBUQUERQUE DOSVALODS NOGUEIRA"
    expected = "MATHEUS FEREIRA DOS SANTOS"
    result = name_chop(given)
    assert result == expected
    
def test_chop():
    given = "MATHEUS FEREIRA DOS SANTOS PRADO NOGUEIRA DA SILVA SANTOS"
    expected = "MATHEUS SANTOS"
    result = name_chop(given)
    assert result == expected
    