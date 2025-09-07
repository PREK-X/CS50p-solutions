from plates import is_valid

def test_is_valid():

    assert is_valid("12kra") == False
    assert is_valid("krakengo") == False
    assert is_valid("kra12k") == False
    assert is_valid("kra ke") == False
    assert is_valid("kra012") == False
    assert is_valid("k") == False
    assert is_valid("123kra") == False
    assert is_valid(",,. k") == False
    assert is_valid("123456") == False
