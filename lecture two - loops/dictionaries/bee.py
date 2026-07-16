# DICTIONARY METHODS
# FROM CS50 SHORTS

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

"""
def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left") # len checks the number of 'key: value' pairs are in the dictionary
        guess = input("Guess a word: ")


        # TODO: Check if guess in dictionary
        # to clear the entire dictionary
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")


        if guess in WORDS.keys():
            # print(f"Good job! You scored {WORDS[guess]} points.") # this will access the value associated with the key

            # to remove word from keys 
            points = WORDS.pop(guess) # pop will return key value and remove key from dictionary
            print(f"Good job! You scored {points} points.")


    print("That's the game!")


main()
"""



def main():
    print("Welcome to Spelling Bee!")


    
    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")


main()