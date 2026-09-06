"""
in a file called test_plates.py, implement four or more functions that collectively 
test your implementation of is_valid thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:
pytest test_plates.py
"""


import pytest
from plates import is_valid

# TESTS
# four or more functions needed
# test to see if plate starts with 2 letters
# test to see if plate has a max of 6 characters and min of 2 
# test to see if numbers are at the end of the plate and not in the middle
# test to see if there's periods, spaces, punctuations



# test to see if plate starts with 2 letters
def test_letters():
    assert is_valid("11AA22") == False
    assert is_valid("22AA33") == False
    # assert is_valid("BBBB22") == True



# test to see if plate has a max of 6 characters and a min of 2
def test_length():
    assert is_valid("11AA222") == False
    assert is_valid("1") == False
    # assert is_valid("BBBB22") == True



# test to see if numbers are at the end of the plate and not in the middle
def test_numbers():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA33A") == False



# test to see if the first numbers is zero
def test_zero_first_five():
    assert is_valid("000") == False
    assert is_valid("00033A") == False
    assert is_valid("0AA33A") == False




# test to see if there's periods, spaces, punctuations
def test_punctuation():
    assert is_valid("AA,SS,22") == False
    assert is_valid("AA SS 22") == False




