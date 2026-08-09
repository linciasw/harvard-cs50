# Exceptions

## What are they?

Exceptions are events that occur during the execution of a program when something unexpected or invalid happens.

Examples:

* Converting invalid input with `int()` → `ValueError`
* Looking for a dictionary key that doesn't exist → `KeyError`
* Dividing by zero → `ZeroDivisionError`
* Using a variable that doesn't exist → `NameError`

Exceptions are Python objects that represent these errors.

---

## Why do exceptions matter?

Programs should be written with error handling in mind.

This is sometimes called **defensive programming** — anticipating problems and deciding how the program should respond when they happen.

Exceptions allow us to separate:

* The code that performs the actual task
* The code that decides what to do when something goes wrong

Instead of putting error-handling logic throughout our program, Python allows an exception to be raised and handled higher up in the program.

---

## Basic syntax

```python
try:
    # code that might cause an exception
except ValueError:
    # what to do if a ValueError occurs
```

The `try` block contains code that might fail.

If an exception occurs, Python stops executing the `try` block and looks for an appropriate `except` block.

---

## Example

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

### Important

If `int()` receives something like `"cat"`, it raises a `ValueError`.

Because the assignment to `x` never finishes, `x` does not exist.

That's why this would cause a `NameError`:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(x)
```

Using `else` allows us to run code involving `x` only when the `try` block succeeds.

---

# Common Exceptions

## ValueError

The value has the correct general type but is not an appropriate value for the operation.

```python
x = int("cat")
```

Produces:

```text
ValueError
```

---

## KeyError

A dictionary key doesn't exist.

```python
distances = {
    "Voyager 1": "163"
}

print(distances["James Webb Space Telescope"])
```

Produces:

```text
KeyError
```

---

## ZeroDivisionError

Trying to divide by zero.

```python
result = 10 / 0
```

Produces:

```text
ZeroDivisionError
```

---

## NameError

Trying to use a variable that doesn't exist.

```python
print(x)
```

Produces:

```text
NameError
```

---

# Handling Multiple Exceptions

We can have multiple `except` blocks.
```python
try:
    body
except exception_type1 as var1:
    exception_code1
except exception_type2 as var2:
    exception_code2
    .
    .
    .
except:
    default_exception_code
else:
    else_body
finally:
    finally_body
```


```python
try:
    au = float(distances[spacecraft])
except KeyError:
    print(f"'{spacecraft}' is not in dictionary")
except ValueError:
    print(f"Can't convert '{distances[spacecraft]}' to a float")
```

Be as specific as possible when handling exceptions.

Avoid catching every possible exception unless you have a good reason.

---

# While Loops + Exceptions

Exceptions can be used with loops to repeatedly ask for valid input.

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

`while True` creates an infinite loop.

`break` exits the loop once valid input has been received.

---

# Creating Reusable Exception Handling

Instead of repeating the same input-validation code, we can create a function.

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

The caller can decide what variable to use while `get_int()` handles the input validation.

---

# `pass`

`pass` allows us to catch an exception without doing anything when it occurs.

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
```

This keeps asking for input until a valid integer is entered.

---

# Raising Exceptions

Python allows us to deliberately raise an exception using `raise`.

```python
def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Minutes must be greater than 0.")

    return minutes / miles
```

We can raise an exception when a condition makes continuing the program invalid.

---

# Debugging

Exceptions tell us that something went wrong, but debugging helps us figure out **why**.

## `print()` debugging

`print()` can be used to inspect what is happening inside a program.

```python
print(i)
```

This can help us understand the values of variables while the program runs.

However, large numbers of debugging `print()` statements can become difficult to manage.

## Breakpoints

IDEs and text editors can provide built-in debugging tools.

A **breakpoint** pauses program execution at a specific line so we can inspect what is happening.

---

# Exception Hierarchy

Python organizes exceptions into a hierarchy.

At the top is:

```text
BaseException
    └── Exception
```

Many of the exceptions we commonly use are subclasses of `Exception`.

For example:

```text
Exception
├── ArithmeticError
│   └── ZeroDivisionError
├── LookupError
│   ├── IndexError
│   └── KeyError
├── NameError
├── TypeError
└── ValueError
```

The hierarchy is based on **inheritance**.

I don't need to memorize the entire hierarchy.

What I need to understand first:

* Exceptions are objects
* Exceptions can inherit from other exceptions
* More specific exceptions can be caught individually
* A broader exception can catch multiple related exceptions
* The hierarchy becomes more useful once I understand inheritance and OOP

## Exceptions I currently know

* `ValueError`
* `KeyError`
* `ZeroDivisionError`
* `NameError`
* `TypeError`

---

# Security & Defensive Programming

Exceptions can contribute to program security because programs cannot always assume that input or actions will behave as expected.

For example:

* Users can enter unexpected input
* Files might not exist
* Data might be malformed
* External systems might fail
* Someone could intentionally provide unexpected input to make a program fail

Exception handling allows the program to respond to expected failures instead of simply crashing.

**Important:** Exception handling does not automatically make a program secure. It is one tool that helps make programs more robust and predictable when something goes wrong.

---

# Things I Learned

* Exceptions are Python objects
* Python can raise exceptions automatically when something goes wrong
* We can handle exceptions using `try` and `except`
* `else` runs when the `try` block succeeds
* `while True` and `break` can be used to repeatedly request valid input
* `pass` can be used when we intentionally don't want to do anything after catching an exception
* We can raise our own exceptions with `raise`
* Exceptions have a hierarchy based on inheritance
* Debuggers and breakpoints can help find problems in code
* Exception handling can help make programs more robust against unexpected input

---

# Things I'm Still Learning

* [ ] Understand OOP and objects in Python
* [ ] Understand inheritance
* [ ] Understand the exception hierarchy in more depth
* [ ] Learn the `assert` statement
* [ ] Learn when to use `assert` versus `raise`
* [ ] Understand when to catch broad versus specific exceptions

---

# Useful Patterns

## Catch a specific exception

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
```

## Keep asking until valid input

```python
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid number.")
```

## Return directly from `try`

```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
```

## Raise your own exception

```python
if value < 0:
    raise ValueError("Value cannot be negative.")
```

## Handle multiple exceptions

```python
try:
    # code
except ValueError:
    # handle ValueError
except KeyError:
    # handle KeyError
```

---

# My Own Examples

Add examples here as I encounter useful exception-handling patterns.

```python
```
