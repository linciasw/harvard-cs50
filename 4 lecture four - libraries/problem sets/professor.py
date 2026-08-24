




import random


def main():
    user_level = get_level()
    x, y = generate_integer(user_level)

    # answer = x + y
    # user_answer = input(f"{x} + {y} = ")

    i = 0
    j = 0
    count = 0

    while i < 10:
        try:
            answer = x + y
            user_answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("Enter a number please")
            continue



        if user_answer == answer:
            i += 1
            count += 1
            generate_integer()

            
        elif user_answer != answer: 
            print("EEE")
            user_answer = int(input(f"{x} + {y} = "))
            j + 1
            continue
        elif user_answer != answer and j == 3:
            print(f"{x} + {y} = ", {answer})
            break





    





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
        x = random.randint(100, 999)


    return x, y



if __name__ == "__main__":
    main()