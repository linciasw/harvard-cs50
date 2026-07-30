'''
In a file called twttr.py, implement a program that prompts the user for a str of text 
and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.
'''



'''
n Python, not in is a membership operator used to check if a specific value is absent from a collection. 
It evaluates to True if the item is not found, and False if it is present.
'''

def main():

    word = input("Input: ")
    vowels = ["a", "e", "i", "o", "u"]
    new_word = ""


    for letter in word:
        if letter not in vowels:
            new_word = new_word + letter.lower()
        else:
            continue 

    print(new_word)


main()