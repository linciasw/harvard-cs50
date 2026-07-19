# LIST AND DICTIONARY COMPREHENSIONS
# DOCSTRING:
"""
    Reads words from a text file, counts the number of occurrences
    of each word, and saves the resulting word frequencies.

    The function:
    1. Creates an empty dictionary to store word counts.
    2. Retrieves a list of words from 'address.txt' using get_words().
    3. Iterates through the words and counts how many times each
       word appears.
    4. Saves the completed word count dictionary using save_counts().

    The below program coounts title case words as separate however. 
"""




from helpers import get_words, save_counts

def main():
    counts = {}
    words = get_words("address.txt") # this counts title case words as separate, a new case-sensitive list needs to be created

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)

main()