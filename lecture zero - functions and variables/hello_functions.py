# functions are mainly to prevent yourself from repeating code again and again


""""
def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)
"""


"""
#name is being copied to another variable named "to"
def hello(to):
    print("hello,", to)


name = input("What's your name? ")
hello(name)
"""



def main():
    name = input("What's your name?")
    hello(name)


#assigning a default value in case there's no input
def hello(to="world"):
    print("hello,", to)


main()