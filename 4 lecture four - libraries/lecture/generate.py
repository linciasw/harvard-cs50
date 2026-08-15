# FROM LECTURE
# REACH 10:54

'''
libraries are files of code that other people have written that
you can use in your own's program or a library's code that you have
written that you can use in your own program  

it does this by using modules.
a module in python is just a library that typically has one or more
functions or other features built into it.
the purpose of it is to encourage reusability of code.
if you find yourself constantly copying code from old projects into new
ones, there's an opportunity to create a module to load into programs.


a module is a singly python file (.py) containing reusable code, a package is a 
folder containing multiple related modules, while a library is a collection of related 
packages bundled together to provide broader functionality. 


example of modules
- random 
- math
- datetime

documentation
https://docs.python.org/3/library/random.html#module-random
'''

# to import everything in the module
import random 


# because we have imported everything from the module, we'll have
# to specify the method by using random.choice()
# coin = random.choice(["heads", "tails"])
# print(coin)


# if we want to just use the choice function, we do
# to prevent any function, variable names that's already in the module
# from clashing with  
# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)


# random.randint(a, b)








