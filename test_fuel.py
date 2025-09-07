import pytest
from fuel import convert
from fuel import gauge


def test_convert():

    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("4/4") == 100
    assert convert("0/4") == 0
    with pytest.raises(ValueError):
        convert("-1/-1")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():

    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"


