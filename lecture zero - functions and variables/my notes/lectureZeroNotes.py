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


# list of common string methods:
# .startswith()
# .endswith()
# .lower()
# .upper()
# .strip()
# .replace()
# .split()
# .join()
# .find()

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
# +  -  *  /  % **

x = 10 + 5
y = 10 / 2

# MODULO gives remainder
remainder = 10 % 3

# ** is squared 


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
# DEEP UNDERSTANDING
# ==================================
"""
These concepts will appear throughout the rest of CS50 and Python.
I don't need to master them today, but I should revisit them often.
"""


# ==================================
# 1. HOW FUNCTIONS WORK
# ==================================

"""
A function is a reusable block of code that performs a task.

Think of every function call like this:

Arguments
    ↓
Function executes
    ↓
Return value (sometimes)
"""

# Example

name = input("What's your name? ").strip().title()

"""
Step-by-step:

1. input() asks the user for input.
2. input() RETURNS a string.
3. strip() RETURNS a new string with whitespace removed.
4. title() RETURNS another new string with each word capitalized.
5. The final value is stored inside 'name'.

Notice that every method returns a value that the next method uses.
"""

# Another example

length = len("banana")

"""
Arguments:
"banana"

↓

len()

↓

Returns:
6

↓

Stored in variable 'length'
"""


# ==================================
# 2. RETURN VALUES
# ==================================

"""
One of the most important ideas in programming.

A function may:
• perform an action
• return a value
• or both
"""

# Performs an action

print("Hello")

"""
print() displays text.

It is mainly used for OUTPUT.
"""

# Returns a value

name = input("Name: ")

"""
input() returns whatever the user types.

If the user types:

Bob

input() returns:

"Bob"

That value gets stored in the variable.
"""

# Another example

length = len("apple")

"""
len() returns:

5

which gets assigned to length.
"""

# IMPORTANT

"""
Ask yourself whenever you use a function:

"What value does this function return?"

Understanding return values will make writing your own functions much easier later.
"""


# ==================================
# 3. STRINGS ARE IMMUTABLE
# ==================================

"""
Immutable means "cannot be changed."

Strings cannot be modified in place.

Methods create NEW strings instead.
"""

name = "john"

# This DOES NOT permanently change name

name.title()

print(name)

# Output:
# john

# Correct

name = name.title()

print(name)

# Output:
# John

"""
Most string methods return a NEW string.

If you want to keep the result,
assign it back to the variable.
"""


# ==================================
# 4. READING DOCUMENTATION
# ==================================

"""
Every programmer reads documentation.

You do NOT have to memorize it.

Learn how to understand it.
"""

# Example documentation

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

"""
How to read this:

objects
    Things you want to print.

sep=' '
    Optional separator between objects.

end='\\n'
    What gets printed after everything.

file=sys.stdout
    Where output is sent (usually the terminal).

flush=False
    Advanced option that forces output immediately.

For now, focus on:

• What does the function do?
• What arguments are required?
• Which arguments are optional?
• What does it return?
"""

# Another example

# round(number[, ndigits])

"""
number
    Required

ndigits
    Optional

Examples:

round(3.14)

round(3.14159, 2)
"""


# ==================================
# QUESTIONS TO ASK YOURSELF
# ==================================

"""
Whenever learning something new, ask:

1. What problem does this solve?

2. What does it return?

3. Does it modify the original object?

4. What arguments can I pass?

5. What mistakes do beginners make?

6. Can I explain it in my own words?

These six questions will help you understand concepts
instead of memorizing syntax.
"""

# ==================================
# END OF LECTURE 0
# ==================================