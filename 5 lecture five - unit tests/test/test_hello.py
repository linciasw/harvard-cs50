# you can test a whole folder of tests
# need to be outside of the folder though


from hello import hello 


def test_default():
    assert hello() == "hello, world"



def test_argument():
    assert hello("David") == "hello, David"
