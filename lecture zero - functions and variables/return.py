# from shorts, not from lecture

"""
def area(length, width):
    print(str(length * width) + " square feet")


def main():
    area(50,20)

main()
"""


"""
def area(length, width):
    print(str(length * width) + " square feet")


def main():
    area(50,20)
    area(50,50)

main()
"""



def area(length, width):
    return length * width # return ends the function


def main():
    house = area(50, 20)
    yard = area(50, 50)
    total = house + yard
    print(str(total) + " square feet")


main()
