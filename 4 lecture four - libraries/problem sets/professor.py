

# need to find a way to call generate_integer() after the users gets it wrong 3 timesa 
# and the correct answer prints


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
        x = random.randint(100, 999)


    return x, y






            
if __name__ == "__main__":
    main()