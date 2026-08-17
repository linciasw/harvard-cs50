# CHAPTER 6
# DICTIONARIES

# Working with dictionaries
'''
a dictionary in python is a collection of key-value pairs.
each key is connected to a value, and you can use a key to access 
the value associated with that key.
a key's value can be a number, a string, a list, or even another dictionary.
you can use any object that you can create in python as a value in a dictionary.
'''

alien_0 = {"color": "green", "points": 5}



# Accessing values in a dictionary
'''
a key-value pair is a set of values associated with each other. 
when you provide a key, python returns the value associated with that key.
you can have an unlimited number of key-value pairs in a dictionary.
'''


# to get the value associated with a key, give the name of the dictionary 
# and then place the key inside a set of square brackets as shown below.

# print(alien_0["color"])
# the output of this is "green"


new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points!")
# the output of this is "You just earned 5 points!"


# Adding new key-value pairs










