# CS50 Lecture 1 — Conditionals

## Table of Contents

- [CS50 Lecture 1 — Conditionals](#cs50-lecture-1--conditionals)
  - [Table of Contents](#table-of-contents)
- [1. What Are Conditionals?](#1-what-are-conditionals)
- [2. Boolean Values](#2-boolean-values)
- [3. Conditional Tests](#3-conditional-tests)
- [4. Comparison Operators](#4-comparison-operators)
  - [Assignment `=` vs Equality `==`](#assignment--vs-equality-)
    - [`=`](#)
    - [`==`](#-1)
    - [Remember](#remember)
  - [Inequality `!=`](#inequality-)
  - [Numerical Comparisons](#numerical-comparisons)
- [5. String Comparisons](#5-string-comparisons)
  - [Case Sensitivity](#case-sensitivity)
  - [Using `.lower()`](#using-lower)
  - [String Immutability](#string-immutability)
- [6. The `if` Statement](#6-the-if-statement)
- [7. The `if...else` Statement](#7-the-ifelse-statement)
- [8. The `if...elif...else` Statement](#8-the-ifelifelse-statement)
    - [Important rule](#important-rule)
  - [Multiple `elif` Statements](#multiple-elif-statements)
- [9. Multiple `if` Statements vs `elif`](#9-multiple-if-statements-vs-elif)
  - [Why Not Use `elif`?](#why-not-use-elif)
- [10. Omitting `else`](#10-omitting-else)
    - [Why can omitting `else` be useful?](#why-can-omitting-else-be-useful)
- [11. Simplifying Conditional Logic](#11-simplifying-conditional-logic)
    - [Habit to build](#habit-to-build)
- [12. Boolean Logic](#12-boolean-logic)
  - [`and`](#and)
  - [`or`](#or)
  - [`not`](#not)
- [13. Numeric Ranges and Chained Comparisons](#13-numeric-ranges-and-chained-comparisons)
  - [Grade Calculator](#grade-calculator)
- [14. The `match` Statement](#14-the-match-statement)
  - [Equivalent `if` Version](#equivalent-if-version)
- [15. The Modulo Operator `%`](#15-the-modulo-operator-)
  - [Checking for Even Numbers](#checking-for-even-numbers)
- [16. Returning Boolean Expressions](#16-returning-boolean-expressions)
  - [Complete Example](#complete-example)
- [17. String Methods Used with Conditionals](#17-string-methods-used-with-conditionals)
  - [`.startswith()`](#startswith)
  - [`.endswith()`](#endswith)
  - [`.lower()`](#lower)
  - [`.upper()`](#upper)
  - [`.strip()`](#strip)
  - [`.replace()`](#replace)
  - [`.split()`](#split)
  - [`.join()`](#join)
  - [`.find()`](#find)
- [18. Practical Example: Greeting Classifier](#18-practical-example-greeting-classifier)
- [19. Practical Example: File Extension / MIME Type](#19-practical-example-file-extension--mime-type)
- [20. Practical Example: Answer to Life, the Universe, and Everything](#20-practical-example-answer-to-life-the-universe-and-everything)
- [21. Practical Example: Simple Interpreter](#21-practical-example-simple-interpreter)
- [22. Practical Example: Meal Time Converter](#22-practical-example-meal-time-converter)
  - [How the Conversion Works](#how-the-conversion-works)
- [23. The `__name__ == "__main__"` Pattern](#23-the-__name__--__main__-pattern)
- [24. Nested Conditionals](#24-nested-conditionals)
- [25. Flattening Nested Conditionals with Boolean Logic](#25-flattening-nested-conditionals-with-boolean-logic)
  - [Why Validate First?](#why-validate-first)
- [26. Functions and Conditionals Working Together](#26-functions-and-conditionals-working-together)
- [27. Indentation and Conditional Blocks](#27-indentation-and-conditional-blocks)
- [28. Common Beginner Mistakes](#28-common-beginner-mistakes)
  - [Mistake 1: Using `=` instead of `==`](#mistake-1-using--instead-of-)
  - [Mistake 2: Forgetting Case Sensitivity](#mistake-2-forgetting-case-sensitivity)
  - [Mistake 3: Using `elif` When Every Condition Should Be Checked](#mistake-3-using-elif-when-every-condition-should-be-checked)
  - [Mistake 4: Automatically Adding `else`](#mistake-4-automatically-adding-else)
  - [Mistake 5: Writing More Conditions Than Necessary](#mistake-5-writing-more-conditions-than-necessary)
- [29. Choosing the Right Conditional](#29-choosing-the-right-conditional)
  - [Quick Decision Guide](#quick-decision-guide)
    - [One decision?](#one-decision)
    - [Two possible outcomes?](#two-possible-outcomes)
    - [Several mutually exclusive outcomes?](#several-mutually-exclusive-outcomes)
    - [Several conditions can independently be true?](#several-conditions-can-independently-be-true)
    - [Many values need to match specific cases?](#many-values-need-to-match-specific-cases)
- [30. Core Mental Model](#30-core-mental-model)
- [31. Key Takeaways](#31-key-takeaways)
- [32. Practice Questions](#32-practice-questions)
  - [Beginner](#beginner)
    - [1. Adult Checker](#1-adult-checker)
    - [2. Number Comparison](#2-number-comparison)
    - [3. Username](#3-username)
    - [4. Grade Calculator](#4-grade-calculator)
  - [Intermediate](#intermediate)
    - [5. Even or Odd](#5-even-or-odd)
    - [6. Pizza Toppings](#6-pizza-toppings)
    - [7. File Extension](#7-file-extension)
    - [8. Greeting Classifier](#8-greeting-classifier)
  - [More Challenging](#more-challenging)
    - [9. Simple Calculator](#9-simple-calculator)
    - [10. Meal Time](#10-meal-time)
    - [11. Game Recommender](#11-game-recommender)
  - [Final Challenge](#final-challenge)

---

# 1. What Are Conditionals?

Conditionals allow a program to **make decisions**.

Instead of always executing the same code, a program can ask a question and execute different code depending on the answer.

For example:

```python
age = 18

if age >= 18:
    print("You can vote.")
```

The program asks:

```python
age >= 18
```

If the answer is `True`, Python executes:

```python
print("You can vote.")
```

If the answer is `False`, Python skips that block.

This is the foundation of program logic.

A useful mental model is:

```text
INPUT
  ↓
CONDITION
  ↓
True or False?
  ↓
DECISION
  ↓
ACTION
```

Conditionals are essentially **forks in the road of a program**.

---

# 2. Boolean Values

Python has two Boolean values:

```python
True
False
```

Boolean values represent whether something is true or false.

Examples:

```python
5 > 3
```

Result:

```python
True
```

```python
5 < 3
```

Result:

```python
False
```

```python
10 == 10
```

Result:

```python
True
```

```python
10 != 10
```

Result:

```python
False
```

Boolean values are extremely important because conditional statements use them to decide what code should execute.

---

# 3. Conditional Tests

A **conditional test** is an expression that evaluates to either:

```python
True
```

or:

```python
False
```

For example:

```python
age = 18

age >= 18
```

The expression evaluates to:

```python
True
```

Therefore:

```python
if age >= 18:
    print("Adult")
```

executes the indented block.

The general structure is:

```python
if condition:
    # code to execute if condition is True
```

The condition is evaluated first.

Then Python decides whether to execute the indented block.

---

# 4. Comparison Operators

Python provides comparison operators for creating conditional tests.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

Examples:

```python
x = 10

x == 10
```

Result:

```python
True
```

```python
x != 10
```

Result:

```python
False
```

```python
x > 5
```

Result:

```python
True
```

```python
x < 5
```

Result:

```python
False
```

```python
x >= 10
```

Result:

```python
True
```

```python
x <= 10
```

Result:

```python
True
```

---

## Assignment `=` vs Equality `==`

This is one of the most important distinctions to understand.

### `=`

The assignment operator stores a value in a variable.

```python
car = "Audi"
```

Read this as:

> Set `car` equal to `"Audi"`.

It does **not** ask a question.

---

### `==`

The equality operator compares two values.

```python
car == "Audi"
```

Read this as:

> Is `car` equal to `"Audi"`?

The result is either:

```python
True
```

or:

```python
False
```

Example:

```python
car = "Audi"

print(car == "Audi")
```

Output:

```text
True
```

### Remember

```text
=   → assignment
==  → comparison
```

---

## Inequality `!=`

`!=` means **not equal to**.

```python
car = "Audi"

print(car != "BMW")
```

Output:

```text
True
```

because `"Audi"` and `"BMW"` are different.

---

## Numerical Comparisons

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Python evaluates:

```python
age >= 18
```

which becomes:

```python
True
```

and therefore executes the block.

---

# 5. String Comparisons

Strings can also be compared using conditional operators.

```python
car = "Audi"

print(car == "Audi")
```

Output:

```text
True
```

---

## Case Sensitivity

String comparisons are **case-sensitive**.

```python
car = "Audi"

print(car == "audi")
```

Output:

```text
False
```

Why?

Because:

```text
"Audi"
```

and:

```text
"audi"
```

are different strings.

Capital `A` and lowercase `a` are different characters.

---

## Using `.lower()`

If capitalization shouldn't matter, convert the string before comparing it.

```python
car = "Audi"

print(car.lower() == "audi")
```

Output:

```text
True
```

This is useful when processing user input.

For example:

```python
name = input("What's your name? ")

if name.lower() == "harry":
    print("Welcome, Harry!")
```

Now the user could enter:

```text
Harry
```

or:

```text
HARRY
```

or:

```text
harry
```

and the comparison would still work.

---

## String Immutability

An important detail:

```python
car.lower()
```

does **not** change `car`.

It returns a new string.

Example:

```python
car = "Audi"

print(car.lower())
print(car)
```

Output:

```text
audi
Audi
```

This happens because strings are **immutable**.

They cannot be modified in place.

---

# 6. The `if` Statement

`if` is the simplest conditional.

```python
temperature = 32

if temperature > 30:
    print("It's hot today.")
```

Python checks:

```python
temperature > 30
```

If `True`, the block executes.

If `False`, the block is skipped.

Another example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Only the code inside the indented block belongs to the `if`.

---

# 7. The `if...else` Statement

Use `if...else` when there are **two possible outcomes**.

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

There are two paths:

```text
age >= 18?
   ↓
YES → Adult
NO  → Minor
```

Exactly one branch executes.

---

# 8. The `if...elif...else` Statement

Use `if...elif...else` when there are multiple possible outcomes.

Example:

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

Python checks conditions **from top to bottom**.

For:

```python
score = 87
```

Python checks:

```python
score >= 90
```

False.

Then:

```python
score >= 80
```

True.

So Python prints:

```text
B
```

Then it stops checking the remaining conditions.

### Important rule

An `if/elif/else` chain stops at the **first true branch**.

---

## Multiple `elif` Statements

You can have as many `elif` statements as necessary.

```python
temperature = 20

if temperature > 35:
    print("Very Hot")
elif temperature > 25:
    print("Warm")
elif temperature > 15:
    print("Cool")
else:
    print("Cold")
```

The conditions are checked from top to bottom.

---

# 9. Multiple `if` Statements vs `elif`

This distinction is extremely important.

Use multiple separate `if` statements when **multiple conditions can be true at the same time**.

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

```text
Adding pepperoni
Adding mushrooms
Adding olives
```

Each `if` is checked independently.

---

## Why Not Use `elif`?

Consider:

```python
if "pepperoni" in toppings:
    print("Adding pepperoni")
elif "mushrooms" in toppings:
    print("Adding mushrooms")
elif "olives" in toppings:
    print("Adding olives")
```

Only the first true condition executes.

Once:

```python
"pepperoni" in toppings
```

is `True`, Python stops the chain.

Therefore, use:

```python
if
if
if
```

when several conditions may be true.

Use:

```python
if
elif
elif
```

when only one outcome should occur.

---

# 10. Omitting `else`

`else` is optional.

You can write:

```python
score = 95

if score >= 90:
    print("Excellent!")
```

If the condition is false, Python simply continues with the rest of the program.

You don't need an `else` if there is no meaningful default action.

### Why can omitting `else` be useful?

`else` is a **catch-all**.

It executes whenever none of the previous conditions matched.

Sometimes that can accidentally treat:

* Invalid input
* Unexpected values
* Malformed data
* Unexpected states

as though they were legitimate input.

So don't automatically add an `else`.

Ask:

> Do I actually need a default action?

---

# 11. Simplifying Conditional Logic

A major programming habit is learning to recognize unnecessary complexity.

For example:

```python
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```

The condition:

```python
x < y or x > y
```

is essentially asking:

> Is x anything other than y?

There is already an operator for this:

```python
!=
```

So this can become:

```python
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```

### Habit to build

Whenever you write conditional logic, ask:

> Could this code be simpler?

> Could I ask fewer questions?

> Is Python already providing an operator for this?

Simpler logic is usually easier to understand, maintain, and debug.

---

# 12. Boolean Logic

Python provides three Boolean operators:

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be true        |
| `or`     | At least one condition must be true |
| `not`    | Reverses the Boolean value          |

---

## `and`

Both sides must be `True`.

```python
age >= 18 and has_id
```

For the entire expression to be `True`:

```text
age >= 18 → True
has_id    → True
```

Example:

```python
18 >= 18 and True
```

Result:

```python
True
```

If either side is false, the whole `and` expression is false.

---

## `or`

At least one condition must be true.

```python
is_student or is_teacher
```

Example:

```python
False or True
```

Result:

```python
True
```

---

## `not`

`not` reverses a Boolean value.

```python
not True
```

becomes:

```python
False
```

And:

```python
not False
```

becomes:

```python
True
```

Example:

```python
if not is_valid:
    print("Invalid input")
```

---

# 13. Numeric Ranges and Chained Comparisons

Sometimes you need to check whether a number falls within a range.

One verbose approach is:

```python
if score >= 90 and score <= 100:
    print("A")
```

Python also supports chained comparisons:

```python
if 90 <= score <= 100:
    print("A")
```

This is easier to read.

---

## Grade Calculator

A more efficient approach is:

```python
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")
```

If:

```text
score = 87
```

Python checks:

```python
87 >= 90
```

False.

Then:

```python
87 >= 80
```

True.

So:

```text
Grade: B
```

Notice that we don't need:

```python
score <= 89
```

in the second condition.

Why?

Because if the score had been 90 or higher, the first condition would already have caught it.

This is an important consequence of checking `elif` conditions from top to bottom.

---

# 14. The `match` Statement

Python also provides `match`, which can be useful when comparing a value against several possible patterns.

Example:

```python
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

The:

```python
|
```

allows multiple values to match the same case.

This:

```python
case "Harry" | "Hermione" | "Ron":
```

means:

> If the value is Harry OR Hermione OR Ron.

The:

```python
case _:
```

is a wildcard.

It functions similarly to an `else` catch-all.

---

## Equivalent `if` Version

```python
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

Both approaches express the same basic decision.

---

# 15. The Modulo Operator `%`

The modulo operator:

```python
%
```

returns the **remainder** after division.

Example:

```python
4 % 2
```

Result:

```python
0
```

Because 4 divides evenly by 2.

Another example:

```python
7 % 2
```

Result:

```python
1
```

Because:

```text
7 ÷ 2 = 3 remainder 1
```

Modulo is particularly useful for checking whether numbers are even or odd.

---

## Checking for Even Numbers

```python
x = 8

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Why does this work?

Every even number has a remainder of `0` when divided by `2`.

```python
8 % 2 → 0
10 % 2 → 0
12 % 2 → 0
```

Odd numbers produce a remainder of `1`.

```python
7 % 2 → 1
9 % 2 → 1
11 % 2 → 1
```

---

# 16. Returning Boolean Expressions

Suppose you write:

```python
def is_even(n):

    if n % 2 == 0:
        return True
    else:
        return False
```

This works.

But it is unnecessarily verbose.

The condition:

```python
n % 2 == 0
```

already evaluates to:

```python
True
```

or:

```python
False
```

Therefore, simply return it:

```python
def is_even(n):
    return n % 2 == 0
```

This is a powerful simplification pattern.

Whenever you see:

```python
if condition:
    return True
else:
    return False
```

you can generally write:

```python
return condition
```

---

## Complete Example

```python
def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
```

Example:

```text
What's x? 7
Odd
```

The function:

```python
is_even(7)
```

returns:

```python
False
```

Therefore the `else` branch executes.

---

# 17. String Methods Used with Conditionals

Conditionals become much more useful when combined with string methods.

Common methods include:

```python
.startswith()
.endswith()
.lower()
.upper()
.strip()
.replace()
.split()
.join()
.find()
```

These methods allow you to transform or inspect strings before making decisions.

---

## `.startswith()`

Checks whether a string begins with a particular sequence.

```python
greeting = "hello there"

if greeting.startswith("hello"):
    print("Hello!")
```

Result:

```text
Hello!
```

---

## `.endswith()`

Checks whether a string ends with a particular sequence.

```python
file_name = "photo.png"

if file_name.endswith(".png"):
    print("PNG image")
```

Result:

```text
PNG image
```

---

## `.lower()`

Converts letters to lowercase.

```python
name = "HARRY"

print(name.lower())
```

Output:

```text
harry
```

Useful for case-insensitive comparisons:

```python
if name.lower() == "harry":
    print("Welcome!")
```

---

## `.upper()`

Converts letters to uppercase.

```python
name = "harry"

print(name.upper())
```

Output:

```text
HARRY
```

---

## `.strip()`

Removes leading and trailing whitespace.

```python
name = "   Harry   "

name = name.strip()

print(name)
```

Output:

```text
Harry
```

This can be useful when processing user input.

---

## `.replace()`

Replaces one sequence with another.

```python
text = "hello world"

text = text.replace("world", "Python")

print(text)
```

Output:

```text
hello Python
```

---

## `.split()`

Splits a string into pieces.

Example:

```python
expression = "6 * 7"

parts = expression.split(" ")
```

Result:

```python
["6", "*", "7"]
```

You can also unpack the result:

```python
x, y, z = expression.split(" ")
```

Now:

```python
x → "6"
y → "*"
z → "7"
```

This is useful for processing structured user input.

---

## `.join()`

Combines strings into one string.

Example:

```python
words = ["Python", "is", "fun"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
Python is fun
```

---

## `.find()`

Searches for a substring and returns its position.

```python
text = "hello world"

print(text.find("world"))
```

The result is the index where `"world"` begins.

---

# 18. Practical Example: Greeting Classifier

A practical conditional program can classify greetings.

```python
def main():
    greeting = input("Greeting: ")

    if greeting.startswith("hello"):
        say_greeting("$0")
    elif greeting.startswith("h"):
        say_greeting("$20")
    else:
        say_greeting("$100")


def say_greeting(finalGreeting):
    print(finalGreeting)


main()
```

Example:

```text
Greeting: hi there
$20
```

The logic is:

```text
Starts with "hello"?
    ↓
YES → $0

NO
 ↓

Starts with "h"?
    ↓
YES → $20

NO
 ↓

$100
```

This demonstrates:

* Functions
* `if`
* `elif`
* `else`
* String methods
* User input
* Function arguments

---

# 19. Practical Example: File Extension / MIME Type

A program can determine a file's MIME type based on its extension.

```python
file_name = input("File name: ").lower()

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg"):
    print("image/jpeg")
elif file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
```

Example:

```text
File name: photo.PNG
image/png
```

Notice:

```python
.lower()
```

is applied first.

Therefore:

```text
photo.PNG
```

becomes:

```text
photo.png
```

and can be compared reliably.

This example combines:

```python
input()
.lower()
.endswith()
if
elif
else
```

---

# 20. Practical Example: Answer to Life, the Universe, and Everything

The program accepts multiple valid representations of the answer.

```python
answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
)

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
```

The following are accepted:

```text
42
forty-two
forty two
```

This demonstrates combining conditions with:

```python
or
```

---

# 21. Practical Example: Simple Interpreter

A simple interpreter can take an expression such as:

```text
6 * 7
```

and perform the operation.

```python
expression = input("Expression: ")

x, y, z = expression.split(" ")

if y == "+":
    a = int(x) + int(z)
    print(float(a))

elif y == "-":
    a = int(x) - int(z)
    print(float(a))

elif y == "*":
    a = int(x) * int(z)
    print(float(a))

else:
    a = int(x) / int(z)
    print(float(a))
```

Example:

```text
Expression: 6 * 7
42.0
```

The input:

```text
6 * 7
```

is split into:

```text
x = "6"
y = "*"
z = "7"
```

The program then checks the operator:

```python
if y == "+":
```

```python
elif y == "-":
```

```python
elif y == "*":
```

and performs the appropriate operation.

Notice that `input()` returns strings, so:

```python
int(x)
```

and:

```python
int(z)
```

are needed before performing integer arithmetic.

The result is converted to a float:

```python
float(a)
```

so the output is:

```text
42.0
```

---

# 22. Practical Example: Meal Time Converter

The program can convert a time such as:

```text
12:15
```

into a decimal representation of the hour.

```python
def main():
    meal_time = input("What time is it? 24-hour format ")
    convert(meal_time)


def convert(time):
    hour, minutes = time.split(":")

    x = float(hour)
    y = float(minutes)

    z = y / 60
    w = x + z

    if w > 7 and w <= 8:
        print("breakfast time")

    elif w > 12 and w <= 13:
        print("lunch time")

    elif w > 18 and w <= 19:
        print("dinner time")

    else:
        print("")


if __name__ == "__main__":
    main()
```

Example:

```text
What time is it? 24-hour format 12:15
lunch time
```

---

## How the Conversion Works

Suppose:

```text
12:15
```

After:

```python
hour, minutes = time.split(":")
```

we have:

```python
hour = "12"
minutes = "15"
```

Convert them:

```python
x = float(hour)
y = float(minutes)
```

Now:

```python
x = 12.0
y = 15.0
```

Convert minutes into a fraction of an hour:

```python
z = y / 60
```

Therefore:

```text
15 / 60 = 0.25
```

Then:

```python
w = x + z
```

becomes:

```text
12.25
```

The program checks:

```python
w > 12 and w <= 13
```

which is true.

Therefore:

```text
lunch time
```

is printed.

---

# 23. The `__name__ == "__main__"` Pattern

You will often see:

```python
if __name__ == "__main__":
    main()
```

This is not necessary simply to make `main()` work.

It determines whether the file is being **run directly** or **imported by another file**.

When the file is executed directly:

```python
__name__
```

is:

```python
"__main__"
```

Therefore:

```python
if __name__ == "__main__":
```

is true, and:

```python
main()
```

runs.

If the file is imported by another Python file, the condition is false.

This prevents `main()` from automatically running merely because another program imported the module.

Mental model:

```text
Did I run this file directly?
        ↓
      YES
        ↓
    run main()

        OR

Was this file imported?
        ↓
      YES
        ↓
 don't automatically run main()
```

---

# 24. Nested Conditionals

A conditional can contain another conditional.

This is called a **nested conditional**.

Example:

```python
def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":

        if players == "Multiplayer":
            recommend("Poker")

        elif players == "Single-player":
            recommend("Klondike")

        else:
            print("Enter a valid number of players")

    elif difficulty == "Casual":

        if players == "Multiplayer":
            recommend("Hearts")

        elif players == "Single-player":
            recommend("Clock")

        else:
            print("Enter a valid number of players")

    else:
        print("Enter a valid difficulty")


def recommend(game):
    print("You might like", game)


main()
```

The program first asks:

```text
Difficult or Casual?
```

Then asks:

```text
Multiplayer or Single-player?
```

The second decision depends on the first.

The structure is:

```text
Difficulty
│
├── Difficult
│   │
│   ├── Multiplayer → Poker
│   └── Single-player → Klondike
│
└── Casual
    │
    ├── Multiplayer → Hearts
    └── Single-player → Clock
```

---

# 25. Flattening Nested Conditionals with Boolean Logic

Nested conditionals aren't always necessary.

The same program can be flattened by validating inputs first and then combining conditions.

```python
def main():
    difficulty = input("Difficult or Casual? ")

    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ")

    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")

    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")

    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")

    else:
        recommend("Clock")


def recommend(game):
    print("You might like", game)


main()
```

This demonstrates:

```python
and
or
not
```

working together.

---

## Why Validate First?

The program first establishes:

```text
Is difficulty valid?
```

If not:

```python
return
```

ends the function early.

Then it establishes:

```text
Is players valid?
```

If not:

```python
return
```

ends the function.

Only after the inputs have been validated does the program decide which game to recommend.

This produces a flatter structure.

---

# 26. Functions and Conditionals Working Together

Conditionals and functions are not separate concepts.

They work together constantly.

Example:

```python
def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
```

Here:

```python
is_even(x)
```

returns a Boolean.

The conditional then uses that Boolean:

```python
if is_even(x):
```

This demonstrates a powerful programming pattern:

```text
Function
   ↓
produces True/False
   ↓
Conditional
   ↓
makes decision
```

Functions can therefore encapsulate logic that conditionals use.

---

# 27. Indentation and Conditional Blocks

Indentation is significant in Python.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

The indentation tells Python that:

```python
print("Adult")
```

belongs to the `if`.

This is different from languages that use braces such as:

```text
{
}
```

Python uses indentation to define blocks.

Incorrect indentation can cause:

```text
IndentationError
```

or, worse, produce code whose logic is different from what you intended.

Always pay attention to which statements belong inside which conditional.

---

# 28. Common Beginner Mistakes

## Mistake 1: Using `=` instead of `==`

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

Remember:

```text
=   → assign
==  → compare
```

---

## Mistake 2: Forgetting Case Sensitivity

This:

```python
"Audi" == "audi"
```

is:

```python
False
```

If capitalization shouldn't matter:

```python
car.lower() == "audi"
```

---

## Mistake 3: Using `elif` When Every Condition Should Be Checked

If several conditions can be true:

```python
if condition1:
    ...

if condition2:
    ...

if condition3:
    ...
```

Use an `elif` chain when the outcomes are mutually exclusive:

```python
if condition1:
    ...

elif condition2:
    ...

elif condition3:
    ...
```

---

## Mistake 4: Automatically Adding `else`

You don't always need:

```python
else:
```

If no default action is required, simply use:

```python
if condition:
    ...
```

---

## Mistake 5: Writing More Conditions Than Necessary

Instead of:

```python
if x < y or x > y:
```

use:

```python
if x != y:
```

Look for opportunities to simplify logic.

---

# 29. Choosing the Right Conditional

| Statement                | Best Used When                                   |
| ------------------------ | ------------------------------------------------ |
| `if`                     | Only one condition needs checking                |
| `if...else`              | Exactly two possible outcomes                    |
| `if...elif...else`       | Several mutually exclusive outcomes              |
| Multiple `elif`          | Many exclusive choices                           |
| Multiple `if` statements | More than one condition may be true              |
| `match`                  | Matching a value against multiple patterns/cases |

---

## Quick Decision Guide

### One decision?

Use:

```python
if
```

### Two possible outcomes?

Use:

```python
if
else
```

### Several mutually exclusive outcomes?

Use:

```python
if
elif
elif
else
```

### Several conditions can independently be true?

Use:

```python
if
if
if
```

### Many values need to match specific cases?

Consider:

```python
match
```

---

# 30. Core Mental Model

The most important thing to understand from this lecture is not the syntax.

It is the **logic**.

A conditional is fundamentally asking a question:

```text
Is this true?
```

For example:

```python
age >= 18
```

Python evaluates it:

```text
True
```

or:

```text
False
```

Then your program chooses what to do.

Think of conditionals as a decision tree:

```text
                 CONDITION
                     │
             ┌───────┴───────┐
           True             False
             │                 │
          ACTION            ACTION
```

With multiple conditions:

```text
             condition 1?
              /       \
           True       False
            │           │
         action      condition 2?
                      /       \
                   True       False
                    │           │
                 action       action
```

This is the foundation of program control flow.

---

# 31. Key Takeaways

You should understand all of the following after this lecture:

* Conditionals allow programs to make decisions.
* Conditional tests evaluate to `True` or `False`.
* Python has two Boolean values: `True` and `False`.
* `=` assigns a value.
* `==` compares two values.
* `!=` checks whether values are different.
* `>` means greater than.
* `<` means less than.
* `>=` means greater than or equal to.
* `<=` means less than or equal to.
* String comparisons are case-sensitive.
* `.lower()` can be used for case-insensitive comparisons.
* Strings are immutable.
* `.lower()` returns a new string rather than changing the original.
* `if` handles a single condition.
* `if...else` handles two possible outcomes.
* `if...elif...else` handles multiple mutually exclusive outcomes.
* `elif` chains stop at the first true condition.
* Multiple independent `if` statements allow multiple conditions to execute.
* `else` is optional.
* `else` is a catch-all.
* `and` requires both conditions to be true.
* `or` requires at least one condition to be true.
* `not` reverses a Boolean value.
* Numeric ranges can use `and`.
* Python supports chained comparisons such as:

  ```python
  90 <= score <= 100
  ```
* `match` can be used for pattern-based matching.
* `case _` acts as a wildcard.
* `%` returns the remainder after division.
* Modulo is useful for detecting even and odd numbers.
* Boolean expressions can be returned directly from functions.
* `.startswith()` checks the beginning of a string.
* `.endswith()` checks the end of a string.
* `.lower()` converts text to lowercase.
* `.upper()` converts text to uppercase.
* `.strip()` removes leading/trailing whitespace.
* `.replace()` replaces text.
* `.split()` breaks strings into pieces.
* `.join()` combines strings.
* `.find()` searches for text.
* Conditionals can work together with functions.
* Conditionals can be nested.
* Boolean logic can sometimes flatten nested conditionals.
* `if __name__ == "__main__":` controls whether a module runs its main function directly.
* Python uses indentation to define conditional blocks.
* Good programmers constantly look for ways to simplify unnecessary conditional logic.

---

# 32. Practice Questions

Try these without looking at the notes.

## Beginner

### 1. Adult Checker

Ask the user for their age.

Print:

```text
Adult
```

if they are 18 or older.

Otherwise print:

```text
Minor
```

---

### 2. Number Comparison

Ask the user for two numbers.

Print whether:

* The first is greater
* The second is greater
* They are equal

---

### 3. Username

Ask for a username.

Accept:

```text
admin
```

regardless of capitalization.

For example:

```text
Admin
ADMIN
admin
AdMiN
```

should all work.

---

### 4. Grade Calculator

Ask for a score and produce:

```text
A
B
C
D
F
```

based on numeric ranges.

---

## Intermediate

### 5. Even or Odd

Ask for a number and determine whether it is even or odd.

Use:

```python
%
```

---

### 6. Pizza Toppings

Create a list:

```python
toppings = ["pepperoni", "mushrooms", "olives"]
```

Use separate `if` statements to check each topping.

---

### 7. File Extension

Ask for a filename.

Detect:

```text
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
```

and print the appropriate MIME type.

---

### 8. Greeting Classifier

Ask for a greeting.

If it starts with:

```text
hello
```

print:

```text
$0
```

If it starts with:

```text
h
```

print:

```text
$20
```

Otherwise print:

```text
$100
```

---

## More Challenging

### 9. Simple Calculator

Ask the user for an expression such as:

```text
6 * 7
```

Support:

```text
+
-
*
/
```

Use `.split()` and conditional logic.

---

### 10. Meal Time

Ask for a time such as:

```text
12:15
```

Convert it to decimal hours and determine whether it is:

```text
breakfast time
lunch time
dinner time
```

---

### 11. Game Recommender

Ask:

```text
Difficult or Casual?
```

Then:

```text
Multiplayer or Single-player?
```

Recommend a game based on the combination.

Try implementing it first with **nested conditionals**, then rewrite it using:

```python
and
or
not
```

to flatten the structure.

---

## Final Challenge

Build a small program that asks the user for:

```text
Age
Student status
Country
Income
```

Then use conditionals and Boolean logic to determine whether they qualify for a fictional program.

Your goal is not just to make it work.

Your goal is to ask:

> Can I make the logic simpler?

> Are these conditions mutually exclusive?

> Should these be separate `if` statements?

> Do I actually need an `else`?

> Can a Boolean expression be returned directly?

That is the deeper lesson of conditionals: **learning to express decisions clearly and efficiently in code.**
