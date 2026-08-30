import pytest
from convert import convert


def test_conversion():
    assert convert(1) == 149597870700
    assert convert(50) == 7479893535000


# to test the TypeError 
def test_error():
    # with is a context manager
    # to verify that a type error occurs with a string 
    # ie expect an error and if it occurs, test passes
    with pytest.raises(TypeError):
        convert("1")



# to test floating-point precision
# ie does the function correctly handle a floating-point value?
def test_float_conversion():
    # assert convert(0.001) == pytest.approx(149597870.691)


    # Expected: 149597870.691
    # Accept anything between:
    # 149597870.591  ← lower limit
    # and
    # 149597870.791  ← upper limit
    # abs means absolute tolerance.
    # you can adjust the tolerance to be exactly the way you want them to be
    assert convert(0.001) == pytest.approx(149597870.691, abs=0.1)
    # 149597870.700
    # -149597870.691
    # ----------------
    #     0.009


# .001 * 149597870700   "approximately"
#        ↓                  ↓
# 149,597,870.7  ≈  149,597,870.691
#        ↑                    ↑
#     actual                expected




# NUMBER MEMORY
# there are only a certain number of bits we can use to represent certain numbers in code
# Bits & Numbers in Python

# int → arbitrary precision (not limited to 32/64 bits)
# Uses as much memory as needed.

# float → typically 64 bits (IEEE 754)

# Check integer bit length:
# x = 255
# print(x.bit_length())  # 8

# 255 = 11111111 → 8 bits





# PYTEST
# you can put pytest on the terminal 
# pytest checks for test files automatically if i put in pytest on the terminal
# files named:
# test_*.py or *_test.py




# WITH STATEMENT
# `with` and pytest.raises()
#
# `with` is used with a context manager.
# A context manager manages what happens before, during, and after a block of code.
#
# Example of managing a resource:
#
# with open("file.txt") as file:
#     data = file.read()
#
# Here, Python handles opening and closing the file automatically.
#
#
# `pytest.raises()` is also a context manager, but it is used to test
# whether a specific exception is raised.
#
# Example:
# def test_error():
#     with pytest.raises(TypeError):
#         convert("1")
#
# This means:
# "Run convert('1') and verify that it raises a TypeError."
#
# If TypeError is raised       -> TEST PASSES
# If a different error occurs  -> TEST FAILS
# If no error occurs            -> TEST FAILS
#
#
# Key idea:
# with pytest.raises(TypeError):
#     ...
#
# Think of it as:
# "Run this block while pytest watches for a TypeError."
#
#
# Two common uses of `with`:
# with open(...):
#     -> Manage a resource (such as a file)
#
# with pytest.raises(...):
#     -> Test for an expected exception
#
# Both use Python's context manager mechanism.