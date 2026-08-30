

import pytest

from twttr import shorten
import twttr




# pytest counts test functions, not individual assert statements,
# so you'll see "1 passed" when you run pytest in terminal


def test_shorten():
    assert shorten("water") == "wtr"
    assert shorten("pembroke") == "pmbrk"
    assert shorten("yard") == "yrd"




# to test try except block
def test_error():
    with pytest.raises(ValueError):
        shorten("555")




