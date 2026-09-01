# think of another test to check 
# test string input?

import pytest

from twttr import shorten
from twttr import get_word




# pytest counts test functions, not individual assert statements,
# so you'll see "1 passed" when you run pytest in terminal


def test_shorten():
    assert shorten("water") == "wtr"
    assert shorten("pembroke") == "pmbrk"
    assert shorten("yard") == "yrd"


def test_number():
    with pytest.raises(TypeError):
        shorten(555)








# to test try except block
# def test_get_word(monkeypatch):
#     def fake_input(prompt):
#         return "555"

#     monkeypatch.setattr("builtins.input", fake_input)
#     with pytest.raises(ValueError):
#         get_word()




