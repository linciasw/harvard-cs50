# FROM LECTURE
# REACHED 22:28, PYTEST

# testing is writing more code to test the code you've written as below

# we changed the * in calculator.py to a + but 
# only the "3 squared was not 9" error was printed
# because 2 + 2 = 4 and 2 squared is also equal to 4

# the less code we write to test, the more likely we'll do it 
# and also fewer opportunities for mistakes.
# this is where the assert keyword comes in.

# ASSERT
# to claim something is true; if it is, nothing happens on the screen 
# if it's not true ie false, you'll see an AssertionError on the screen.
# it's not 100% user-friendly but it'll show the line etc.


# think in terms of corner and edge cases when testing

# PYTEST
# to automate the testing of code
# does not have to write as much lines of code 

# unit testing 
# testing different units of your program, unit means functions 
# pretty user-friendly as far as testing frameworks go and allows us to dive right in 

# documentation:
# docs.pytest.org







from calculator import square 


# def main():

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0



'''
# error with pytest
test_calculator.py F                                                             [100%]

====================================== FAILURES =======================================
_____________________________________ test_square _____________________________________

    def test_square():
        assert square(2) == 4
>       assert square(3) == 9
E       assert 6 == 9
E        +  where 6 = square(3)

test_calculator.py:44: AssertionError
=============================== short test summary info ===============================
FAILED test_calculator.py::test_square - assert 6 == 9
================================== 1 failed in 0.57s ==================================
(venv) PS C:\Users\linci\OneDrive\Desktop\python\harvard-cs50\5 lecture five - unit tests> 

'''




# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")


# USING ASSERT
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")

# if __name__ == "__main__":
#     main()
