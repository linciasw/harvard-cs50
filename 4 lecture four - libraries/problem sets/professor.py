
'''
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. 
For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. 
If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, 
the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. 
No need to support operations other than addition (+).
Note: The order in which you generate x and y matters. 
Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, 
allowing the user up to three tries in total for that problem. 
If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, 
and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3.
'''




"""
# THINGS LEARNT
- you have to learn to recognize when nested loops are necessary
- you don't have to check for all conditionals:
    - in the below, only the amount of attempts was checked in the while loop

    

# TO HELP WITH PROGRAMMATIC THINKING:
Whenever you get a programming problem, don't write code immediately.
Ask these 4 questions:
    - What is the overall task repeating?
    - What is happening repeatedly inside that task?
    - What causes the inner repetition to stop?
    - What causes the outer repetition to stop?
"""


import random


def main():

    user_level = get_level()
    count = 0



    for i in range(10):
            
            x, y = generate_integer(user_level)
            attempts = 0


            while attempts < 3:

                try:
                    answer = x + y
                    user_answer = int(input(f"{x} + {y} = "))
                except ValueError:
                    print("Enter a number please")
                    continue


                if user_answer == answer:
                    count += 1
                    break

                elif attempts < 2: 
                    attempts += 1
                    print("EEE")
                    continue

                elif attempts == 2:
                    print(f"{x} + {y} = {answer}")
                    break


    print(f"Total correct: ", {count})

    

        # else:
        #     print(f"Total correct: ", {count})
        #     # generate_integer(user_level)
        #     continue


def get_level():
    ...
    # range(1, 4)
    while True:
        try:
            user_level = int(input("Level: "))
        except ValueError:
            print("Level must be 1 - 3")
            continue

        if user_level not in range(1, 4):
            continue
        elif user_level in range(1, 4):
            break


    return user_level


def generate_integer(level):
    ...
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)

    if level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    if level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)


    return x, y






            
if __name__ == "__main__":
    main()