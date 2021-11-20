from calculations import add, add_string, divide, multiply, subtract

def test_add():
    assert add(2,3) == 5
    assert add(10,10) == 20

def test_add_negative():
    assert add(-2,3) == 1
    assert add(10,-10) == 0

def test_subtract():
    assert subtract(2,3) == -1
    assert subtract(10,10) == 0

def test_divide():
    assert divide(10,2) == 5
    assert divide(10,10) == 1

def test_multiply():
    assert multiply(2,3) == 6
    assert multiply(10,10) == 100

def test_add_string_negative():
    assert add_string('-2','3') == 1
    assert add_string('10','-10') == 0

def test_add_string():
    assert add_string('2','3') == 5
    assert add_string('10','10') == 20
