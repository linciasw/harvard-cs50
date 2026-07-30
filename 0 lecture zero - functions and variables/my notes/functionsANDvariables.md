# Lecture 0: Functions & Variables — Code Walkthrough

> Companion to `lectureZeroNotes.md` and `dataTypesMethods.md`. This file walks through every code file in the **lecture**, **shorts**, and **problem sets** folders, organized by topic, with example output added for every script that didn't already show one.

---

## 1. Variables, Input, and String Methods — `lecture/hello.py`

Demonstrates `input()`, `.strip()`, `.title()`, `.split()`, and f-strings.

```python
name = input("What's your name?").strip().title()

first, last = name.split(" ")

print(f"hello, {name}")
```

**Example Output**

```
What's your name? john smith
hello, John Smith
```

- `.strip()` removes accidental leading/trailing spaces from the input.
- `.title()` capitalizes each word.
- `.split(" ")` breaks `"John Smith"` into `first = "John"` and `last = "Smith"`.

---

## 2. Functions & Scope — `lecture/hello_functions.py`

Shows why a helper function needs a value *passed* to it (scope), and how a parameter can have a default value.

```python
def main():
    name = input("What's your name?")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()
```

**Example Output**

```
What's your name? Lincia
hello, Lincia
```

**Example Output (no input given / just pressing Enter)**

```
What's your name? 
hello, 
```

- If `to` were never passed in, `hello()` would fall back to its default: `hello, world`.
- `name` only exists inside `main()` — trying to `print(name)` outside of `main()` would raise a `NameError`. This is **scope**.

---

## 3. Return Values & Type Conversion — `lecture/calculator.py`

Shows a function that **returns** a value instead of just printing one.

```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
```

**Example Output**

```
What's x? 4
x squared is 16
```

- `input()` always returns a `str`, so `int(...)` converts it to a number before it can be squared.
- `square(n)` uses `return`, so the result can be stored, printed, or reused — unlike a function that only calls `print()` internally.

---

## 4. Return Values (Multiple Calls) — `shorts/return.py`

Reinforces `return` by combining the results of two function calls.

```python
def area(length, width):
    return length * width  # return ends the function


def main():
    house = area(50, 20)
    yard = area(50, 50)
    total = house + yard
    print(str(total) + " square feet")


main()
```

**Example Output**

```
3500 square feet
```

- `house = 50 * 20 = 1000`, `yard = 50 * 50 = 2500`, `total = 3500`.
- Because `area()` *returns* instead of *prints*, both results can be added together before anything is displayed — this is the key difference from a print-only function.

---

## 5. Side Effects & Global Variables — `shorts/machine.py`

Shows a global variable being changed by a function (a "side effect").

```python
emoticon = "v.v"  # global variable


def main():
    global emoticon  # need to say this to change global variable
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
```

**Example Output**

```
Is anyone there? v.v
Oh, hi! :D
```

- A **side effect** is anything a function does besides returning a value (printing, modifying a global variable, writing a file, etc.).
- `global emoticon` is required inside `main()` because, without it, `emoticon = ":D"` would just create a new *local* variable instead of changing the global one.
- A function that only computes and returns a value (no printing, no state changes) is called a **pure function**.

---

## 6. Problem Set: `.replace()` & Type Conversion — `problem sets/tip.py`

Parses currency-style strings (`"$20.00"`, `"15%"`) into usable floats.

```python
def main():
    dollars = dollars_to_float(input("How much was the meal? Enter format $00.00 "))
    percent = percent_to_float(input("What percentage would you like to tip? Enter format 00% "))
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

**Example Output**

```
How much was the meal? Enter format $00.00 $20.00
What percentage would you like to tip? Enter format 00% 15%
Leave $3.00
```

- `.replace("$", "")` strips the currency symbol so `float()` can parse it. Because **strings are immutable**, the result has to be reassigned (`d = d.replace(...)`), not just called on its own.
- `:.2f` in the f-string formats the tip to exactly 2 decimal places.

---

## 7. Problem Set: Formula with Large Numbers — `problem sets/einstein.py`

Applies Einstein's `E = mc²`.

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

**Example Output**

```
m: 5
e: 450000000000000000
```

- `**` is the exponentiation operator: `300000000 ** 2` = 90,000,000,000,000,000.
- Python `int` has no fixed size limit, so it can represent very large whole numbers exactly (unlike `float`, which loses precision at that scale).

---

## 8. Problem Set: Case Conversion — `problem sets/indoor.py`

The shortest possible example of chaining a string method directly onto `input()`.

```python
text = input("Enter text: ").lower()

print(text)
```

**Example Output**

```
Enter text: Hello World
hello world
```

---

## 9. Problem Set: `split()` + `join()` — `problem sets/playback.py`

Shows `split()` and `join()` used together to transform text.

```python
text = input("Enter text: ")

result = "...".join(text.split())

print(result)
```

**Example Output**

```
Enter text: This is CS50
This...is...CS50
```

- `text.split()` runs first (innermost parentheses), turning `"This is CS50"` into `["This", "is", "CS50"]`.
- `"...".join(...)` then combines that list back into one string, placing `"..."` between each item.

---

## Quick Reference — Files in This Section

| File | Folder | Core Concept |
|------|--------|---------------|
| `hello.py` | lecture | Input, `.strip()`, `.title()`, `.split()`, f-strings |
| `hello_functions.py` | lecture | Function scope, default parameter values |
| `calculator.py` | lecture | Return values, type conversion |
| `return.py` | shorts | Combining return values from multiple calls |
| `machine.py` | shorts | Side effects, global variables |
| `tip.py` | problem sets | `.replace()`, string immutability, formatted output |
| `einstein.py` | problem sets | Exponentiation, large integers |
| `indoor.py` | problem sets | Method chaining on `input()` |
| `playback.py` | problem sets | `split()` and `join()` together |