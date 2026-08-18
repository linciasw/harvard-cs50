# Python Exceptions

## Table of Contents

- [Python Exceptions](#python-exceptions)
  - [Table of Contents](#table-of-contents)
- [1. What Are Exceptions?](#1-what-are-exceptions)
- [2. Why Exceptions Matter](#2-why-exceptions-matter)
- [3. How Exceptions Work](#3-how-exceptions-work)
- [4. The `try` Statement](#4-the-try-statement)
- [5. The `except` Statement](#5-the-except-statement)
- [6. The `else` Clause](#6-the-else-clause)
- [7. The `finally` Clause](#7-the-finally-clause)
- [8. Common Python Exceptions](#8-common-python-exceptions)
  - [SyntaxError](#syntaxerror)
    - [Meaning](#meaning)
  - [IndentationError](#indentationerror)
    - [Meaning](#meaning-1)
  - [NameError](#nameerror)
    - [Meaning](#meaning-2)
  - [TypeError](#typeerror) 
    - [Meaning](#meaning-3)
  - [ValueError](#valueerror)
    - [Meaning](#meaning-4)
  - [IndexError](#indexerror)
    - [Meaning](#meaning-5)
  - [KeyError](#keyerror)
    - [Meaning](#meaning-6)
  - [AttributeError](#attributeerror)
    - [Meaning](#meaning-7)
  - [ZeroDivisionError](#zerodivisionerror)
    - [Meaning](#meaning-8)
  - [FileNotFoundError](#filenotfounderror)
    - [Meaning](#meaning-9)
  - [PermissionError](#permissionerror)
    - [Meaning](#meaning-10)
  - [ModuleNotFoundError](#modulenotfounderror)
    - [Meaning](#meaning-11)
  - [ImportError](#importerror)
    - [Meaning](#meaning-12)
  - [RecursionError](#recursionerror)
    - [Meaning](#meaning-13)
- [9. Handling Multiple Exceptions](#9-handling-multiple-exceptions)
- [10. Multiple Exceptions in One Handler](#10-multiple-exceptions-in-one-handler)
- [11. Exceptions and `while` Loops](#11-exceptions-and-while-loops)
    - [How this works](#how-this-works)
- [12. Using `pass`](#12-using-pass)
- [13. Creating Reusable Exception Handling](#13-creating-reusable-exception-handling)
- [14. Raising Exceptions with `raise`](#14-raising-exceptions-with-raise)
- [15. Exception Hierarchy](#15-exception-hierarchy)
- [16. Important Exception Relationships](#16-important-exception-relationships)
  - [Arithmetic Errors](#arithmetic-errors)
  - [Import Errors](#import-errors)
  - [Lookup Errors](#lookup-errors)
  - [Name Errors](#name-errors)
  - [Operating System Errors](#operating-system-errors)
  - [Syntax Errors](#syntax-errors)
  - [Unicode Errors](#unicode-errors)
- [17. Complete Exception Hierarchy](#17-complete-exception-hierarchy)
- [18. Exception Mental Models](#18-exception-mental-models)
  - [TypeError](#typeerror-1)
  - [ValueError](#valueerror-1)
  - [IndexError](#indexerror-1)
  - [KeyError](#keyerror-1)
  - [NameError](#nameerror-1)
  - [AttributeError](#attributeerror-1)
  - [SyntaxError](#syntaxerror-1)
- [19. Defensive Programming and Security](#19-defensive-programming-and-security)
- [20. Debugging Exceptions](#20-debugging-exceptions)
  - [`print()` Debugging](#print-debugging)
  - [Breakpoints](#breakpoints)
- [21. Quick Debugging Guide](#21-quick-debugging-guide)
- [22. Exceptions to Learn Later](#22-exceptions-to-learn-later)
- [23. Useful Exception-Handling Patterns](#23-useful-exception-handling-patterns)
  - [Catch a Specific Exception](#catch-a-specific-exception)
  - [Keep Asking Until Valid Input](#keep-asking-until-valid-input)
  - [Use `else` After Successful Conversion](#use-else-after-successful-conversion)
  - [Return Directly From `try`](#return-directly-from-try)
  - [Handle Multiple Exceptions Separately](#handle-multiple-exceptions-separately)
  - [Handle Multiple Exceptions Together](#handle-multiple-exceptions-together)
  - [Raise Your Own Exception](#raise-your-own-exception)
- [24. What I Know Now](#24-what-i-know-now)
- [25. Things I'm Still Learning](#25-things-im-still-learning)
- [26. The Big Picture](#26-the-big-picture)
- [My Own Examples](#my-own-examples)

---

# 1. What Are Exceptions?

An **exception** is an event that occurs during the execution of a program when something unexpected or invalid happens.

Python can automatically **raise** an exception when an operation cannot be completed.

Examples:

```python
int("cat")
```

raises:

```text
ValueError
```

Trying to access a dictionary key that doesn't exist:

```python
distances = {
    "Voyager 1": "163"
}

print(distances["James Webb Space Telescope"])
```

raises:

```text
KeyError
```

Dividing by zero:

```python
result = 10 / 0
```

raises:

```text
ZeroDivisionError
```

Using a variable that doesn't exist:

```python
print(x)
```

raises:

```text
NameError
```

Exceptions are **Python objects** that represent these errors.

---

# 2. Why Exceptions Matter

Programs should be written with error handling in mind.

This is sometimes called **defensive programming**.

Defensive programming means anticipating problems and deciding how the program should respond when they happen.

Exceptions allow us to separate:

* The code that performs the actual task
* The code that decides what to do when something goes wrong

Instead of putting error-handling logic throughout the program, Python allows an exception to be raised and handled at an appropriate level.

For example, instead of assuming that a user will always enter a valid integer:

```python
x = int(input("What's x? "))
```

we can anticipate invalid input:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
```

This makes the program more robust.

---

# 3. How Exceptions Work

The general flow is:

```text
Program runs
    ↓
Python encounters an invalid/unexpected operation
    ↓
An exception is raised
    ↓
Python looks for an appropriate handler
    ↓
Matching `except` block runs
    ↓
Program continues according to the surrounding control flow
```

For example:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
```

If the user enters:

```text
5
```

there is no exception.

If the user enters:

```text
cat
```

`int()` cannot convert `"cat"` to an integer, so Python raises `ValueError`.

Python then looks for:

```python
except ValueError:
```

and executes its code.

---

# 4. The `try` Statement

The `try` block contains code that **might cause an exception**.

Basic structure:

```python
try:
    # code that might cause an exception
except ValueError:
    # what to do if ValueError occurs
```

Important:

If an exception occurs inside the `try` block, Python stops executing the remaining code in that `try` block.

It then looks for an appropriate `except` handler.

---

# 5. The `except` Statement

`except` tells Python what to do when a particular exception occurs.

Example:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
```

The `except` block only handles the exception specified:

```python
ValueError
```

It is generally better to catch the **specific exception you expect** instead of catching every possible exception.

---

# 6. The `else` Clause

The `else` block runs **only if the `try` block succeeds**.

Example:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

The flow is:

```text
try succeeds
    ↓
else runs

try raises exception
    ↓
matching except runs
    ↓
else does not run
```

This is particularly useful when a variable is created inside the `try` block.

Consider:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(x)
```

If the user enters `"cat"`, the assignment:

```python
x = int(...)
```

never successfully completes.

Therefore `x` does not exist.

Trying:

```python
print(x)
```

would then produce:

```text
NameError
```

Using `else` prevents us from using `x` unless the conversion succeeded:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

---

# 7. The `finally` Clause

A `finally` block can be used for code that should run regardless of whether an exception occurred.

General structure:

```python
try:
    # code
except SomeException:
    # handle exception
else:
    # runs if try succeeds
finally:
    # runs regardless
```

The overall structure is:

```python
try:
    body
except exception_type:
    exception_code
else:
    else_body
finally:
    finally_body
```

`finally` becomes especially useful when working with resources that need cleanup.

---

# 8. Common Python Exceptions

## SyntaxError

### Meaning

The Python code does not follow Python's syntax rules.

Example:

```python
if age >= 18
    print("Adult")
```

Think:

> "I wrote invalid Python."

---

## IndentationError

### Meaning

The indentation is incorrect.

Example:

```python
if age >= 18:
print("Adult")
```

Think:

> "My indentation is wrong."

`IndentationError` is a subclass of `SyntaxError`.

---

## NameError

### Meaning

Python does not know the variable or name you're trying to use.

Example:

```python
print(username)
```

if `username` was never defined.

Think:

> "Does this variable or name exist?"

---

## TypeError

### Meaning

The wrong type is being used for an operation.

Example:

```python
age = 35

print("Age: " + age)
```

You cannot concatenate a string and an integer this way.

Think:

> "Am I using the wrong TYPE?"

---

## ValueError

### Meaning

The type is appropriate, but the value is invalid for the operation.

Example:

```python
number = int("hello")
```

`"hello"` is a string, so the type is appropriate for `int()` to receive.

However, `"hello"` is not a valid representation of an integer.

Therefore:

```text
ValueError
```

Think:

> "Is this the right TYPE but the wrong VALUE?"

Another example:

```python
x = float("cat")
```

also produces:

```text
ValueError
```

The function's contract determines what values it can accept.

---

## IndexError

### Meaning

You attempted to access a sequence index that does not exist.

Example:

```python
numbers = [10, 20, 30]

print(numbers[5])
```

The valid indexes are:

```text
0
1
2
```

Think:

> "Does that position exist?"

---

## KeyError

### Meaning

You attempted to access a dictionary key that does not exist.

Example:

```python
person = {
    "name": "Lincia",
    "age": 35
}

print(person["salary"])
```

Think:

> "Does that dictionary key exist?"

---

## AttributeError

### Meaning

An object does not have the attribute or method you are trying to access.

Example:

```python
name = "Lincia"

name.append("!")
```

Strings do not have an `append()` method.

Think:

> "Does this object have that method or attribute?"

---

## ZeroDivisionError

### Meaning

You attempted to divide by zero.

Example:

```python
result = 10 / 0
```

Think:

> "Did I divide by zero?"

---

## FileNotFoundError

### Meaning

Python attempted to access a file or directory that does not exist.

Example:

```python
with open("missing.txt") as file:
    data = file.read()
```

Think:

> "Does this file actually exist?"

---

## PermissionError

### Meaning

Python does not have permission to perform the requested operation.

Example:

```python
with open("protected.txt", "w") as file:
    file.write("Hello")
```

Think:

> "Do I have permission to do this?"

---

## ModuleNotFoundError

### Meaning

Python cannot find the module being imported.

Example:

```python
import pandas
```

If the module is not installed or cannot be found:

```text
ModuleNotFoundError
```

Think:

> "Can Python find this module?"

---

## ImportError

### Meaning

Something went wrong while importing something.

Example:

```python
from math import something_that_doesnt_exist
```

Think:

> "Something went wrong with my import."

`ModuleNotFoundError` is a subclass of `ImportError`.

---

## RecursionError

### Meaning

The program exceeded Python's recursion limit.

Example:

```python
def count():
    count()

count()
```

The function keeps calling itself.

Think:

> "My recursion went too deep."

---

# 9. Handling Multiple Exceptions

A program can have multiple `except` blocks.

General structure:

```python
try:
    body

except exception_type1 as var1:
    exception_code1

except exception_type2 as var2:
    exception_code2

else:
    else_body

finally:
    finally_body
```

Example:

```python
try:
    au = float(distances[spacecraft])

except KeyError:
    print(f"'{spacecraft}' is not in dictionary")

except ValueError:
    print(f"Can't convert '{distances[spacecraft]}' to a float")
```

The first matching exception handler is used.

Be as specific as possible when handling exceptions.

Avoid catching every possible exception unless there is a good reason.

---

# 10. Multiple Exceptions in One Handler

If multiple exceptions should be handled in exactly the same way, they can be grouped into a tuple.

Example:

```python
while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)

        if x > y:
            continue

        percentage = (x / y) * 100

    except (ValueError, ZeroDivisionError):
        pass

    else:
        break
```

This means:

```python
except (ValueError, ZeroDivisionError):
```

will catch either:

```text
ValueError
```

or:

```text
ZeroDivisionError
```

The same handling logic applies to both.

---

# 11. Exceptions and `while` Loops

Exceptions work particularly well with loops when repeatedly asking users for valid input.

Example:

```python
while True:
    try:
        x = int(input("What's x? "))

    except ValueError:
        print("x is not an integer")

    else:
        break

print(f"x is {x}")
```

### How this works

`while True` creates an infinite loop:

```text
Ask for input
    ↓
Try to convert it
    ↓
Exception?
 ┌───────────────┐
 │               │
Yes              No
 │               │
 ↓               ↓
except          else
 │               │
 ↓               ↓
loop again      break
                 ↓
              continue
```

`break` exits the loop once valid input has been received.

This creates a common pattern:

```text
Keep asking
    ↓
Validate input
    ↓
Invalid?
    → Try again
    ↓
Valid?
    → Break
```

---

# 12. Using `pass`

`pass` means:

> Do nothing.

It can be used when an exception is intentionally caught but no action needs to be taken at that point.

Example:

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
```

If the user enters something invalid, `ValueError` is caught and nothing happens inside the `except` block.

The loop then naturally starts another iteration.

`pass` is therefore useful when the loop itself is responsible for retrying.

---

# 13. Creating Reusable Exception Handling

Instead of repeating the same input-validation code throughout a program, we can create a function.

Example:

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print("x is not an integer")
```

Then:

```python
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

main()
```

The important idea is **separation of responsibilities**.

`get_int()` handles:

* Getting input
* Converting input
* Handling invalid input
* Repeating until valid

The caller decides what to do with the returned value:

```python
x = get_int("What's x? ")
```

This makes the validation logic reusable.

---

# 14. Raising Exceptions with `raise`

Python allows us to deliberately raise an exception using:

```python
raise
```

Example:

```python
def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Minutes must be greater than 0.")

    return minutes / miles
```

Here, the program explicitly raises:

```python
ValueError
```

because continuing would be invalid.

General pattern:

```python
if invalid_condition:
    raise ValueError("Explanation of the problem.")
```

This is useful when the programmer wants to enforce a rule or contract.

---

# 15. Exception Hierarchy

Python organizes exceptions into a hierarchy.

At the top:

```text
BaseException
    └── Exception
```

Many exceptions commonly encountered in normal programs are subclasses of:

```python
Exception
```

For example:

```python
try:
    number = int("hello")

except Exception:
    print("Something went wrong.")
```

This works because:

```text
ValueError
    ↓
Exception
```

`ValueError` is a subclass of `Exception`.

However, catching the specific exception is usually preferable:

```python
except ValueError:
```

rather than:

```python
except Exception:
```

because it makes it clearer what problem the program expects and handles.

---

# 16. Important Exception Relationships

## Arithmetic Errors

```text
ArithmeticError
├── FloatingPointError
├── OverflowError
└── ZeroDivisionError
```

Example:

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## Import Errors

```text
ImportError
└── ModuleNotFoundError
```

Example:

```python
try:
    import pandas

except ModuleNotFoundError:
    print("Pandas is not installed.")
```

---

## Lookup Errors

```text
LookupError
├── IndexError
└── KeyError
```

`IndexError` applies to invalid sequence positions.

```python
numbers = [10, 20, 30]

try:
    print(numbers[10])

except IndexError:
    print("That index does not exist.")
```

`KeyError` applies to missing dictionary keys.

```python
person = {
    "name": "Lincia"
}

try:
    print(person["age"])

except KeyError:
    print("That key does not exist.")
```

---

## Name Errors

```text
NameError
└── UnboundLocalError
```

Example:

```python
print(username)
```

produces:

```text
NameError
```

---

## Operating System Errors

```text
OSError
├── BlockingIOError
├── ChildProcessError
├── ConnectionError
│   ├── BrokenPipeError
│   ├── ConnectionAbortedError
│   ├── ConnectionRefusedError
│   └── ConnectionResetError
├── FileExistsError
├── FileNotFoundError
├── InterruptedError
├── IsADirectoryError
├── NotADirectoryError
├── PermissionError
├── ProcessLookupError
└── TimeoutError
```

These are commonly encountered when working with:

* Files
* Directories
* Processes
* Networking
* Operating-system resources

---

## Syntax Errors

```text
SyntaxError
└── IndentationError
    └── TabError
```

Example:

```python
if age >= 18
    print("Adult")
```

produces:

```text
SyntaxError
```

---

## Unicode Errors

```text
UnicodeError
├── UnicodeDecodeError
├── UnicodeEncodeError
└── UnicodeTranslateError
```

These are mainly encountered when working with text encodings.

---

# 17. Complete Exception Hierarchy

The major built-in hierarchy is:

```text
BaseException
│
├── BaseExceptionGroup
│
├── GeneratorExit
│
├── KeyboardInterrupt
│
├── SystemExit
│
└── Exception
    │
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    │
    ├── AssertionError
    │
    ├── AttributeError
    │
    ├── BufferError
    │
    ├── EOFError
    │
    ├── ImportError
    │   └── ModuleNotFoundError
    │
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    │
    ├── MemoryError
    │
    ├── NameError
    │   └── UnboundLocalError
    │
    ├── OSError
    │   ├── BlockingIOError
    │   ├── ChildProcessError
    │   ├── ConnectionError
    │   │   ├── BrokenPipeError
    │   │   ├── ConnectionAbortedError
    │   │   ├── ConnectionRefusedError
    │   │   └── ConnectionResetError
    │   │
    │   ├── FileExistsError
    │   ├── FileNotFoundError
    │   ├── InterruptedError
    │   ├── IsADirectoryError
    │   ├── NotADirectoryError
    │   ├── PermissionError
    │   ├── ProcessLookupError
    │   └── TimeoutError
    │
    ├── RecursionError
    │
    ├── RuntimeError
    │
    ├── StopAsyncIteration
    │
    ├── StopIteration
    │
    ├── SyntaxError
    │   └── IndentationError
    │       └── TabError
    │
    ├── SystemError
    │
    ├── TypeError
    │
    ├── ValueError
    │   └── UnicodeError
    │       ├── UnicodeDecodeError
    │       ├── UnicodeEncodeError
    │       └── UnicodeTranslateError
    │
    └── Warning
```

I do **not** need to memorize the entire hierarchy.

The important concepts are:

* Exceptions are objects.
* Exceptions can inherit from other exceptions.
* More specific exceptions can be caught individually.
* A broader exception can catch multiple related exceptions.
* The hierarchy becomes more useful after learning inheritance and object-oriented programming.

---

# 18. Exception Mental Models

The fastest way to become comfortable with exceptions is to recognize patterns.

## TypeError

```text
WRONG TYPE
```

Ask:

> "Am I using the wrong kind of object?"

Example:

```python
"Age: " + 35
```

---

## ValueError

```text
RIGHT TYPE
WRONG VALUE
```

Ask:

> "Is this the right type, but an invalid value?"

Example:

```python
int("hello")
```

---

## IndexError

```text
POSITION DOESN'T EXIST
```

Ask:

> "Does this index exist?"

Example:

```python
numbers[10]
```

---

## KeyError

```text
KEY DOESN'T EXIST
```

Ask:

> "Does this dictionary contain this key?"

Example:

```python
person["salary"]
```

---

## NameError

```text
NAME DOESN'T EXIST
```

Ask:

> "Did I define this variable?"

Example:

```python
print(total)
```

when `total` was never defined.

---

## AttributeError

```text
ATTRIBUTE OR METHOD DOESN'T EXIST
```

Ask:

> "Does this object have this method or attribute?"

Example:

```python
name.append("!")
```

---

## SyntaxError

```text
PYTHON CODE IS INVALID
```

Ask:

> "Did I write valid Python syntax?"

---

# 19. Defensive Programming and Security

Exception handling contributes to robust software because programs cannot assume that every input or operation will behave as expected.

Possible problems include:

* Users entering unexpected input
* Files not existing
* Malformed data
* External systems failing
* Network failures
* Operating-system failures
* Someone intentionally providing unexpected input

Exception handling allows a program to respond to expected failures instead of simply crashing.

However:

> Exception handling does not automatically make a program secure.

It is one tool that helps make programs more robust and predictable.

---

# 20. Debugging Exceptions

Exceptions tell us **that something went wrong**.

Debugging helps us determine **why**.

## `print()` Debugging

`print()` can be used to inspect what is happening inside a program.

Example:

```python
print(i)
```

This can help us see the values of variables while the program runs.

However, using large numbers of debugging `print()` statements can become difficult to manage.

---

## Breakpoints

IDEs and text editors can provide debugging tools.

A **breakpoint** pauses program execution at a specific line.

This allows us to inspect:

* Variable values
* Program state
* Which lines have executed
* What the program is about to do

Breakpoints are generally more useful than scattering many `print()` statements throughout a larger program.

---

# 21. Quick Debugging Guide

When Python gives an exception, use the exception name as a clue.

```text
SyntaxError
    ↓
Did I write valid Python syntax?

NameError
    ↓
Did I define this variable/name?

TypeError
    ↓
Am I using the wrong type?

ValueError
    ↓
Is the value invalid?

IndexError
    ↓
Does this list position exist?

KeyError
    ↓
Does this dictionary key exist?

AttributeError
    ↓
Does this object have this method/attribute?

ZeroDivisionError
    ↓
Did I divide by zero?

FileNotFoundError
    ↓
Does the file exist?

PermissionError
    ↓
Do I have permission?

ModuleNotFoundError
    ↓
Can Python find the module?

ImportError
    ↓
Did something go wrong during import?

RecursionError
    ↓
Did my recursion go too deep?
```

The exception is not merely an error message.

It is a **clue about what Python encountered**.

---

# 22. Exceptions to Learn Later

I do not need to spend time memorizing every Python exception.

These can be learned naturally as they become relevant:

* `FloatingPointError`
* `BufferError`
* `EOFError`
* `MemoryError`
* `BlockingIOError`
* `ChildProcessError`
* `BrokenPipeError`
* `ConnectionAbortedError`
* `ConnectionRefusedError`
* `ConnectionResetError`
* `InterruptedError`
* `IsADirectoryError`
* `NotADirectoryError`
* `ProcessLookupError`
* `TimeoutError`
* `StopAsyncIteration`
* `StopIteration`
* `SystemError`
* `UnicodeDecodeError`
* `UnicodeEncodeError`
* `UnicodeTranslateError`
* `ReferenceError`
* `GeneratorExit`
* `ExceptionGroup`

These become more relevant when studying areas such as:

* File handling
* APIs
* Networking
* OOP
* Iterators
* Generators
* Async programming
* Operating-system programming
* Concurrency

---

# 23. Useful Exception-Handling Patterns

## Catch a Specific Exception

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")
```

---

## Keep Asking Until Valid Input

```python
while True:
    try:
        number = int(input("Enter a number: "))
        break

    except ValueError:
        print("Invalid number.")
```

---

## Use `else` After Successful Conversion

```python
try:
    x = int(input("What's x? "))

except ValueError:
    print("x is not an integer")

else:
    print(f"x is {x}")
```

---

## Return Directly From `try`

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass
```

---

## Handle Multiple Exceptions Separately

```python
try:
    # code

except ValueError:
    # handle ValueError

except KeyError:
    # handle KeyError
```

---

## Handle Multiple Exceptions Together

```python
try:
    # code

except (ValueError, ZeroDivisionError):
    # handle either exception
    pass
```

---

## Raise Your Own Exception

```python
if value < 0:
    raise ValueError("Value cannot be negative.")
```

---

# 24. What I Know Now

I understand that:

* Exceptions are Python objects.
* Python can automatically raise exceptions when something goes wrong.
* `try` contains code that might fail.
* `except` handles matching exceptions.
* `else` runs when the `try` block succeeds.
* `finally` can run regardless of whether an exception occurs.
* Multiple `except` blocks can handle different exceptions.
* Multiple exceptions can be handled together using a tuple.
* `while True` and `break` can repeatedly request valid input.
* `pass` can intentionally do nothing when an exception is caught.
* Functions can encapsulate reusable exception-handling logic.
* `raise` allows me to deliberately raise an exception.
* Exceptions have a hierarchy based on inheritance.
* Specific exceptions are generally preferable to broad exception handlers.
* Debuggers and breakpoints can help locate problems.
* Exception handling can make programs more robust.
* Exception handling is part of defensive programming.
* Exception handling alone does not make a program secure.

---

# 25. Things I'm Still Learning

* [ ] Understand OOP and objects in Python
* [ ] Understand inheritance
* [ ] Understand the exception hierarchy in greater depth
* [ ] Learn the `assert` statement
* [ ] Understand `assert` versus `raise`
* [ ] Understand when to catch broad versus specific exceptions
* [ ] Learn more about `finally`
* [ ] Learn how exceptions interact with files and resource management
* [ ] Learn exception chaining
* [ ] Learn custom exception classes

---

# 26. The Big Picture

Exception handling fits into Python programming as a way of making programs capable of dealing with problems rather than assuming everything will always work.

The overall mental model is:

```text
WRITE PROGRAM
     ↓
PROGRAM PERFORMS AN OPERATION
     ↓
     ├── Operation succeeds
     │       ↓
     │    Continue normally
     │
     └── Operation fails
             ↓
        Exception raised
             ↓
        Python searches
        for a matching
        exception handler
             ↓
        ┌───────────────────┐
        │                   │
     Handler found      No handler
        │                   │
        ↓                   ↓
    Handle it            Program
        │                terminates
        ↓
    Continue
```

When writing robust programs, think:

```text
What could go wrong?
        ↓
What exception would Python raise?
        ↓
Should I handle that exception?
        ↓
What should my program do if it happens?
```

The goal is not to memorize every exception.

The goal is to recognize the **pattern behind the exception**.

```text
TYPE
    ↓
Wrong kind of object?
    → TypeError

VALUE
    ↓
Right kind of object, invalid value?
    → ValueError

INDEX
    ↓
Position doesn't exist?
    → IndexError

KEY
    ↓
Dictionary key doesn't exist?
    → KeyError

NAME
    ↓
Variable/name doesn't exist?
    → NameError

ATTRIBUTE
    ↓
Object doesn't have it?
    → AttributeError

SYNTAX
    ↓
Python code is written incorrectly?
    → SyntaxError
```

Once these patterns become familiar, Python error messages stop looking like random failures and start becoming useful clues about what the program is doing wrong.

---

# My Own Examples

Add examples here as I encounter useful exception-handling patterns.

```python
```
