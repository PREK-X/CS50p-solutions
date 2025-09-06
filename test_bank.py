from bank import value

def test_value():
    
    assert value("Hello, World") == 0
    assert value("Hy, World") == 20
    assert value("World") == 100
