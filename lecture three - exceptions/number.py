# LECTURE

# x = int(input("What's x? ")) # input is cat, the word
# print(f"x is {x}")
# output is a ValueError: invalid literal for int() with base 10: 'cat'
# This error occurs because you are passing the text string 'cat' into Python's int() function, 
# which can only convert strings that contain numeric digits.
# The Python int() built-in function expects a string literal that represents a valid base-10 whole number (like '123' or '-45'). 
# Because letters like "c", "a",  and "t" have no numeric value in base-10, the interpreter throws a ValueError



# error messages are written for comfortable programmers
# write code with error handling in mind 

# we have to program defenensively ie:
# solve the problems we care about while being able to handle errors
# that might unexpectedly happen or errors that happen becuase the user is in fact malicious
# and they're actively trying to crash the program 


# TRY & EXCEPT 
# to check if something unexpected has happened
# try:
#     x = int(input("What's x? ")) # input is cat, the word
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}")

# NameError: name 'x' is not defined
# NameError received with code above 
# because of the order of operations:

# When int(input(...)) raises a ValueError, 
# execution jumps directly to the except block.
# Since the assignment to x never completed, x doesn't exist. 
# After the except block, your program still tries to execute:
# print(f"x is {x}")
# but there's no variable named x


# to fix this, we can use the else keyword
# if there is a ValueError, 
# output will be "x is not an integer" and program will end however
# if valid, it'll go the the else block
# try:
#     x = int(input("What's x? ")) 
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")



# instead of ending the program after an invalid value is inputted, 
# using a while loop and the break keyword restarts the program 
# while True: creates an infinite loop because the condition evaluating the loop is hardcoded to always be true. 
# It will execute the code block inside it endlessly until it hits an explicit command to stop, 
# like a break statement, a return statement, or an external system crash.
# once a valid int value is inputted, the try block goes down 
# to the break statement which ends the while loop
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



# you can also do the below.
# if you don't break, it will stay in the loop
# breaks are generally used in loops
# while True:
#     try:
#         x = int(input("What's x? ")) 
#         break
#     except ValueError:
#         print("x is not an integer")

# print(f"x is {x}")


# random information:
# scope refers to the portion of code in which a variable exists 
# input function always returns a string 
# there is a way to catch all errors but this could 
# potentially hide bugs in your code so try to 
# explicitly state the type of error for except keyword
# as much as possible



# if we want to abstract the function away, 
# we can create a function to get integers from users 

def main():
    x = get_int()
    print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? ")) 
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x



# tightening up the get_int() function
# one way:
def get_int():
    while True:
        try:
            x = int(input("What's x? ")) 
            return x
        except ValueError:
            print("x is not an integer")


# another way:
def get_int():
    while True:
        try:
            return int(input("What's x? ")) 
        except ValueError:
            print("x is not an integer")

# which one is better depends on if you want readability
# and understanding less than compact code 


# the pass keyword
# if you want to handle an exception in python
# but you want to pass on doing anything with it 
# ie you want to catch it but ignore it
def get_int():
    while True:
        try:
            return int(input("What's x? ")) 
        except ValueError:
            pass

main()

# indentation is baked into python 
# the pythonic way of doing things is to try things, 
# hope they work but if they don't, handle the exception 