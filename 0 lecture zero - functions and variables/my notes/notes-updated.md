# CS50 Lecture 0 — Functions & Variables

## Complete Consolidated Notes

> **Goal:** Understand the fundamental building blocks of Python: variables, functions, input/output, strings, data types, operators, scope, return values, and basic program structure.
>
> These concepts form the foundation for everything that follows in CS50 and Python.

---

# Table of Contents

1. [The Big Picture](#1-the-big-picture)
2. [How Python Executes Code](#2-how-python-executes-code)
3. [Variables](#3-variables)
4. [Assignment and Reassignment](#4-assignment-and-reassignment)
5. [Input](#5-input)
6. [Output with print()](#6-output-with-print)
7. [f-Strings](#7-f-strings)
8. [Data Types](#8-data-types)
9. [Integers](#9-integers)
10. [Floating-Point Numbers](#10-floating-point-numbers)
11. [Complex Numbers](#11-complex-numbers)
12. [Strings](#12-strings)
13. [String Methods](#13-string-methods)
14. [String Immutability](#14-string-immutability)
15. [Method Chaining](#15-method-chaining)
16. [Splitting and Joining Strings](#16-splitting-and-joining-strings)
17. [String Searching and Validation](#17-string-searching-and-validation)
18. [Type Conversion](#18-type-conversion)
19. [Checking Data Types with type()](#19-checking-data-types-with-type)
20. [Operators](#20-operators)
21. [Comments and Documentation](#21-comments-and-documentation)
22. [Functions](#22-functions)
23. [Parameters and Arguments](#23-parameters-and-arguments)
24. [Function Syntax](#24-function-syntax)
25. [Default Parameters](#25-default-parameters)
26. [Positional Arguments](#26-positional-arguments)
27. [Keyword Arguments](#27-keyword-arguments)
28. [Variable Numbers of Arguments](#28-variable-numbers-of-arguments)
29. [Return Values](#29-return-values)
30. [return vs print()](#30-return-vs-print)
31. [None](#31-none)
32. [Scope](#32-scope)
33. [Global Variables and Side Effects](#33-global-variables-and-side-effects)
34. [Pure Functions](#34-pure-functions)
35. [Function Design and Decomposition](#35-function-design-and-decomposition)
36. [Arguments and Object References](#36-arguments-and-object-references)
37. [print() Parameters](#37-print-parameters)
38. [Escape Characters](#38-escape-characters)
39. [Interactive Python](#39-interactive-python)
40. [Reading Documentation](#40-reading-documentation)
41. [Common Beginner Mistakes](#41-common-beginner-mistakes)
42. [Complete CS50 Code Walkthrough](#42-complete-cs50-code-walkthrough)
43. [Practice Work](#43-practice-work)
44. [Practical Function Patterns](#44-practical-function-patterns)
45. [Six Questions for Learning Python](#45-six-questions-for-learning-python)
46. [Key Takeaways](#46-key-takeaways)
47. [Mini Practice](#47-mini-practice)
48. [Further Practice Ideas](#48-further-practice-ideas)

---

# 1. The Big Picture

Python programs are built from a few fundamental ideas:

* **Functions** → perform tasks
* **Variables** → store values
* **Data types** → describe what kind of value is being stored
* **Operators** → perform calculations and comparisons
* **Methods** → perform operations on objects
* **Input** → allows a program to receive information
* **Output** → allows a program to display information
* **Control flow** → determines what code executes and when

A useful mental model is:

```text
INPUT
  ↓
STORE DATA IN VARIABLES
  ↓
PROCESS DATA
  ↓
RETURN / DISPLAY RESULT
```

Functions allow us to organize this process into reusable pieces.

---

# 2. How Python Executes Code

Python is an **interpreted language**.

At a basic level, Python executes instructions from top to bottom.

For example:

```python
print("First")
print("Second")
print("Third")
```

Output:

```text
First
Second
Third
```

The order matters.

A Python program generally begins executing at the first executable statement and proceeds through the program.

---

# 3. Variables

A variable is a name that refers to a value.

```python
name = "Lincia"
age = 27
```

You can think of:

```python
name = "Lincia"
```

as assigning the value `"Lincia"` to the name `name`.

Variables allow us to store information and use it later.

```python
name = "Lincia"

print(name)
```

Output:

```text
Lincia
```

---

# 4. Assignment and Reassignment

The `=` operator is the **assignment operator**.

It does not mean mathematical equality.

```python
name = "Lincia"
```

means:

> Assign the value `"Lincia"` to the variable `name`.

Variables can be reassigned:

```python
name = "Lincia"

name = "John"

print(name)
```

Output:

```text
John
```

The variable now refers to the new value.

---

# 5. Input

The `input()` function allows a program to receive information from the user.

```python
name = input("What's your name? ")
```

If the user enters:

```text
Lincia
```

then:

```python
name
```

contains:

```python
"Lincia"
```

## Important Rule

`input()` **always returns a string**.

Even if the user enters a number:

```python
age = input("Age: ")
```

and enters:

```text
25
```

Python receives:

```python
"25"
```

not:

```python
25
```

This distinction is extremely important.

---

# 6. Output with print()

The `print()` function displays information.

```python
print("Hello")
```

Output:

```text
Hello
```

You can print multiple values:

```python
print("Hello", "World")
```

Output:

```text
Hello World
```

You can also print variables:

```python
name = "Lincia"

print(name)
```

---

# 7. f-Strings

f-strings provide a convenient way to insert variables into strings.

```python
name = "Lincia"

print(f"Hello, {name}")
```

Output:

```text
Hello, Lincia
```

The `f` before the string tells Python that expressions inside `{}` should be evaluated.

Example:

```python
age = 27

print(f"I am {age} years old.")
```

You can also perform expressions:

```python
x = 10
y = 5

print(f"The answer is {x + y}")
```

---

# 8. Data Types

Python has different types of values.

Common types include:

| Type      | Meaning              | Example     |
| --------- | -------------------- | ----------- |
| `str`     | Text                 | `"hello"`   |
| `int`     | Whole number         | `10`        |
| `float`   | Decimal number       | `3.14`      |
| `complex` | Complex number       | `3 + 4j`    |
| `list`    | Collection of values | `[1, 2, 3]` |

The type determines what operations can be performed on the value.

---

# 9. Integers

Integers (`int`) represent whole numbers.

```python
x = 10
```

Examples:

```python
10
0
-5
999999999999999999
```

Python integers can represent extremely large whole numbers.

## Integer Arithmetic

### Addition

```python
x + 5
```

### Subtraction

```python
x - 5
```

### Multiplication

```python
x * 5
```

### Division

```python
x / 5
```

Division with `/` produces a float.

```python
10 / 2
```

produces:

```python
5.0
```

### Floor Division

```python
10 // 3
```

produces:

```text
3
```

Floor division removes the fractional portion by rounding down.

### Modulus

```python
10 % 3
```

produces:

```text
1
```

The modulus operator gives the remainder.

### Exponentiation

```python
10 ** 2
```

produces:

```text
100
```

---

# 10. Floating-Point Numbers

Floats (`float`) represent decimal numbers.

```python
y = 3.14
```

Examples:

```python
3.14
10.5
-2.75
```

Floats support the same basic arithmetic operators:

```python
y + 2
y - 1
y * 3
y / 2
```

## Rounding

```python
round(3.14159, 2)
```

Output:

```text
3.14
```

You can also use:

```python
round(3.14159)
```

Output:

```text
3
```

Syntax:

```python
round(number[, ndigits])
```

---

# 11. Complex Numbers

Python also has a `complex` data type.

Example:

```python
z = 3 + 4j
```

Complex numbers contain:

* a real component
* an imaginary component

They are commonly used in:

* Mathematics
* Physics
* Electrical engineering
* AC circuit analysis
* Signal processing
* Fourier transforms

They are not a major focus of Lecture 0, but they are another built-in Python numeric type.

---

# 12. Strings

Strings (`str`) represent text.

```python
text = "hello world"
```

Strings can contain:

```python
"Hello"
"CS50"
"123"
"hello world"
```

Even this:

```python
"123"
```

is text, not a number.

That means:

```python
"10" + "5"
```

produces:

```text
105
```

while:

```python
10 + 5
```

produces:

```text
15
```

The first performs string concatenation.

The second performs mathematical addition.

---

# 13. String Methods

Strings have many built-in methods.

Given:

```python
text = "hello world"
```

## lower()

```python
text.lower()
```

Result:

```text
hello world
```

## upper()

```python
text.upper()
```

Result:

```text
HELLO WORLD
```

## title()

```python
text.title()
```

Result:

```text
Hello World
```

## capitalize()

```python
text.capitalize()
```

This capitalizes the first character.

Example:

```python
"john smith".capitalize()
```

Result:

```text
John smith
```

## strip()

Removes whitespace from the beginning and end.

```python
text.strip()
```

Example:

```python
name = " john smith "

name = name.strip()
```

Result:

```text
john smith
```

## replace()

Replaces text.

```python
text.replace("hello", "hi")
```

Result:

```text
hi world
```

## split()

Splits a string into a list.

```python
text.split()
```

Example:

```python
"John Smith".split()
```

Result:

```python
["John", "Smith"]
```

## join()

Joins values into a string.

```python
" ".join(["John", "Smith"])
```

Result:

```text
John Smith
```

Another example:

```python
"...".join(["This", "is", "CS50"])
```

Result:

```text
This...is...CS50
```

## find()

Finds the position where text begins.

```python
text.find("world")
```

## startswith()

Checks whether a string starts with particular text.

```python
text.startswith("he")
```

Returns:

```python
True
```

## endswith()

Checks whether a string ends with particular text.

```python
text.endswith("ld")
```

Returns:

```python
True
```

## isdigit()

Checks whether all characters are digits.

```python
"123".isdigit()
```

Returns:

```python
True
```

## isalpha()

Checks whether all characters are alphabetic.

```python
"abc".isalpha()
```

Returns:

```python
True
```

## isalnum()

Checks whether all characters are letters or numbers.

```python
"abc123".isalnum()
```

Returns:

```python
True
```

## len()

`len()` returns the length of an object.

```python
text = "hello world"

len(text)
```

Result:

```text
11
```

---

# 14. String Immutability

One of the important concepts from the notes is that **strings are immutable**.

This means a string cannot be changed in place.

For example:

```python
name = "john"

name.title()

print(name)
```

The result is still:

```text
john
```

Why?

Because:

```python
name.title()
```

creates a **new string**.

It does not modify the original string.

To keep the result:

```python
name = name.title()
```

Now:

```python
print(name)
```

produces:

```text
John
```

This idea becomes important later when working with other mutable and immutable objects.

---

# 15. Method Chaining

You can call multiple methods in sequence.

Example:

```python
name = " john smith ".strip().title()
```

Conceptually:

```text
" john smith "
       ↓
.strip()
       ↓
"john smith"
       ↓
.title()
       ↓
"John Smith"
```

Another example:

```python
text = input("Enter your name: ").strip().title()
```

This combines:

1. Input
2. Removing whitespace
3. Capitalizing the name

---

# 16. Splitting and Joining Strings

A particularly useful pattern is:

```python
split()
```

followed by:

```python
join()
```

Example:

```python
text = input("Enter text: ")

result = "...".join(text.split())

print(result)
```

If the user enters:

```text
This is CS50
```

the process is:

```text
"This is CS50"
       ↓
split()
       ↓
["This", "is", "CS50"]
       ↓
"...".join(...)
       ↓
"This...is...CS50"
```

This demonstrates that methods can be combined to transform data.

---

# 17. String Searching and Validation

Useful methods include:

```python
text.find("word")
text.startswith("hello")
text.endswith("world")
text.isdigit()
text.isalpha()
text.isalnum()
```

These are useful when validating or processing user input.

For example:

```python
age = input("Age: ")

if age.isdigit():
    print("Looks like a number.")
```

---

# 18. Type Conversion

Python provides functions for converting values between types.

## int()

```python
int("10")
```

Result:

```python
10
```

You can also convert a float:

```python
int(3.7)
```

Result:

```text
3
```

The decimal portion is truncated.

## float()

```python
float("3.14")
```

Result:

```python
3.14
```

You can also convert an integer:

```python
float(10)
```

Result:

```python
10.0
```

## Why Conversion Matters

Remember:

```python
input()
```

returns a string.

Therefore:

```python
age = input("Age: ")

age + 1
```

does not perform numerical addition.

Instead:

```python
age = int(input("Age: "))

print(age + 1)
```

allows Python to perform arithmetic.

---

# 19. Checking Data Types with type()

The `type()` function tells you what type a value is.

```python
type(10)
```

returns:

```python
int
```

```python
type(10.0)
```

returns:

```python
float
```

```python
type("10")
```

returns:

```python
str
```

This is useful when debugging.

---

# 20. Operators

## Arithmetic Operators

| Operator | Meaning        | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `5 + 2`  |
| `-`      | Subtraction    | `5 - 2`  |
| `*`      | Multiplication | `5 * 2`  |
| `/`      | Division       | `5 / 2`  |
| `//`     | Floor division | `5 // 2` |
| `%`      | Remainder      | `5 % 2`  |
| `**`     | Exponentiation | `5 ** 2` |

Example:

```python
10 % 3
```

Result:

```text
1
```

Example:

```python
2 ** 3
```

Result:

```text
8
```

---

# 21. Comments and Documentation

Comments allow programmers to explain code.

Single-line comment:

```python
# This is a comment
```

Python also supports triple-quoted strings, commonly used for documentation:

```python
"""
Long explanation
"""
```

## Comments vs Docstrings

A useful distinction:

**Comments** explain internal implementation details or why something is done.

**Docstrings** describe the external behavior of a function, class, or module and the parameters it accepts.

Example:

```python
def calculate_total(price, tax):
    """Return the total price including tax."""
    return price + tax
```

A function's docstring can be accessed through:

```python
calculate_total.__doc__
```

---

# 22. Functions

A function is a reusable block of code designed to perform a specific task.

Functions help break large programs into smaller, manageable pieces.

Examples of built-in functions:

```python
print("Hello")
len("hello")
round(3.14159, 2)
```

Functions can:

* Perform an action
* Return a value
* Do both
* Accept information as input
* Be called multiple times

---

# 23. Parameters and Arguments

This distinction is important.

## Parameter

A parameter is the variable defined in the function.

```python
def greet(name):
    print(f"Hello, {name}!")
```

Here:

```python
name
```

is the parameter.

## Argument

An argument is the actual value supplied when calling the function.

```python
greet("Bob")
```

Here:

```python
"Bob"
```

is the argument.

Think:

```text
Parameter = placeholder
Argument  = actual value
```

---

# 24. Function Syntax

Basic syntax:

```python
def function_name(parameters):
    # code
    return value
```

Example:

```python
def calculate_total(price, tax):
    return price + tax
```

Calling the function:

```python
total = calculate_total(100, 15)
```

Now:

```python
total
```

contains:

```text
115
```

---

# 25. Default Parameters

A function parameter can have a default value.

```python
def greet(name="User"):
    print(f"Hello, {name}!")
```

Calling:

```python
greet()
```

produces:

```text
Hello, User!
```

Calling:

```python
greet("Lincia")
```

produces:

```text
Hello, Lincia!
```

Another CS50-style example:

```python
def hello(to="world"):
    print("hello,", to)
```

Then:

```python
hello()
```

produces:

```text
hello, world
```

while:

```python
hello("Lincia")
```

produces:

```text
hello, Lincia
```

---

# 26. Positional Arguments

The simplest way to pass arguments is by position.

Example:

```python
def power(x, y):
    return x ** y
```

Calling:

```python
power(2, 3)
```

produces:

```text
8
```

because:

```text
x = 2
y = 3
```

Calling:

```python
power(3, 2)
```

produces:

```text
9
```

because:

```text
x = 3
y = 2
```

The order matters.

---

# 27. Keyword Arguments

Arguments can also be passed by parameter name.

Example:

```python
power(y=2, x=3)
```

This produces:

```text
9
```

even though the order is reversed.

The names tell Python which value belongs to which parameter.

Keyword arguments can also be combined with default values.

This is useful when a function has many optional settings.

---

# 28. Variable Numbers of Arguments

Python allows a function to accept a variable number of positional arguments using `*`.

Example:

```python
def maximum(*numbers):
    if len(numbers) == 0:
        return None

    maxnum = numbers[0]

    for n in numbers[1:]:
        if n > maxnum:
            maxnum = n

    return maxnum
```

Now you can call:

```python
maximum(3, 2, 8)
```

or:

```python
maximum(1, 5, 9, -2, 2)
```

The function can receive different numbers of arguments.

The `*numbers` parameter collects the supplied positional arguments.

---

# 29. Return Values

`return` is one of the most important concepts in programming.

A function can calculate something and send the result back to the caller.

Example:

```python
def square(n):
    return n * n
```

Then:

```python
result = square(4)
```

Now:

```python
result
```

contains:

```text
16
```

The returned value can be:

* stored
* printed
* added
* multiplied
* passed to another function
* used in a condition
* used elsewhere in the program

---

# 30. return vs print()

This distinction is critical.

## print()

`print()` displays something.

```python
def square(n):
    print(n * n)
```

Calling:

```python
square(4)
```

displays:

```text
16
```

But the function does not give the calling code the value to work with.

## return

```python
def square(n):
    return n * n
```

Now:

```python
result = square(4)
```

The result can be used:

```python
print(result)
```

or:

```python
x = square(4) + square(5)
```

This is why functions that calculate values often use `return`.

---

# 31. None

In some other programming languages, a procedure may be described as a function that doesn't return a value.

In Python, if a function reaches the end without executing an explicit `return`, it returns:

```python
None
```

Example:

```python
def greet():
    print("Hello")
```

The function prints:

```text
Hello
```

but its return value is:

```python
None
```

Also important:

Once Python executes a `return`, the function immediately ends.

Example:

```python
def test():
    return 10
    print("This will never run")
```

The `print()` statement is unreachable because the function has already returned.

---

# 32. Scope

Scope determines where a variable exists and can be accessed.

Example:

```python
def greet():
    name = "Bob"

print(name)
```

This produces an error because:

```python
name
```

was created inside `greet()`.

It is local to that function.

A useful mental model:

```text
def greet():
    ┌──────────────────────┐
    │ name = "Bob"         │
    │                      │
    │ name exists here     │
    └──────────────────────┘

outside the function:

name does not exist
```

This is why functions receive values through parameters.

Example:

```python
def greet(name):
    print(name)
```

The function doesn't need access to a global `name`.

It receives the value through its parameter.

---

# 33. Global Variables and Side Effects

A global variable exists outside a function.

Example:

```python
emoticon = "v.v"
```

A function can read a global variable:

```python
def say(phrase):
    print(phrase + " " + emoticon)
```

Changing a global variable from inside a function requires the `global` keyword.

```python
emoticon = "v.v"

def main():
    global emoticon

    say("Is anyone there?")

    emoticon = ":D"

    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
```

Output:

```text
Is anyone there? v.v
Oh, hi! :D
```

## Side Effects

A side effect is something a function does besides simply calculating and returning a value.

Examples:

* Printing
* Modifying a global variable
* Writing to a file
* Changing external state

Global state should generally be used carefully because it can make programs harder to understand and debug.

---

# 34. Pure Functions

A pure function focuses on taking input and returning an output without modifying external state.

Example:

```python
def add_tax(price):
    return price * 1.15
```

The function:

* receives `price`
* calculates a value
* returns the result
* does not modify a global variable
* does not print anything

This makes the function predictable and reusable.

---

# 35. Function Design and Decomposition

Functions help break large programs into smaller tasks.

Instead of writing:

```python
print(price * 1.15)
print(price * 1.15)
print(price * 1.15)
```

you can create:

```python
def add_tax(price):
    return price * 1.15
```

Then:

```python
print(add_tax(100))
print(add_tax(200))
print(add_tax(300))
```

This provides:

* Reusability
* Organization
* Easier testing
* Easier debugging
* Less repetition

A useful question when designing programs is:

> "Is this task something I may need to perform more than once?"

If yes, a function may be appropriate.

Another useful question:

> "Is this piece of code doing one clear job?"

If not, consider breaking it into smaller functions.

---

# 36. Arguments and Object References

Python passes arguments to functions by object reference.

The parameter inside the function becomes another reference to the object.

This becomes especially important when comparing mutable and immutable objects.

## Immutable Objects

Examples include:

* Strings
* Numbers
* Tuples

If a function receives an immutable object and attempts to change the parameter itself, the original object outside the function is not changed.

Example:

```python
def change_name(name):
    name = "Bob"
```

The original string outside the function is not changed.

## Mutable Objects

Examples include:

* Lists
* Dictionaries
* Class instances

If a function receives a mutable object and modifies the object itself, the change can be visible outside the function.

This is an important concept to revisit when learning lists and dictionaries.

---

# 37. print() Parameters

`print()` has optional parameters.

Basic form:

```python
print(*objects, sep=' ', end='\n')
```

## sep

Controls the separator between multiple objects.

```python
print("A", "B", "C", sep="-")
```

Output:

```text
A-B-C
```

Normally:

```python
print("A", "B", "C")
```

produces:

```text
A B C
```

because the default separator is a space.

## end

Controls what happens after the printed content.

Normally, `print()` ends with a newline.

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

You can change it:

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

---

# 38. Escape Characters

A backslash can be used to represent special characters.

For example:

```python
print("He said \"Hello\"")
```

Output:

```text
He said "Hello"
```

Alternatively, use single quotes around the outer string:

```python
print('He said "Hello"')
```

Common escape sequences include:

```text
\n    newline
\t    tab
\"    double quote
\'    single quote
\\    backslash
```

---

# 39. Interactive Python

Python can be run directly from the terminal.

On Windows:

```text
python
```

This opens the interactive interpreter.

You can then enter:

```python
>>> 2 + 2
4
```

or:

```python
>>> name = "Lincia"
>>> print(name)
Lincia
```

To exit on Windows:

```text
Ctrl + Z
Enter
```

Interactive mode is useful for quickly testing Python behavior.

---

# 40. Reading Documentation

You do not need to memorize every Python function.

A major programming skill is learning how to read documentation.

Whenever you encounter a function, ask:

1. What does it do?
2. What arguments are required?
3. What arguments are optional?
4. What does it return?
5. Does it modify the original object?
6. What type does it return?

For example:

```python
print(*objects, sep=' ', end='\n')
```

You can determine:

* `objects` → values to print
* `sep` → separator between values
* `end` → what comes after the printed values

The goal is not to memorize everything.

The goal is to become comfortable finding out how something works.

---

# 41. Common Beginner Mistakes

## Mistake 1 — Missing Quotes

Incorrect:

```python
print(Hello)
```

Correct:

```python
print("Hello")
```

Without quotes, Python interprets `Hello` as a variable name.

---

## Mistake 2 — Forgetting input() Returns a String

Incorrect:

```python
age = input("Age: ")

print(age + 1)
```

Correct:

```python
age = int(input("Age: "))

print(age + 1)
```

---

## Mistake 3 — Expecting String Methods to Modify Strings

Incorrect:

```python
name = "john"

name.title()

print(name)
```

Output:

```text
john
```

Correct:

```python
name = name.title()

print(name)
```

---

## Mistake 4 — Confusing print() and return

This:

```python
def add(a, b):
    print(a + b)
```

is different from:

```python
def add(a, b):
    return a + b
```

The second version allows the calling code to use the result.

---

## Mistake 5 — Confusing Parameters and Arguments

```python
def greet(name):
```

`name` is the parameter.

```python
greet("Lincia")
```

`"Lincia"` is the argument.

---

# 42. Complete CS50 Code Walkthrough

## 42.1 hello.py — Input, Variables, and String Methods

```python
name = input("What's your name?").strip().title()

first, last = name.split(" ")

print(f"hello, {name}")
```

Example:

```text
What's your name? john smith
hello, John Smith
```

Concepts:

* `input()`
* variables
* `.strip()`
* `.title()`
* `.split()`
* f-strings
* multiple assignment

This:

```python
first, last = name.split(" ")
```

takes two resulting values and assigns them to two variables.

---

## 42.2 hello_functions.py — Functions and Scope

```python
def main():
    name = input("What's your name?")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()
```

If the user enters:

```text
Lincia
```

output:

```text
hello, Lincia
```

The function:

```python
hello(to="world")
```

has a default parameter.

If called without an argument:

```python
hello()
```

the default value is used.

The variable:

```python
name
```

exists inside `main()`.

Trying to access it outside `main()` would result in a `NameError`.

This demonstrates **scope**.

---

## 42.3 calculator.py — Return Values and Type Conversion

```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
```

Example:

```text
What's x? 4
x squared is 16
```

Important concepts:

```python
input()
```

returns a string.

Therefore:

```python
int(input(...))
```

converts the user's input into an integer.

The function:

```python
square(n)
```

returns a value rather than printing it.

---

## 42.4 return.py — Combining Return Values

```python
def area(length, width):
    return length * width


def main():
    house = area(50, 20)
    yard = area(50, 50)

    total = house + yard

    print(str(total) + " square feet")


main()
```

Calculations:

```text
house = 50 × 20
      = 1000

yard = 50 × 50
     = 2500

total = 1000 + 2500
      = 3500
```

Output:

```text
3500 square feet
```

The important idea is that `area()` returns values that can be reused.

---

## 42.5 machine.py — Global Variables and Side Effects

```python
emoticon = "v.v"


def main():
    global emoticon

    say("Is anyone there?")

    emoticon = ":D"

    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
```

Output:

```text
Is anyone there? v.v
Oh, hi! :D
```

This demonstrates:

* global variables
* the `global` keyword
* functions reading global state
* functions changing global state
* side effects

---

## 42.6 tip.py — Strings, replace(), Conversion, and Formatting

```python
def main():
    dollars = dollars_to_float(
        input("How much was the meal? Enter format $00.00 ")
    )

    percent = percent_to_float(
        input("What percentage would you like to tip? Enter format 00% ")
    )

    tip = dollars * percent

    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)


def percent_to_float(p):
    p = p.replace("%", "")
    return float(p) / 100


main()
```

Example:

```text
How much was the meal? $20.00
What percentage would you like to tip? 15%
Leave $3.00
```

Important ideas:

```python
.replace("$", "")
```

removes the currency symbol.

Because strings are immutable, the result is assigned back:

```python
d = d.replace("$", "")
```

The formatting:

```python
:.2f
```

means display the floating-point value to two decimal places.

---

## 42.7 einstein.py — Exponentiation and Large Integers

```python
def main():
    mass = int(input("m: "))
    formula(mass)


def formula(mass):
    c_squared = 300000000 ** 2
    energy = mass * c_squared

    print(f"e: {energy}")


main()
```

Formula:

```text
E = mc²
```

Example:

```text
m: 5
e: 450000000000000000
```

The operator:

```python
**
```

performs exponentiation.

Python integers can represent very large whole numbers exactly.

---

## 42.8 indoor.py — Method Chaining

```python
text = input("Enter text: ").lower()

print(text)
```

Example:

```text
Enter text: Hello World
hello world
```

This demonstrates calling a method directly on the result of `input()`.

---

## 42.9 playback.py — split() and join()

```python
text = input("Enter text: ")

result = "...".join(text.split())

print(result)
```

Example:

```text
Enter text: This is CS50
This...is...CS50
```

The inner operation runs first:

```python
text.split()
```

producing:

```python
["This", "is", "CS50"]
```

Then:

```python
"...".join(...)
```

combines the items.

---

# 43. Practice Work

The practice file contains exercises designed to reinforce functions, input, conversion, arithmetic, and formatted output.

---

## 43.1 Add Two Numbers

```python
def sum():
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")

    z = int(x) + int(y)

    print(f"The sum is {z}")


sum()
```

Concepts:

* function definition
* input
* conversion
* arithmetic
* f-strings

---

## 43.2 Subtract Two Numbers

```python
def subtract():
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")

    z = int(x) - int(y)

    print(f"The difference is {z}")


subtract()
```

---

## 43.3 Multiply Two Numbers

```python
def multiply():
    x = input("Enter the first number: ")
    y = input("Enter the second number: ")

    z = int(x) * int(y)

    print(f"The product is {z}")


multiply()
```

---

## 43.4 Calculate Rectangle Area

```python
def area():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))

    z = length * width

    print(f"The area is {z}")


area()
```

Formula:

```text
area = length × width
```

---

## 43.5 Calculate Circle Circumference

```python
def circumference():
    pi = 3.14159
    radius = float(input("Enter the radius: "))

    total = 2 * pi * radius

    print(f"The circumference is {total:.2f}")


circumference()
```

Formula:

```text
C = 2πr
```

---

## 43.6 Celsius to Fahrenheit

```python
def ctof():
    celsius = int(input("Enter temperature in Celsius: "))

    fahrenheit = (celsius * 9 / 5) + 32

    print(f"{celsius}°C = {fahrenheit}°F")


ctof()
```

Formula:

```text
°F = (°C × 9/5) + 32
```

---

## 43.7 Fahrenheit to Celsius

```python
def ftoc():
    fahrenheit = int(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5 / 9

    print(f"{fahrenheit}°F = {celsius:.2f}°C")


ftoc()
```

Formula:

```text
°C = (°F - 32) × 5/9
```

---

## 43.8 Calculate a 15% Tip

```python
def tip():
    bill = float(input("Enter the bill amount: "))

    tip_amount = bill * 0.15

    print(f"Tip amount: ${tip_amount:.2f}")

    total = bill + tip_amount

    print(f"Total bill with tip: ${total:.2f}")


tip()
```

---

## 43.9 Calculate 12.5% Tax

```python
def tax():
    bill = float(input("Enter the bill amount: "))

    tax = bill * 0.125

    total = float(bill + tax)

    print(f"Total: ${total:.2f}")


tax()
```

---

## 43.10 Calculate Monthly Savings

```python
def savings():
    monthly_savings = int(input("Monthly savings: "))
    months = int(input("Months: "))

    total = monthly_savings * months

    print(f"Total savings = {total}")


savings()
```

---

## 43.11 Remaining Practice Ideas

The practice file also contains placeholders for:

* A loan interest calculator
* A BMI calculator

These were not completed in the practice file.

---

# 44. Practical Function Patterns

These patterns are worth remembering.

## Function With No Parameters

```python
def greet():
    print("Hello!")
```

Call it:

```python
greet()
```

---

## Function With Parameters

```python
def greet(name):
    print(f"Hello, {name}!")
```

Call it:

```python
greet("Lincia")
```

---

## Function That Returns a Value

```python
def add(a, b):
    return a + b
```

Use it:

```python
result = add(5, 10)
```

---

## Function With a Default Parameter

```python
def greet(name="User"):
    print(f"Hello, {name}!")
```

---

## Function That Returns Based on a Condition

```python
def is_adult(age):
    if age >= 18:
        return True

    return False
```

---

## Finding the Largest Value

A common programming pattern:

```python
largest = 0

for number in numbers:
    if number > largest:
        largest = number
```

The general idea is:

1. Start with a value.
2. Examine each item.
3. Compare it with the current best value.
4. Replace the best value when appropriate.

---

## Counting Occurrences

```python
count = 0

for item in items:
    if item == target:
        count += 1
```

This pattern counts how many times something appears.

---

## Looping Through a Dictionary

```python
for key, value in data.items():
    print(key, value)
```

This becomes especially useful when working with dictionaries later.

---

## Finding the Highest Dictionary Value

```python
highest = max(data, key=data.get)
```

This finds the key associated with the highest value.

---

# 45. Six Questions for Learning Python

Whenever you encounter a new function, method, or programming concept, ask:

### 1. What problem does this solve?

Understand the purpose before memorizing syntax.

### 2. What does it return?

This is especially important with functions and methods.

### 3. Does it modify the original object?

For example, strings are immutable.

A method like:

```python
text.upper()
```

returns a new string.

### 4. What arguments can it accept?

Determine:

* required arguments
* optional arguments
* default values
* positional arguments
* keyword arguments

### 5. What mistakes do beginners commonly make?

Understanding common errors can prevent them.

### 6. Can I explain it in my own words?

If you can explain a concept without simply repeating the documentation, you probably understand it better.

---

# 46. Key Takeaways

By the end of Lecture 0, the major ideas are:

* Python executes code from top to bottom.
* Variables store references to values.
* `=` is the assignment operator.
* Variables can be reassigned.
* `input()` always returns a string.
* `print()` displays information.
* f-strings allow variables and expressions inside strings.
* Python has multiple data types.
* `int` represents whole numbers.
* `float` represents decimal numbers.
* `complex` represents complex numbers.
* `str` represents text.
* Strings are immutable.
* String methods return new strings.
* String methods can be chained.
* `split()` converts a string into a list.
* `join()` combines values into a string.
* `type()` identifies a value's type.
* `int()` and `float()` perform type conversion.
* `/` performs division.
* `//` performs floor division.
* `%` gives the remainder.
* `**` performs exponentiation.
* Functions allow code to be reused.
* Parameters are placeholders.
* Arguments are actual values.
* Functions can have default parameters.
* Arguments can be passed positionally.
* Arguments can be passed by keyword.
* `*args` allows a variable number of positional arguments.
* `return` sends a value back to the caller.
* `print()` and `return` are fundamentally different.
* A function without an explicit return produces `None`.
* Code after `return` does not execute.
* Variables have scope.
* Local variables exist within their scope.
* Global variables exist outside functions.
* Global state can create side effects.
* Pure functions are easier to reason about.
* Python passes arguments by object reference.
* Mutable and immutable objects behave differently when passed to functions.
* Documentation is a core programming skill.
* You do not need to memorize everything.
* You need to understand how to find and verify information.

---

# 47. Mini Practice

Try these without looking at your notes.

## Exercise 1 — Greeting

Ask the user for their name and print a greeting.

Expected idea:

```text
What's your name? Lincia
Hello, Lincia
```

---

## Exercise 2 — Next Year

Ask the user for their age and print how old they will be next year.

Example:

```text
Age: 35
Next year you will be 36.
```

---

## Exercise 3 — Name Formatting

Ask the user for their full name and convert it to title case.

Input:

```text
john smith
```

Output:

```text
John Smith
```

---

## Exercise 4 — Split a Name

Ask for a first and last name and split them into separate variables.

```python
first, last = name.split(" ")
```

---

## Exercise 5 — f-String

Ask the user for their name and age.

Print a sentence containing both.

---

## Exercise 6 — Calculator Function

Create:

```python
def add(a, b):
    return a + b
```

Then use the returned value.

---

## Exercise 7 — Temperature Converter

Create functions for:

```text
Celsius → Fahrenheit
Fahrenheit → Celsius
```

---

## Exercise 8 — Loan Calculator

Create a function that receives the relevant values and calculates loan interest.

---

## Exercise 9 — BMI Calculator

Create a function that receives weight and height and calculates BMI.

---

## Exercise 10 — Refactor

Take an older program and identify repeated pieces of code.

Ask:

> "Can this repeated task become a function?"

Then refactor the program.

---

# 48. Further Practice Ideas

The original practice notes suggest building small practical functions around real-world calculations.

Good exercises include:

### Financial

* Tip calculator
* Tax calculator
* Monthly savings calculator
* Loan interest calculator
* Loan payment calculator
* Compound interest calculator
* Currency converter

### Mathematics

* Rectangle area
* Circle circumference
* Temperature conversion
* BMI calculator
* Percentage calculator

### Text Processing

* Name formatter
* Text cleaner
* Word counter
* String validator
* Currency string converter
* Percentage string converter

The goal is not to build complicated applications yet.

The goal is to become comfortable with:

```text
INPUT
  ↓
CONVERT
  ↓
PROCESS
  ↓
RETURN
  ↓
DISPLAY
```

For example:

```python
def calculate_tip(bill, percentage):
    return bill * percentage
```

Then:

```python
bill = float(input("Bill: "))
percentage = float(input("Tip percentage: ")) / 100

tip = calculate_tip(bill, percentage)

print(f"Tip: ${tip:.2f}")
```

This is the beginning of program decomposition.

---

# Final Mental Model

The most important thing to take away from Lecture 0 is not individual pieces of syntax.

Think about a Python program as a collection of **values, operations, and reusable functions**.

A typical flow looks like:

```text
USER
 ↓
input()
 ↓
STRING DATA
 ↓
TYPE CONVERSION
 ↓
VARIABLE
 ↓
FUNCTION
 ↓
PROCESSING
 ↓
RETURN VALUE
 ↓
OUTPUT
 ↓
print()
```

For example:

```python
def calculate_total(price, tax):
    return price + tax


price = float(input("Price: "))
tax = float(input("Tax: "))

total = calculate_total(price, tax)

print(f"Total: ${total:.2f}")
```

Here you are using nearly everything from Lecture 0:

* Variables
* Input
* Strings
* Type conversion
* Floats
* Functions
* Parameters
* Arguments
* Return values
* Arithmetic
* f-strings
* Output

That is the foundation you will build on throughout the rest of Python.

> **Reminder:** You do not need to memorize everything after one lecture. The goal is to understand the concepts, practice them repeatedly, and learn how to look things up when you forget syntax.
