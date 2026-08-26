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







from calculator import square 


def main():
    test_square()


# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")


# USING ASSERT
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")

if __name__ == "__main__":
    main()
