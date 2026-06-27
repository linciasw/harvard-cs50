# ==================================
# CS50 - LECTURE 0: FUNCTIONS & VARIABLES
# ==================================
# Personal Python Learning Notebook
# Do NOT delete examples. Modify and experiment.

# ==================================
# 0. BIG IDEA
# ==================================
"""
Python is an interpreter:
- It reads code top to bottom
- Converts it into instructions the computer understands

Core building blocks:
- Functions → do things
- Variables → store things
- Data types → define what kind of thing it is
"""

# ==================================
# 1. VARIABLES
# ==================================

# Variables store values in memory

name = "Lincia"
age = 27

# Assignment operator
# = means "store value", NOT equality

# IMPORTANT:
# Variables can be overwritten
name = "John"

# PRACTICE
city = "Chaguanas"


# ==================================
# 2. INPUT + OUTPUT
# ==================================

# input() ALWAYS returns a STRING

name = input("What's your name? ").strip().title()

# print() outputs text to the screen
print("Hello,", name)

# f-string (best way to format strings)
print(f"Hello, {name}")

# NOTE:
# print automatically adds a newline at the end


# ==================================
# 3. FUNCTIONS
# ==================================

# A function performs a task

print("Hello")
len("hello")  # returns length of string
round(3.14159, 2)

# Functions can take inputs (arguments)

# Example:
print("Hello", "World")

# print(*objects, sep=' ', end='\n')

# IMPORTANT IDEA:
# Functions can return values OR just perform actions


# ==================================
# 4. STRING METHODS
# ==================================

name = " john smith "

# Remove whitespace
name = name.strip()

# Capitalize first letter
name = name.capitalize()

# Capitalize each word
name = name.title()

# Chain methods
name = " john smith ".strip().title()

print(name)

# IMPORTANT:
# Strings are IMMUTABLE (cannot be changed directly)
# Methods return NEW strings


# ==================================
# 5. SPLIT FUNCTION
# ==================================

name = "John Smith"

first, last = name.split(" ")

print(first)
print(last)

# NOTE:
# split() breaks a string into parts based on a separator


# ==================================
# 6. DATA TYPES
# ==================================

# String
text = "hello"

# Integer
num = 10

# Float
pi = 3.14

# IMPORTANT:
# input() returns STRING even if user types numbers

age = input("Age: ")
# age + 1  ❌ will fail


# FIX:
age = int(input("Age: "))
print(age + 1)


# ==================================
# 7. OPERATORS
# ==================================

# Arithmetic operators
# +  -  *  /  %

x = 10 + 5
y = 10 / 2

# MODULO gives remainder
remainder = 10 % 3


# ==================================
# 8. COMMENTS
# ==================================

# Single-line comment

"""
Multi-line comment (docstring style)
Used for longer explanations
"""

# IMPORTANT:
# Comments should explain WHY, not WHAT


# ==================================
# 9. PARAMETERS VS ARGUMENTS
# ==================================

# Parameter = placeholder in function definition
# Argument = actual value passed in

print("Hello")  # "Hello" is an argument


# ==================================
# 10. SCOPE
# ==================================

# Variables only exist where they are created

def greet():
    name = "Bob"
    print(name)

greet()

# print(name)  ❌ ERROR (outside scope)


# ==================================
# 11. PRINT PARAMETERS
# ==================================

print("A", "B", "C", sep="-")
print("Hello", end=" ")
print("World")

# sep = separator
# end = what happens at end of print


# ==================================
# 12. ESCAPE CHARACTERS
# ==================================

print("He said \"Hello\"")

# OR use single quotes outside
print('He said "Hello"')


# ==================================
# 13. PYTHON INTERACTIVE MODE
# ==================================

# In terminal:
# python
# then type commands directly

# exit with:
# Ctrl + Z then Enter (Windows)


# ==================================
# 14. COMMON MISTAKES
# ==================================

# ❌ Missing quotes
# print(Hello)

# ✅ Correct
print("Hello")

# ❌ input returns string
# age = input()
# print(age + 1)

# ✅ Fix
age = int(input("Age: "))
print(age + 1)


# ==================================
# 15. FLOAT VS INT LIMITATION
# ==================================

# int = unlimited size (practically)
big_number = 999999999999999999

# float = limited precision
pi = 3.14159265358979323846

# NOTE:
# floats can lose precision due to memory limits


# ==================================
# 16. ROUND FUNCTION
# ==================================

# round(number[, ndigits])

x = round(3.14159)
y = round(3.14159, 2)

print(x)
print(y)


# ==================================
# 17. KEY TAKEAWAYS (IMPORTANT)
# ==================================
"""
- input() always returns a string
- Variables store values
- Functions do work or return values
- Methods modify or return new strings
- Python runs top to bottom
- = is assignment, not equality
- Strings are immutable
"""


# ==================================
# 18. MINI TEST (DO NOT SKIP)
# ==================================

# Try writing these without looking:

# 1. Ask for name and print it
# 2. Ask for age and print next year
# 3. Format full name using title case
# 4. Split full name into first/last
# 5. Print using f-string


# ==================================
# END OF LECTURE 0
# ==================================