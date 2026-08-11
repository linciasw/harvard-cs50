# Python Primitive Data Types Cheat Sheet

Python has several built-in data types. The four most common primitive data types are:

- `int` – Whole numbers
- `float` – Decimal numbers
- `complex` – Real & imaginary numbers
- `str` – Text (strings)


Complex numbers are commonly used in:
- Electrical engineering (AC circuit analysis)
- Signal processing
- Physics
- Mathematics
- Fourier transforms


---

# Integers (`int`)

Integers represent whole numbers.

```python
x = 10
```

## Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `x + 5` |
| `-` | Subtraction | `x - 5` |
| `*` | Multiplication | `x * 5` |
| `/` | Division (returns a float) | `x / 5` |
| `//` | Floor Division | `x // 5` |
| `%` | Modulus (remainder) | `x % 5` |
| `**` | Exponentiation | `x ** 2` |

Example:

```python
print(x + 5)
print(x - 5)
print(x * 5)
print(x / 5)
print(x // 5)
print(x % 5)
print(x ** 2)
```

## Useful Built-in Functions

```python
abs(-10)        # 10
pow(2, 3)       # 8
min(1, 2, 3)    # 1
max(1, 2, 3)    # 3
```

## Type Conversion

Convert other data types into integers.

```python
int("10")   # 10
int(3.7)    # 3 (decimal is truncated)
```

---

# Floating-Point Numbers (`float`)

Floats represent decimal numbers.

```python
y = 3.14
```

## Arithmetic

Floats use the same arithmetic operators as integers.

```python
print(y + 2)
print(y - 1)
print(y * 3)
print(y / 2)
```

## Rounding

```python
round(3.14159, 2)
# Output: 3.14
```

## Type Conversion

```python
float("3.14")
float(10)
```

## Floating-Point Precision

Due to the way computers store decimal numbers, floating-point calculations are sometimes not exact.

```python
print(0.1 + 0.2)
```

Output:

```python
0.30000000000000004
```

This is normal behavior in Python (and most programming languages).

---

# Strings (`str`)

Strings represent text.

```python
text = "hello world"
```

---

## Changing Letter Case

```python
text.lower()     # hello world
text.upper()     # HELLO WORLD
text.title()     # Hello World
```

---

## Cleaning and Replacing Text

### Remove whitespace

```python
text.strip()
```

### Replace text

```python
text.replace("hello", "hi")
```

Output:

```
hi world
```

---

## Splitting and Joining

### Split a string into a list

```python
words = text.split()
```

Output:

```python
['hello', 'world']
```

### Join a list into a string

```python
" ".join(["hi", "there"])
```

Output:

```
hi there
```

---

## Searching Strings

### Find text

```python
text.find("world")
```

Returns the index where `"world"` begins.

### Check how a string starts

```python
text.startswith("he")
```

Returns `True` or `False`.

### Check how a string ends

```python
text.endswith("ld")
```

Returns `True` or `False`.

---

## Checking String Contents

### Digits only

```python
"123".isdigit()
```

### Letters only

```python
"abc".isalpha()
```

### Letters and numbers

```python
"abc123".isalnum()
```

These methods return either `True` or `False`.

---

## Length of a String

```python
len(text)
```

Output:

```python
11
```

---

# Checking Data Types

Use the `type()` function to see what type of data a variable contains.

```python
type(10)      # int
type(10.0)    # float
type("10")    # str
```

---

# Strings vs Numbers

Python treats strings and numbers differently.

## String Concatenation

```python
"10" + "5"
```

Output:

```
105
```

The strings are joined together.

## Numeric Addition

```python
10 + 5
```

Output:

```
15
```

Numbers are added mathematically.

---

# Summary

| Data Type | Purpose | Example |
|-----------|---------|---------|
| `int` | Whole numbers | `10` |
| `float` | Decimal numbers | `3.14` |
| `complex` | Real & Imaginary | `3 + 4j` |
| `str` | Text | `"hello"` |

### Common Integer Operations

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `//` Floor Division
- `%` Modulus
- `**` Exponentiation

### Common String Methods

- `.lower()`
- `.upper()`
- `.title()`
- `.strip()`
- `.replace()`
- `.split()`
- `.join()`
- `.find()`
- `.startswith()`
- `.endswith()`
- `.isdigit()`
- `.isalpha()`
- `.isalnum()`

### Useful Functions

- `abs()`
- `pow()`
- `min()`
- `max()`
- `round()`
- `len()`
- `type()`
- `int()`
- `float()`