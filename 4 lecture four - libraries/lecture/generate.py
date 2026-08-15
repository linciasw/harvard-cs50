# Modules. random. import. from. statistics. Command-Line Arguments. sys. sys.argv. 
# IndexError. sys.exit. Slices. Packages. PyPI. pip. cowsay. APIs. requests. JSON. __name__.

# FROM LECTURE
# FROM BEGINNING, UNTIL 17:01

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
https://sites.pitt.edu/~naraehan/python3/importing_modules.html

'''




# to import everything in the module
import random 

# coin = random.choice(["heads", "tails"])
# print(coin)


# if we want to just use the choice function, we do the below.
# this helps you not write random.choice a lot, making the code ugly and annoying 
# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)

# ==============================================================================
# ⚠️ NAMESPACE WARNING: 'from random import choice' vs. Variable Names
# ==============================================================================
# In Python, namespaces can only hold one value for a specific name at a time.
# If you use 'from random import choice', it will clash directly with any local 
# variable or function named 'choice'. The last one defined wins and overwrites 
# the previous one.
#
# SCENARIO 1: Variable overwrites the function
#   from random import choice
#   choice = ["apple", "banana"] # Overwrites the function
#   print(choice(choice))        # CRASH: TypeError ('list' object is not callable)
#
# SCENARIO 2: Function overwrites the variable
#   choice = ["apple", "banana"]
#   from random import choice    # Overwrites the list
#   print(len(choice))           # CRASH: TypeError (function has no len())
#
# BEST PRACTICE SOLUTIONS:
# 1. Use the 'as' keyword to alias the function:
#    from random import choice as choose_item
#
# 2. Import the whole module to keep names separated inside a namespace container:
#    import random
#    choice = ["apple", "banana"]
#    random.choice(choice)
# ==============================================================================



# random.randint(a, b)
# if you put a as 1 and b as 10, the function will give you back a random int
# betwen the 1 and 10 inclusive 


# number = random.randint(1, 10)
# print(number)


# random.shuffle(x)
# takes a list and shuffles it up
# shuffles the argument in place? research

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)



# help(random)

'''
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 
'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', 
'__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
'_acos', '_ceil', '_cos', '_e', '_exp', '_inst', '_log', '_pi', '_random', '_sha512', '_sin', 
'_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'expovariate', 
'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 
'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 
'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
'''




