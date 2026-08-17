# CS50 Lecture 0: Functions & Variables

> **Goal:** Understand the basic building blocks of Python—variables, functions, input/output, strings, and data types. These concepts form the foundation for everything else you'll learn.

---

# Big Idea

Python is an **interpreted language**, meaning it reads your code **from top to bottom** and executes each instruction one at a time.

The core building blocks are:

- **Functions** → Perform tasks
- **Variables** → Store values
- **Data Types** → Describe what kind of value is stored

---

# Variables

Variables store values in memory.

```python
name = "Lincia"
age = 27
```

## Assignment Operator (`=`)

The `=` operator **assigns** a value to a variable.

```python
name = "Lincia"
```

This means:

> Store `"Lincia"` inside the variable `name`.

It **does not** mean "equals."

## Variables Can Be Reassigned

Variables can be updated by assigning a new value.

```python
name = "John"
```

The old value is replaced.

---

# Input and Output

## `input()`

The `input()` function asks the user for input.

```python
name = input("What's your name? ")
```

### Important

`input()` **always returns a string**, even if the user types a number.

```python
age = input("Age: ")
```

If the user types:

```
25
```

Python stores:

```python
"25"
```

not

```python
25
```

To use the value as a number:

```python
age = int(input("Age: "))
```

---

## `print()`

The `print()` function displays output on the screen.

```python
print("Hello")
```

You can print multiple values.

```python
print("Hello", "World")
```

Output:

```
Hello World
```

---

## f-Strings

The recommended way to insert variables into text.

```python
name = "Lincia"

print(f"Hello, {name}")
```

Output:

```
Hello, Lincia
```

---

# Functions

A function is a reusable block of code that performs a task.

Examples:

```python
print("Hello")
len("hello")
round(3.14159, 2)
```

Functions can:

- Perform an action
- Return a value
- Or both

---

## Function Arguments

Arguments are the values passed into a function.

```python
print("Hello", "World")
```

Here:

- `"Hello"` is an argument.
- `"World"` is another argument.

---

# Return Values

One of the most important programming concepts.

A function may return a value that you can store or use later.

Example:

```python
length = len("banana")
```

Process:

```
"banana"
     ↓
len()
     ↓
6
     ↓
Stored in length
```

Another example:

```python
name = input("Name: ")
```

If the user types:

```
Bob
```

Then:

```python
name == "Bob"
```

---

## Ask Yourself

Whenever you use a function, ask:

> **What value does this function return?**

Understanding return values makes programming much easier.

---

# String Methods

Strings have many built-in methods.

```python
name = " john smith "
```

## Remove Whitespace

```python
name.strip()
```

Removes spaces from both ends.

---

## Capitalize First Letter

```python
name.capitalize()
```

Output:

```
John smith
```

---

## Title Case

```python
name.title()
```

Output:

```
John Smith
```

---

## Method Chaining

You can call multiple methods in one line.

```python
name = " john smith ".strip().title()
```

Python performs them from left to right.

---

## Common String Methods

| Method | Purpose |
|---------|----------|
| `.lower()` | Convert to lowercase |
| `.upper()` | Convert to uppercase |
| `.title()` | Capitalize each word |
| `.capitalize()` | Capitalize first letter only |
| `.strip()` | Remove surrounding whitespace |
| `.replace()` | Replace text |
| `.split()` | Split into a list |
| `.join()` | Join a list into a string |
| `.find()` | Find the position of text |
| `.startswith()` | Check beginning of string |
| `.endswith()` | Check ending of string |

---

# Strings Are Immutable

Strings **cannot be changed in place**.

Methods create **new strings** instead.

Incorrect:

```python
name = "john"

name.title()

print(name)
```

Output:

```
john
```

Correct:

```python
name = name.title()

print(name)
```

Output:

```
John
```

Whenever you want to keep the result of a string method, assign it back to a variable.

---

# Splitting Strings

`split()` breaks a string into parts.

```python
name = "John Smith"

first, last = name.split(" ")
```

Result:

```python
first = "John"
last = "Smith"
```

---

# Data Types

Python has several built-in data types.

| Type | Description | Example |
|------|-------------|---------|
| `str` | Text | `"hello"` |
| `int` | Whole numbers | `10` |
| `float` | Decimal numbers | `3.14` |
| `list` | Collection of values | `[1, 2, 3]` |

---

## Converting Input

Since `input()` returns a string:

```python
age = input("Age: ")
```

This will fail:

```python
age + 1
```

Correct:

```python
age = int(input("Age: "))

print(age + 1)
```

---

# Operators

## Arithmetic Operators

| Operator | Meaning |
|----------|---------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor Division |
| `%` | Modulus (remainder) |
| `**` | Exponentiation |

Example:

```python
10 % 3
```

Output:

```
1
```

---

# Comments

Single-line comment:

```python
# This is a comment
```

Multi-line comment (docstring style):

```python
"""
Long explanation
"""
```

### Best Practice

Comments should explain **why**, not **what**.

---

# Parameters vs Arguments

A common source of confusion.

## Parameter

A placeholder in a function definition.

```python
def greet(name):
```

`name` is the parameter.

---

## Argument

The actual value passed into the function.

```python
greet("Bob")
```

`"Bob"` is the argument.

---

# Scope

Variables only exist where they are created.

```python
def greet():
    name = "Bob"

print(name)
```

This produces an error because `name` only exists inside `greet()`.

---

# Print Parameters

`print()` has useful optional parameters.

## `sep`

Separator between printed objects.

```python
print("A", "B", "C", sep="-")
```

Output:

```
A-B-C
```

---

## `end`

Controls what is printed at the end.

```python
print("Hello", end=" ")
print("World")
```

Output:

```
Hello World
```

Normally, `print()` ends with a newline (`\n`).

---

# Escape Characters

Use a backslash (`\`) to include special characters.

```python
print("He said \"Hello\"")
```

Or use single quotes outside:

```python
print('He said "Hello"')
```

---

# Interactive Python Mode

Run Python directly in your terminal:

```text
python
```

Then type Python commands one at a time.

Exit on Windows:

```text
Ctrl + Z
Enter
```

---

# Common Beginner Mistakes

## Missing Quotes

Incorrect:

```python
print(Hello)
```

Correct:

```python
print("Hello")
```

---

## Forgetting That `input()` Returns a String

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

# Integers vs Floats

## Integers (`int`)

Can represent extremely large whole numbers.

```python
999999999999999999
```

---

## Floats (`float`)

Store decimal numbers but have limited precision.

```python
3.14159265358979323846
```

Floating-point values may lose precision because of how computers store decimal numbers.

---

# The `round()` Function

Syntax:

```python
round(number[, ndigits])
```

Examples:

```python
round(3.14159)
```

Output:

```
3
```

```python
round(3.14159, 2)
```

Output:

```
3.14
```

---

# Reading Documentation

Every programmer reads documentation.

Don't try to memorize everything.

Instead, learn to answer these questions:

- What does the function do?
- What arguments are required?
- Which arguments are optional?
- What does it return?

Example:

```python
print(*objects, sep=' ', end='\n')
```

- `objects` → Values to print
- `sep` → Separator between values
- `end` → What is printed after the last value

---

# Six Questions to Ask When Learning Anything

Whenever you encounter a new function, method, or concept, ask yourself:

1. What problem does this solve?
2. What does it return?
3. Does it modify the original object?
4. What arguments can it accept?
5. What mistakes do beginners commonly make?
6. Can I explain it in my own words?

These questions help you understand concepts instead of memorizing syntax.

---

# Key Takeaways

- Python executes code from top to bottom.
- Variables store values.
- `=` is the assignment operator, not equality.
- Functions perform actions and/or return values.
- `input()` always returns a string.
- Use `int()` or `float()` to convert numeric input.
- Strings are immutable; methods return new strings.
- Methods can be chained together.
- Variables only exist within their scope.
- Read documentation to understand behavior instead of memorizing it.

---

# Mini Practice

Try completing these without looking at your notes:

1. Ask the user for their name and print a greeting.
2. Ask the user for their age and print how old they'll be next year.
3. Format a full name using title case.
4. Split a full name into first and last names.
5. Print a sentence using an f-string.

> **Reminder:** You don't need to master everything after one lecture. Revisit these concepts often—they'll appear throughout the rest of CS50 and your Python journey.