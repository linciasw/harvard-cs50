# LECTURE

# x = int(input("What's x? ")) # input is cat, the word
# print(f"x is {x}")


# value error
# invalid literal for int() with base 10: 'hello'

# error messages are written for comfortable programmers
# write code with error handling in mind 

# we have to program defenensively ie:
# solve the problems we care about while being able to handle errors
# that might unexpectedly happen or errors that happen becuase the user is in fact malicious
# and they're actively trying to crash the program 


# TRY & EXCEPT 
# to check if something unexpected has happened

'''
try:
    x = int(input("What's x? ")) 
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
'''

# there is a way to catch all errors but this could 
# potentially hide bugs in your code so try to 
# explicitly state the type of error for except keyword
# as much as possible


# NameError 
# name 'x' is not defined
# nameError received with code above 
# because of the order of operations:

# When int(input(...)) raises a ValueError, 
# execution jumps directly to the except block.
# Since the assignment to x never completed, x doesn't exist. 
# After the except block, your program still tries to execute:
# print(f"x is {x}")
# but there's no variable named x
# to fix this, we can use the else keyword:
'''
try:
    x = int(input("What's x? ")) 
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
'''


# instead of ending the program after an invalid value is inputted, 
# using the break keyword restarts the program 
# once a valid int value is inputted, break ends the while loop
# essentially, the block will keep looping to the try statement until there's no valueError 
# and only after it gets a value for x, it will go down to the else 
# you can generally use break to get out of any loop
'''
while True:
    try:
        x = int(input("What's x? ")) 
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
'''



# you can also do this:
while True:
    try:
        x = int(input("What's x? ")) 
        break
    except ValueError:
        print("x is not an integer")


print(f"x is {x}")



# random information:
# scope refers to the portion of code in which a variable exists 
# input function always returns a string 
