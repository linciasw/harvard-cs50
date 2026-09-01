# test three functions
# 


import pytest
from bank import value


def test_value():
    assert value("hello") == 0
    assert value("hat") == 20
    assert value("cat") == 100




def test_number():
    with pytest.raises(ValueError):
        value(555)







