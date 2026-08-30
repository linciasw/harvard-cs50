"""
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, 
wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.

Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:

"""


# TO DO 
# create another function to get user input
# create a test for the value error



def main():


# once you're in a try-except block and an error comes up, it wil look for the except to know what to do
# in the below loop, it stays in the while loop because the break is only if the try does not give a ValueError

    while True:
        try:
            word = input("Input: ")

            if word.isdigit():
                raise ValueError
            else:
                break

        except ValueError:
            print("Please enter a word")




    shortened_word = shorten(word)
    print(shortened_word)



def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_word = ""

    for letter in word:
        if letter not in vowels:
            new_word = new_word + letter.lower()
        else:
            continue

    return new_word




if __name__ == "__main__":
    main()