# LIST COMPREHENSIONS

# comprehensions are a quick way to build up a list or a dictionary 
# from data you already have

from helpers import get_words, save_counts

# this program counts the frequency of words in 'address.txt' and save the results.
def main():

    counts = {}
    words = get_words("address.txt") # get_words creates a list

    # list comprehension: to create a new list that's all lower case to ignore case
    # the program before was counting the title case words as separate
    # lowercase_words = [word.lower() for word in words]

    # narrower conditions 
    # lower case words that are > 4
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    # for word in words:
    for word in lowercase_words:
        if word in counts:
            counts[word] += 1 # accessing the value of the key and adding one to it 
        else:
            counts[word] = 1
        
    save_counts(counts) # to save dictionary in a csv



main()