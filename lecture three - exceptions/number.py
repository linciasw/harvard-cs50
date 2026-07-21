# x = int(input("What's x? ")) # input is cat, the word
# print(f"x is {x}")


# value error
# invalid literal for int() with base 10: 'hello'

# error messages are written for comfortable programmers
# write code with error handling in mind 
# we have to program defenensively ie 
# solve the problems we care about while being able to handle errors
# that might unexpectedly happen or that the user is in fact malicious
# and they're actively trying to crash the program 


# TRY & EXCEPT 
# to check if something unexpected has happened

try:
    x = int(input("What's x? ")) 
except ValueError:
    print("x is not an integer")

print(f"x is {x}")


# there is a way to catch all errors but this could 
# potentially hide bugs in your code so try to 
# explicitly state the type of error for except 
# as much as possible

