# https://cs.du.edu/~intropython/intro-to-programming/random_numbers.html

import random 


while True:
    try:
        n = int(input("Level: "))
        number = random.randint(1, n)
    except ValueError:
        continue
    else:
        break


while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    if guess == number:
        print("Just right!")
        break


"""
# THINGS LEARNT
- sometime 2 while loops are what's necessary 
- ValueErrors occur when there's a type conversion 
- a little bit about randint
"""
        











