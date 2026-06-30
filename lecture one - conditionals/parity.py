
# modulo operator 
# used to return the remainder of a division operation between 2 numbers
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
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0: # if n divided by 2 equals to zero 
        return True
    else: 
        return False


main()