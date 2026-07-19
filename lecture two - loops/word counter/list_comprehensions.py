# LIST COMPREHENSIONS

# comprehensions are a quick way to build up a list or a dictionary 
# from data you already have

from helpers import get_words, save_counts

# this program counts the frequency of words in 'address.txt' and save the results.
def main():

    counts = {}
    words = get_words("address.txt") # get_words creates a list

    # list comprehension needed: to create a new list that's all lower case to ignore case
    # the program before was counting the title case words as separate
    # lowercase_words = [word.lower() for word in words]

    # narrower conditions 
    # lower case words that are > 4
    lowercase_words = [word.lower() for word in words if len(word) > 4]


    """
    a list comprehension is just a compact way of writing a for loop.
    it's used for transforming, filtering and simplifying code. 

    this list comprehension:
    lowercase_words = [word.lower() for word in words if len(word) > 4] 

    is equivalent to this for loop:
    lowercase_words = []    # create an empty list first 
    for word in words:      # got through every word 
        if len(word) > 4:   # only keep words longer than 4 characters 
            lowercase_words.append(word.lower())    # add the lowercase version 



    the list comprehension has three parts:
    - what to put in the new list: word.lower()
    - where to get the values from: for word in words
    - the condition: if len(word) > 4


    a trick to use to read list comprehensions:
    - read them from the middle outward:
    instead of reading from left-to-right, think:
    "for each word in words, if its length is greater than 4, put word.lower() into the new list."



    most list comprehensions follow this pattern:
    new_list = [do_something(item) for item in collection/iterable if condition]

    nb: do_something(item) could be a call to a method, 
    or any other valid expression that returns a value

    nb: the conditional in this list comprehension does filtering 


    which expands to the below for loop:
    new_list = []

    for item in collection:
        if condition:
            new_list.append(do_something(item))


    Should you use list comprehensions or a for loop? 
    Rather than adhere to a single rule that’s true in all cases, 
    it’s more useful to ask yourself whether or not performance matters in your specific circumstance. 
    If not, then it’s usually best to choose whatever approach leads to the cleanest code!

    the timeit library is useful for timing how long it takes chunks of code to run. 
    You can use timeit to compare the runtime.
    """

    # for word in words:
    for word in lowercase_words:
        if word in counts:
            counts[word] += 1 # accessing the value of the key and adding one to it 
        else:
            counts[word] = 1
        
    save_counts(counts) # to save dictionary in a csv



main()