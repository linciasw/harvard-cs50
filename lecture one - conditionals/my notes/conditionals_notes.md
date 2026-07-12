# Python Conditionals

> **Goal:** Learn how Python makes decisions using conditional tests and `if` statements.

Conditionals allow your program to execute different blocks of code depending on whether a condition is **True** or **False**.

---

# What is a Conditional Test?

At the heart of every `if` statement is a **conditional test**.

A conditional test is an expression that evaluates to either:

- `True`
- `False`

If the test evaluates to `True`, Python executes the code inside the `if` block.

If the test evaluates to `False`, Python skips that block.

Example:

```python
age = 18

if age >= 18:
    print("You can vote.")
```

Python evaluates:

```python
age >= 18
```

Since the expression is `True`, the message is printed.

---

# Boolean Values

Conditional tests always return one of two Boolean values:

```python
True
False
```

Examples:

```python
5 > 3      # True
5 < 3      # False
10 == 10   # True
10 != 10   # False
```

---

# Assignment (`=`) vs Equality (`==`)

One of the most common beginner mistakes.

## Assignment Operator (`=`)

The assignment operator stores a value in a variable.

```python
car = "Audi"
```

Read as:

> Set the variable `car` equal to `"Audi"`.

It **does not** compare values.

---

## Equality Operator (`==`)

The equality operator compares two values.

```python
car == "Audi"
```

Read as:

> Is the value of `car` equal to `"Audi"`?

The result is either:

```python
True
```

or

```python
False
```

Example:

```python
car = "Audi"

print(car == "Audi")
```

Output:

```python
True
```

---

# Types of Conditional Tests

Python provides several ways to compare values.

## Equality

Checks if two values are the same.

```python
car == "Audi"
```

Returns:

```python
True
```

---

## Inequality (`!=`)

Checks if two values are different.

```python
car != "BMW"
```

Returns:

```python
True
```

if the values are different.

---

## Numerical Comparisons

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```python
age = 20

age >= 18
```

Returns:

```python
True
```

---

# Combining Conditions

Sometimes one comparison isn't enough.

Python provides two logical operators.

## `and`

Both conditions must be `True`.

```python
age >= 18 and has_id
```

Examples:

```python
18 >= 18 and True
```

Returns:

```python
True
```

---

## `or`

Only one condition must be `True`.

```python
is_student or is_teacher
```

Example:

```python
False or True
```

Returns:

```python
True
```

---

# Case-Sensitive Comparisons

String comparisons are case-sensitive.

```python
car = "Audi"

car == "audi"
```

Returns:

```python
False
```

because `"Audi"` and `"audi"` are different strings.

---

# Ignoring Letter Case

If capitalization shouldn't matter, convert the string before comparing.

```python
car = "Audi"

car.lower() == "audi"
```

Returns:

```python
True
```

### Important

```python
car.lower()
```

returns a **new string**.

It does **not** modify the original variable.

```python
car = "Audi"

print(car.lower())
```

Output:

```
audi
```

But:

```python
print(car)
```

Output:

```
Audi
```

This happens because strings are immutable.

---

# The `if` Statement

The simplest conditional statement.

```python
temperature = 32

if temperature > 30:
    print("It's hot today.")
```

Python executes the indented block only if the condition is `True`.

---

# The `if...else` Statement

Use `if...else` when there are **two possible outcomes**.

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Only one block will execute.

---

# The `if...elif...else` Statement

Use this when there are **more than two possible outcomes**.

```python
score = 87

if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")

else:
    print("Needs Improvement")
```

Python checks conditions from top to bottom.

As soon as one condition is `True`, the remaining conditions are skipped.

---

# Multiple `elif` Statements

You can have as many `elif` blocks as needed.

```python
if temperature > 35:
    print("Very Hot")

elif temperature > 25:
    print("Warm")

elif temperature > 15:
    print("Cool")

else:
    print("Cold")
```

---

# Omitting the `else` Block

An `else` block is optional.

```python
score = 95

if score >= 90:
    print("Excellent!")
```

If the condition is `False`, Python simply continues with the rest of the program.

### Why omit `else`?

The `else` block is a **catch-all**.

It executes whenever none of the previous conditions match.

Sometimes this includes:

- Invalid input
- Unexpected values
- Malicious data

If you don't need a default action, it's perfectly acceptable to leave the `else` block out.

---

# Testing Multiple Conditions

Sometimes several conditions can all be `True`.

In these cases, use **multiple `if` statements** instead of `if...elif...else`.

Example:

```python
toppings = ["pepperoni", "mushrooms", "olives"]

if "pepperoni" in toppings:
    print("Adding pepperoni")

if "mushrooms" in toppings:
    print("Adding mushrooms")

if "olives" in toppings:
    print("Adding olives")
```

Output:

```
Adding pepperoni
Adding mushrooms
Adding olives
```

Each condition is checked independently.

---

# Why Not Use `elif`?

An `if...elif...else` chain stops after the first `True` condition.

```python
if "pepperoni" in toppings:
    print("Adding pepperoni")

elif "mushrooms" in toppings:
    print("Adding mushrooms")
```

Only pepperoni would be added.

This is why multiple `if` statements are used when **more than one action** should happen.

---

# Choosing the Right Conditional

| Statement | Best Used When |
|-----------|----------------|
| `if` | Only one condition needs checking |
| `if...else` | Exactly two possible outcomes |
| `if...elif...else` | Several mutually exclusive outcomes |
| Multiple `elif` | Many exclusive choices |
| Multiple `if` statements | More than one condition may be true at the same time |

---

# Common Beginner Mistakes

### Using `=` instead of `==`

❌ Incorrect

```python
if age = 18:
```

✅ Correct

```python
if age == 18:
```

---

### Forgetting comparisons are case-sensitive

```python
"Audi" == "audi"
```

Returns:

```python
False
```

Use:

```python
car.lower() == "audi"
```

---

### Using `elif` when every condition should be checked

If multiple actions need to happen, use multiple `if` statements instead.

---

# Key Takeaways

- Conditionals allow your program to make decisions.
- Every conditional test evaluates to either `True` or `False`.
- `=` assigns values; `==` compares values.
- Use `!=` to check for inequality.
- Use comparison operators like `>`, `<`, `>=`, and `<=` for numeric comparisons.
- Combine conditions with `and` and `or`.
- String comparisons are case-sensitive.
- Use `.lower()` or `.upper()` when capitalization shouldn't matter.
- Use `if` for a single condition.
- Use `if...else` for two possible outcomes.
- Use `if...elif...else` when only one of many outcomes should occur.
- Use multiple `if` statements when several conditions can all be true.
- The `else` block is optional and should only be used when a default action is appropriate.

---

# Mini Practice

Try these without looking at your notes:

1. Ask the user for their age and print whether they are an adult.
2. Compare two numbers and print which is larger.
3. Check whether a username matches `"admin"` regardless of capitalization.
4. Write an `if...elif...else` statement to print a letter grade.
5. Create a pizza topping list and use multiple `if` statements to print each topping that should be added.

> **Remember:** Writing conditionals is about expressing logic clearly. Focus on understanding *why* a condition is `True` or `False`, not just memorizing the syntax.