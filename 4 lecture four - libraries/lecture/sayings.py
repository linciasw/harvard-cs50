# FROM LECTURE 
# CUSTOM LIBRARIES
# FROM 1:10:06


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")



# __name__ == "__main__" prevents the program importing this as a module from running the entire program.
# the program will only run fully if it's called by itself.
# it's basically asking: "is this file being imported or is it being run?"
if __name__ == "__main__":
    main()