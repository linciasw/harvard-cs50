def main():
    name = input("What's your name? ")
    print(hello(name))


# this will not work because the function is not returning anything
# it essentially just has a print side effect
# def hello(to="world"):
#     print("hello,", to)


# to make it testable, we do below
def hello(to="world"):
    return f"hello, {to}"



if __name__ == "__main__":
    main()