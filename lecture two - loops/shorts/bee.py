# DICTIONARY METHODS

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left")
        guess = input("Guess a word: ")


        # TODO: Check if guess in dictionary
        if guess in WORDS.keys():
            # print(f"Good job! You scored {WORDS[guess]} points.") # this will access the value associated with the key

            # to remove word from keys 
            points = WORDS.pop(guess) # pop will return key value and remove key from dictionary
            print(f"Good job! You scored {points} points.")


    print("That's the game!")


main()