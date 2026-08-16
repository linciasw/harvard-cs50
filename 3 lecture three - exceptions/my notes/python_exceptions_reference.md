# Python Exceptions — Reference

A reference for Python's built-in exception hierarchy and the exceptions
that are most important to learn first.


  - [Exception Hierarchy](#1-exception-hierarchy)
  - [Important Exception Relationships](#2-important-exception-relationships)
    - [Arithmetic Errors](#arithmetic-errors)
    - [Import Errors](#import-errors)
    - [Lookup Errors](#lookup-errors)
    - [Name Errors](#name-errors)
    - [Operating System Errors](#operating-system-errors)
    - [Syntax Errors](#syntax-errors)
    - [Unicode Errors](#unicode-errors)
  - [Top Exceptions to Learn First](#3-top-exceptions-to-learn-first)
  - [The Five Most Important Mental Models](#4-the-five-most-important-mental-models)
  - [Quick Debugging Guide](#5-quick-debugging-guide)
  - [Exceptions You Can Learn Later](#6-exceptions-you-can-learn-later)
  - [The Most Important Thing to Remember](#7-the-most-important-thing-to-remember)





---

# 1. Exception Hierarchy

The exception hierarchy shows how Python's exceptions are related.

A subclass is a more specific type of exception.

For example:

```python
try:
    number = int("hello")
except Exception:
    print("Something went wrong.")
```

Because `ValueError` is a subclass of `Exception`, the general `Exception`
handler can catch it. However, it is usually better to catch the specific
exception you expect.

## Complete Hierarchy

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

---

# 2. Important Exception Relationships

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

Example:

```python
numbers = [10, 20, 30]

try:
    print(numbers[10])
except IndexError:
    print("That index does not exist.")
```

Example:

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

Produces:

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
│
├── FileExistsError
├── FileNotFoundError
├── InterruptedError
├── IsADirectoryError
├── NotADirectoryError
├── PermissionError
├── ProcessLookupError
└── TimeoutError
```

These are mostly encountered when working with:

- Files
- Directories
- Processes
- Networking
- Operating-system resources

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

Produces:

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

# 3. Top Exceptions to Learn First

You do NOT need to memorize every Python exception.

These are the important ones to recognize as a beginner/intermediate Python programmer.

---

## 1. SyntaxError

### Meaning

Your Python code does not follow Python's syntax rules.

### Example

```python
if age >= 18
    print("Adult")
```

### Think:

> "I wrote invalid Python."

---

## 2. IndentationError

### Meaning

Your indentation is incorrect.

### Example

```python
if age >= 18:
print("Adult")
```

### Think:

> "My indentation is wrong."

---

## 3. NameError

### Meaning

Python does not know the variable or name you're trying to use.

### Example

```python
print(username)
```

If `username` was never defined:

```text
NameError
```

### Think:

> "Does this variable/name exist?"

---

## 4. TypeError

### Meaning

You are using the wrong type for an operation.

### Example

```python
age = 35

print("Age: " + age)
```

You cannot concatenate a string and an integer like this.

### Think:

> "Am I using the wrong TYPE?"

---

## 5. ValueError

### Meaning

The type is appropriate, but the value is invalid.

### Example

```python
number = int("hello")
```

`"hello"` is a string, but it isn't a valid representation of an integer.

### Think:

> "Is this the right TYPE but the wrong VALUE?"

---

## 6. IndexError

### Meaning

You tried to access a list/sequence index that doesn't exist.

### Example

```python
numbers = [10, 20, 30]

print(numbers[5])
```

Valid indexes are:

```text
0
1
2
```

### Think:

> "Does that position exist?"

---

## 7. KeyError

### Meaning

You tried to access a dictionary key that doesn't exist.

### Example

```python
person = {
    "name": "Lincia",
    "age": 35
}

print(person["salary"])
```

### Think:

> "Does that dictionary key exist?"

---

## 8. AttributeError

### Meaning

An object doesn't have the attribute or method you're trying to use.

### Example

```python
name = "Lincia"

name.append("!")
```

Strings don't have an `append()` method.

### Think:

> "Does this object have that method/attribute?"

---

## 9. ZeroDivisionError

### Meaning

You tried to divide by zero.

### Example

```python
result = 10 / 0
```

### Think:

> "Did I divide by zero?"

---

## 10. FileNotFoundError

### Meaning

Python tried to access a file or directory that doesn't exist.

### Example

```python
with open("missing.txt") as file:
    data = file.read()
```

### Think:

> "Does this file actually exist?"

---

## 11. PermissionError

### Meaning

Python doesn't have permission to perform the requested operation.

### Example

```python
with open("protected.txt", "w") as file:
    file.write("Hello")
```

### Think:

> "Do I have permission to do this?"

---

## 12. ModuleNotFoundError

### Meaning

Python cannot find the module you're trying to import.

### Example

```python
import pandas
```

If Pandas isn't installed:

```text
ModuleNotFoundError
```

### Think:

> "Can Python find this module?"

---

## 13. ImportError

### Meaning

Something went wrong while importing something.

### Example

```python
from math import something_that_doesnt_exist
```

### Think:

> "Something went wrong with my import."

---

## 14. RecursionError

### Meaning

Your program has exceeded Python's recursion limit.

### Example

```python
def count():
    count()

count()
```

The function keeps calling itself.

### Think:

> "My recursion went too deep."

---

# 4. The Five Most Important Mental Models

These five are especially useful when debugging.

---

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

# 5. Quick Debugging Guide

When you see an exception, ask:

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

---

# 6. Exceptions You Can Learn Later

Don't spend time memorizing these yet:

- `FloatingPointError`
- `BufferError`
- `EOFError`
- `MemoryError`
- `BlockingIOError`
- `ChildProcessError`
- `BrokenPipeError`
- `ConnectionAbortedError`
- `ConnectionRefusedError`
- `ConnectionResetError`
- `InterruptedError`
- `IsADirectoryError`
- `NotADirectoryError`
- `ProcessLookupError`
- `TimeoutError`
- `StopAsyncIteration`
- `StopIteration`
- `SystemError`
- `UnicodeDecodeError`
- `UnicodeEncodeError`
- `UnicodeTranslateError`
- `ReferenceError`
- `GeneratorExit`
- `ExceptionGroup`

You'll naturally encounter some of these later when you study:

- File handling
- APIs
- Networking
- OOP
- Iterators
- Generators
- Async programming
- Operating-system programming
- Concurrency

---

# 7. The Most Important Thing to Remember

Don't try to memorize every exception.

Learn to recognize the pattern:

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

Once these become familiar, Python error messages stop looking like random failures and start becoming clues about what your program is doing wrong.
