# LIST & DICTIONARY COMPREHENSIONS

"""
this program combines a list & dictionary comprehension 
to simplify the program into 4 lines as seen below.


the initial nested for, if loop is converted to a dictionary comprehension 


    # nested for, if loop
    for word in words:
    for word in lowercase_words:
        if word in counts:
            counts[word] += 1 # accessing the value of the key and adding one to it 
        else:
            counts[word] = 1 

    # dictionary compreension 
    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    
    the .count() method counts how many times something appears in a list
    
"""


from helpers import get_words, save_counts

def main():
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]
    counts = {word: lowercase_words.count(word) for word in lowercase_words}
    save_counts(counts)

main()