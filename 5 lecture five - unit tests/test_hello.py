# TESTING STRINGS, SIDE EFFECTS 



from hello import hello 



# the assert statements are really design to test:
# 1 - return arguments from functions and
# 2 - return values from functions, not side effects (print, for example)
# def test_hello():
#     assert hello("David") == "hello, David"
#     assert hello() == "hello, world"


# to separate tests
def test_default():
    assert hello() == "hello, world"



def test_argument():
    # we can test using loops:
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
    # assert hello("David") == "hello, David"
    



