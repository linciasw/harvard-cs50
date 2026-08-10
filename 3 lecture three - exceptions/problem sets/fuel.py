'''
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, 
and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, 
wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage 
rounded to the nearest integer, how much fuel is in the tank. 
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''

# look at problem sets in conditionals re: the split method
# intepreter. py and meal.py


def main():

    while True:
        try:
            x, y = input("Fraction: ").split("/")
        except ValueError:
            pass
        else:
            try:
                x = int(x)
                y = int(y)

                if x > y:
                    continue

                percentage = (x / y) * 100
            except (ValueError, ZeroDivisionError):
                pass
            else:
                break

    if percentage == 100:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{round(percentage)}%")


main()

