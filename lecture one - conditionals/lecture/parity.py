
# modulo operator 
# parity: the property of an integer being even or odd
# used to return the remainder of a division operation between 2 numbers
# 4 % 2 asks "how many times does 2 go into 4? and what's the remainder"
# the anser is 2 times exactly with a remainder of 0 so 4 % 2 = 0 
# 
"""
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
"""


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even") # True 
    else:
        print("Odd") # False

def is_even(n):
    """
    if n % 2 == 0: # 2 into n remainder; 2 into 4 is 2 with remainder zero 
        return True
    else: 
        return False
    """

    # 2nd way doing the above
    # return True if n % 2 == 0 else False # boolean expression, Y/N True/False

    # 3rd way of doing above; the pythonic way 
    # n % 2 == 0 already evaluates to either True or False
    return n % 2 == 0


    """
    whenever you see code like: 
    if condition:
        return True
    else:
        return False


    you can almost always simplify it to 
    return condition 
    
    """


main()


