# test three functions
# 


import pytest
from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello, there") == 0
    assert value("hello, world") == 0




def test_h():
    assert value("hat") == 20
    assert value("hey") == 20
    assert value("hi") == 20




def test_other():
    assert value("cat") == 100
    assert value("good morning") == 100




def test_number():
    with pytest.raises(ValueError):
        value(555)










