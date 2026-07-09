# Python Conditionals Module Notes

## 1. What are Conditionals?

Conditionals are used when your program needs to **make decisions**.

Think of them as forks in the road:

> If this condition is true, do this. Otherwise, do something else.

``` python
if temperature > 30:
    print("It's hot")
else:
    print("It's cool")
```

The program evaluates the condition: - True → execute the `if` block -
False → execute the `else` block (if present)

------------------------------------------------------------------------

## 2. Boolean Expressions

A boolean expression evaluates to either:

``` python
True
False
```

Example:

``` python
x = 5
print(x > 3)
```

------------------------------------------------------------------------

## 3. Comparison Operators

  Operator   Meaning
  ---------- --------------------------
  `>`        Greater than
  `>=`       Greater than or equal to
  `<`        Less than
  `<=`       Less than or equal to
  `==`       Equal to
  `!=`       Not equal to

Remember: - `=` assigns a value. - `==` compares values.

------------------------------------------------------------------------

## 4. if, elif, else

``` python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

-   `if` starts a decision.
-   `elif` checks another condition only if previous ones failed.
-   `else` catches everything remaining.

Python stops checking an `if/elif/else` chain after the first true
condition.

------------------------------------------------------------------------

## 5. Indentation

Python uses indentation to define code blocks.

``` python
if x > y:
    print("Correct")
```

Without proper indentation, Python raises an error.

------------------------------------------------------------------------

## 6. Multiple if vs elif

Separate `if` statements are all checked.

``` python
if x < y:
    ...

if x > y:
    ...

if x == y:
    ...
```

Using `elif` is more efficient because Python stops after the first
match.

------------------------------------------------------------------------

## 7. Logical Operators

### and

Both conditions must be true.

``` python
if score >= 80 and score < 90:
```

### or

Only one condition must be true.

``` python
if answer == "42" or answer == "forty-two":
```

### not

Reverses a boolean.

``` python
if not logged_in:
```

------------------------------------------------------------------------

## 8. Simplifying Conditions

Instead of:

``` python
if score >= 90 and score <= 100:
```

Write:

``` python
if score >= 90:
```

Because earlier conditions already ruled out higher grades.

Always ask: - Can this be simpler? - Am I asking unnecessary questions?

------------------------------------------------------------------------

## 9. Nested Conditionals

``` python
if difficulty == "Difficult":
    if players == "Multiplayer":
        recommend("Poker")
```

This works, but flattening conditions often improves readability:

``` python
if difficulty == "Difficult" and players == "Multiplayer":
```

------------------------------------------------------------------------

## 10. Modulo (%)

Modulo returns the remainder after division.

Examples:

``` python
4 % 2   # 0
5 % 2   # 1
```

Even numbers:

``` python
if number % 2 == 0:
```

------------------------------------------------------------------------

## 11. Returning Booleans

Instead of:

``` python
if condition:
    return True
else:
    return False
```

Use:

``` python
return condition
```

Your `is_even()` function is a perfect example.

------------------------------------------------------------------------

## 12. String Methods

Useful methods:

-   `.startswith()`
-   `.endswith()`
-   `.lower()`
-   `.upper()`
-   `.strip()`
-   `.replace()`
-   `.split()`
-   `.join()`
-   `.find()`

Examples:

``` python
greeting.startswith("hello")
filename.endswith(".pdf")
filename = filename.lower()
```

------------------------------------------------------------------------

## 13. match / case

Instead of many `elif` statements:

``` python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

`case _` works like `else`.

------------------------------------------------------------------------

## 14. Input Validation

Never assume the user enters valid data.

``` python
if not (difficulty == "Difficult" or difficulty == "Casual"):
    print("Enter a valid difficulty")
    return
```

Validate before continuing.

------------------------------------------------------------------------

## 15. Parsing Input

``` python
expression = input("Expression: ")
x, operator, z = expression.split(" ")
```

Input:

    5 + 3

Becomes:

    x = "5"
    operator = "+"
    z = "3"

------------------------------------------------------------------------

## 16. **name** == "**main**"

``` python
if __name__ == "__main__":
    main()
```

Meaning:

Run `main()` only if this file was started directly.

If another Python file imports it, `main()` will not automatically run.

------------------------------------------------------------------------

# Cheat Sheet

## Comparison

``` python
==
!=
>
<
>=
<=
```

## Boolean Operators

``` python
and
or
not
```

## Common Patterns

``` python
if x == "A":
    ...
elif x == "B":
    ...
else:
    ...
```

``` python
if filename.endswith(".pdf"):
```

``` python
if number % 2 == 0:
```

``` python
return condition
```

------------------------------------------------------------------------

# Key Takeaways

1.  Conditionals allow programs to make decisions.
2.  Boolean expressions evaluate to `True` or `False`.
3.  `elif` avoids unnecessary checks.
4.  Simpler code is usually better code.
5.  `and`, `or`, and `not` combine conditions.
6.  `%` is commonly used to detect even and odd numbers.
7.  String methods are frequently used in conditionals.
8.  Validate user input before processing it.
9.  `match` can replace long `if/elif` chains.
10. `if __name__ == "__main__":` prevents imported files from executing
    automatically.
