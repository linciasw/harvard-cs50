# Functions

## What is it?

A function is a reusable block of code that performs a specific task.

## Syntax

```python
def function_name(parameters):
    # code
    return value
```

## Key things to remember

* `def` creates a function
* Parameters are the inputs
* `return` sends a value back
* A function doesn't have to return anything
* Functions help break large programs into smaller pieces

## Example

```python
def calculate_total(price, tax):
    return price + tax

total = calculate_total(100, 15)
```

## Things I learned

* `return` is different from `print()`
* Parameters are variables inside the function
* Arguments are the actual values passed to the function

## Things I'm still unsure about

* When should I use multiple parameters?
* When should I create a separate function?

## Practice

* [ ] Create a temperature converter
* [ ] Create a loan payment calculator
* [ ] Refactor an old project using functions

---

# Useful Patterns

## Function with no parameters

```python
def greet():
    print("Hello!")
```

## Function with parameters

```python
def greet(name):
    print(f"Hello, {name}!")
```

## Function that returns a value

```python
def add(a, b):
    return a + b

result = add(5, 10)
```

## Function with a default parameter

```python
def greet(name="User"):
    print(f"Hello, {name}!")
```

## Check a condition and return a result

```python
def is_adult(age):
    if age >= 18:
        return True
    return False
```

## Find the largest value

```python
largest = 0

for number in numbers:
    if number > largest:
        largest = number
```

## Count occurrences

```python
count = 0

for item in items:
    if item == target:
        count += 1
```

## Loop through a dictionary

```python
for key, value in data.items():
    print(key, value)
```

## Find the item with the highest value

```python
highest = max(data, key=data.get)
```

## Build a function around a repeated task

Instead of:

```python
print(price * 1.15)
print(price * 1.15)
print(price * 1.15)
```

Create a function:

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

---

# My Own Examples

Add examples here as I encounter patterns in projects.

```python
```
