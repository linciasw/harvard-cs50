# Python Programming Patterns — Complete Review

A collection of programming patterns I've learned so far.

These patterns are important because they appear repeatedly in different programs. Instead of memorizing individual exercises, learn to recognize the underlying pattern.

---

# Table of Contents

1. [Loop Through Every Item](#1-loop-through-every-item)
2. [Accumulator / Total](#2-accumulator--total)
3. [Counter](#3-counter)
4. [Maximum Value](#4-maximum-value)
5. [Minimum Value](#5-minimum-value)
6. [Average](#6-average)
7. [Searching](#7-searching)
8. [Boolean Flag](#8-boolean-flag)
9. [Filtering](#9-filtering)
10. [Building a New Collection](#10-building-a-new-collection)
11. [Counting by Category](#11-counting-by-category)
12. [Total by Category](#12-total-by-category)
13. [Running Total](#13-running-total)
14. [Loop Counter / Position](#14-loop-counter--position)
15. [Input Validation](#15-input-validation)
16. [`while True` Menu](#16-while-true-menu)
17. [Accumulator + Counter](#17-accumulator--counter)
18. [Maximum + Associated Value](#18-maximum--associated-value)
19. [List of Dictionaries](#19-list-of-dictionaries)
20. [Dictionary as a Record](#20-dictionary-as-a-record)
21. [Sentinel Value](#21-sentinel-value)
22. [Input → Process → Output](#22-input--process--output)
23. [Function for One Responsibility](#23-function-for-one-responsibility)
24. [Pattern Combinations](#24-pattern-combinations)
25. [Pattern Recognition](#25-pattern-recognition)
26. [Quick Reference](#26-quick-reference)
27. [Mental Model](#27-mental-model)
28. [Review Checklist](#28-review-checklist)

---

# 1. Loop Through Every Item

## The Pattern

Use a `for` loop when you need to perform an operation on every item in a collection.

```python
for item in items:
    print(item)
```

## Example

```python
prices = [10, 20, 15, 30]

for price in prices:
    print(price)
```

Output:

```text
10
20
15
30
```

## Mental Model

> "I have a collection and I need to do something with each item."

Common uses:

* Calculate totals
* Find the maximum
* Find the minimum
* Search
* Filter
* Count
* Transform data

---

# 2. Accumulator / Total

## The Pattern

An accumulator stores a value that grows as the loop runs.

The most common example is calculating a total.

```python
total = 0

for value in values:
    total += value
```

## Example

```python
prices = [10, 20, 15, 30]

total = 0

for price in prices:
    total += price

print(total)
```

Output:

```text
75
```

## Why Start at 0?

Because you are adding values.

```python
total = 0
```

Then:

```text
0 + 10 = 10
10 + 20 = 30
30 + 15 = 45
45 + 30 = 75
```

## General Rule

If you're **adding numbers together**, the accumulator usually starts at:

```python
0
```

---

# 3. Counter

## The Pattern

A counter keeps track of how many times something happens.

```python
count = 0

for item in items:
    if condition:
        count += 1
```

## Example

Count how many prices are greater than 20:

```python
prices = [10, 25, 30, 15, 40]

count = 0

for price in prices:
    if price > 20:
        count += 1

print(count)
```

Output:

```text
3
```

## Mental Model

> "How many?"

Whenever the question is:

* How many?
* How often?
* How many passed?
* How many failed?
* How many are above X?

Think:

```python
count = 0
```

and:

```python
count += 1
```

---

# 4. Maximum Value

## The Pattern

Find the largest value in a collection.

One approach is to use Python's built-in:

```python
maximum = max(values)
```

But manually finding a maximum is an important programming pattern.

```python
maximum = values[0]

for value in values:
    if value > maximum:
        maximum = value
```

## Example

```python
prices = [25, 10, 50, 30]

maximum = prices[0]

for price in prices:
    if price > maximum:
        maximum = price

print(maximum)
```

Output:

```text
50
```

## Why Start With the First Value?

You need a real value to compare against.

```python
maximum = prices[0]
```

Then ask:

> "Is the current value greater than my current maximum?"

```python
if price > maximum:
    maximum = price
```

## Important

Do **not** automatically start maximum at `0`.

This can fail:

```python
maximum = 0
```

If all values are negative:

```python
[-5, -10, -2]
```

the result would incorrectly remain `0`.

---

# 5. Minimum Value

## The Pattern

Find the smallest value.

```python
minimum = values[0]

for value in values:
    if value < minimum:
        minimum = value
```

## Example

```python
prices = [25, 10, 50, 30]

minimum = prices[0]

for price in prices:
    if price < minimum:
        minimum = price

print(minimum)
```

Output:

```text
10
```

## Mental Model

Maximum:

```python
if value > maximum:
```

Minimum:

```python
if value < minimum:
```

The structure is almost identical.

---

# 6. Average

## The Pattern

Average is:

```text
total / number_of_items
```

Python:

```python
average = total / len(values)
```

## Example

```python
prices = [10, 20, 30]

total = 0

for price in prices:
    total += price

average = total / len(prices)

print(average)
```

Output:

```text
20.0
```

## Important Connection

Average usually combines two patterns:

```text
Accumulator + Collection Size
```

or:

```text
Accumulator + Counter
```

Example:

```python
total = 0
count = 0

for price in prices:
    total += price
    count += 1

average = total / count
```

---

# 7. Searching

## The Pattern

Searching means checking whether something exists.

```python
for item in items:
    if item == target:
        print("Found")
```

## Example

```python
names = ["John", "Sarah", "David"]

target = "Sarah"

for name in names:
    if name == target:
        print("Found")
```

## Better Version

Use a Boolean flag when you need to remember the result.

```python
found = False

for name in names:
    if name == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")
```

## Mental Model

> "Does this thing exist?"

---

# 8. Boolean Flag

## The Pattern

A Boolean flag remembers whether something happened.

```python
found = False
```

Then:

```python
if condition:
    found = True
```

Finally:

```python
if found:
    ...
```

## Example

```python
passwords = ["abc123", "hello", "python"]

found = False

for password in passwords:
    if password == "python":
        found = True
        break

if found:
    print("Password found")
else:
    print("Password not found")
```

## Mental Model

Think:

```text
False = "It hasn't happened yet."

True = "It happened."
```

Common flags:

```python
found = False
valid = False
exists = False
logged_in = False
```

---

# 9. Filtering

## The Pattern

Filtering means selecting only items that satisfy a condition.

```python
filtered_items = []

for item in items:
    if condition:
        filtered_items.append(item)
```

## Example

```python
prices = [10, 25, 30, 15, 40]

expensive = []

for price in prices:
    if price >= 25:
        expensive.append(price)

print(expensive)
```

Output:

```text
[25, 30, 40]
```

## Mental Model

> "Keep the items that match."

---

# 10. Building a New Collection

## The Pattern

Start with an empty collection and add items as you process data.

```python
results = []

for item in items:
    results.append(item)
```

Usually there is a transformation or condition.

```python
results = []

for item in items:
    if condition:
        results.append(transformed_item)
```

## Example

```python
prices = [10, 20, 30]

discounted_prices = []

for price in prices:
    discounted = price * 0.9
    discounted_prices.append(discounted)

print(discounted_prices)
```

Output:

```text
[9.0, 18.0, 27.0]
```

## Mental Model

> "I'm creating a new collection from the old collection."

---

# 11. Counting by Category

## The Pattern

Sometimes you don't want one overall count.

You want separate counts for different categories.

A dictionary works well.

```python
counts = {}

for item in items:
    category = item["category"]

    if category not in counts:
        counts[category] = 0

    counts[category] += 1
```

## Example

```python
expenses = [
    {"category": "food", "amount": 50},
    {"category": "transport", "amount": 20},
    {"category": "food", "amount": 30},
    {"category": "activities", "amount": 100}
]

counts = {}

for expense in expenses:
    category = expense["category"]

    if category not in counts:
        counts[category] = 0

    counts[category] += 1

print(counts)
```

Result:

```python
{
    "food": 2,
    "transport": 1,
    "activities": 1
}
```

## Mental Model

> "How many of each type?"

---

# 12. Total by Category

## The Pattern

This is similar to counting by category, except you accumulate money instead of `1`.

```python
totals = {}

for item in items:
    category = item["category"]
    amount = item["amount"]

    if category not in totals:
        totals[category] = 0

    totals[category] += amount
```

## Example

```python
expenses = [
    {"category": "food", "amount": 50},
    {"category": "transport", "amount": 20},
    {"category": "food", "amount": 30}
]

totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category not in totals:
        totals[category] = 0

    totals[category] += amount

print(totals)
```

Result:

```python
{
    "food": 80,
    "transport": 20
}
```

## Key Connection

Counting:

```python
counts[category] += 1
```

Totaling:

```python
totals[category] += amount
```

Same structure.

Different accumulator.

---

# 13. Running Total

## The Pattern

A running total updates after every item.

```python
total = 0

for value in values:
    total += value
    print(total)
```

## Example

```python
expenses = [50, 20, 100, 30]

total = 0

for expense in expenses:
    total += expense
    print(total)
```

Output:

```text
50
70
170
200
```

## Mental Model

> "What is the total so far?"

This pattern is useful for:

* Bank balances
* Spending trackers
* Scores
* Sales
* Inventory
* Progress tracking

---

# 14. Loop Counter / Position

## The Pattern

Sometimes you need to know the position of the current item.

Use `enumerate()`:

```python
for index, item in enumerate(items):
    print(index, item)
```

## Example

```python
names = ["John", "Sarah", "David"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```text
0 John
1 Sarah
2 David
```

## Starting From 1

```python
for number, name in enumerate(names, start=1):
    print(number, name)
```

Output:

```text
1 John
2 Sarah
3 David
```

## Important

You do not always need to manually create:

```python
counter = 0
```

If you're simply tracking position, `enumerate()` is usually cleaner.

---

# 15. Input Validation

## The Pattern

Keep asking until the user provides valid input.

```python
while True:
    try:
        value = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input.")
```

## Example

```python
while True:
    try:
        price = float(input("Enter price: "))

        if price < 0:
            print("Price cannot be negative.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")
```

## Mental Model

> "Don't continue until the input is acceptable."

Validation usually involves:

1. Get input
2. Check input
3. Reject invalid input
4. Ask again
5. Continue when valid

---

# 16. `while True` Menu

## The Pattern

A menu repeatedly displays options until the user chooses to exit.

```python
while True:
    print("1. Add")
    print("2. View")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        ...
    elif choice == "2":
        ...
    elif choice == "3":
        break
```

## Example

```python
while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding expense...")

    elif choice == "2":
        print("Viewing expenses...")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
```

## Mental Model

> "Keep the program alive until the user tells it to stop."

This is particularly useful for:

* Expense trackers
* Inventory systems
* Banking applications
* Contact managers
* CRUD applications
* Command-line programs

---

# 17. Accumulator + Counter

## The Pattern

Calculate a total and count items at the same time.

```python
total = 0
count = 0

for value in values:
    total += value
    count += 1
```

Then:

```python
average = total / count
```

## Example

```python
prices = [10, 20, 30, 40]

total = 0
count = 0

for price in prices:
    total += price
    count += 1

average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
```

## Mental Model

You are tracking two different questions:

```text
total → "How much?"

count → "How many?"
```

---

# 18. Maximum + Associated Value

## The Pattern

Sometimes you don't just want the largest number.

You want the object associated with the largest number.

Example:

```python
expenses = [
    {"name": "Flight", "amount": 500},
    {"name": "Hotel", "amount": 800},
    {"name": "Food", "amount": 300}
]
```

You want:

```text
Hotel — 800
```

## Pattern

```python
highest = expenses[0]

for expense in expenses:
    if expense["amount"] > highest["amount"]:
        highest = expense
```

Then:

```python
print(highest["name"])
print(highest["amount"])
```

## Mental Model

Instead of remembering only:

```python
highest_amount
```

remember the **entire record** that produced it.

This is an important step toward working with real-world data.

---

# 19. List of Dictionaries

## The Pattern

A list of dictionaries is useful when you have multiple records containing related information.

```python
expenses = [
    {"category": "food", "amount": 50},
    {"category": "transport", "amount": 20},
    {"category": "activities", "amount": 100}
]
```

Each dictionary represents one record.

The list represents the collection of records.

## Accessing Data

```python
for expense in expenses:
    print(expense["category"])
    print(expense["amount"])
```

## Adding a Record

```python
expense = {
    "category": "food",
    "amount": 50
}

expenses.append(expense)
```

## Mental Model

Think:

```text
List
    ↓
many records

Dictionary
    ↓
one record
```

---

# 20. Dictionary as a Record

A dictionary can represent one real-world object or record.

```python
trip = {
    "destination": "New York",
    "days": 8,
    "budget": 2000
}
```

Access values using keys:

```python
print(trip["destination"])
print(trip["budget"])
```

Update values:

```python
trip["budget"] = 2500
```

Add new values:

```python
trip["currency"] = "USD"
```

## Mental Model

> "This dictionary describes one thing."

Examples:

```python
user = {}
product = {}
employee = {}
trip = {}
expense = {}
```

---

# 21. Sentinel Value

## The Pattern

A sentinel is a special value that tells a loop when to stop.

Example:

```python
while True:
    value = input("Enter a value or 'quit': ")

    if value == "quit":
        break

    print(value)
```

Here:

```text
"quit"
```

is the sentinel.

## Another Example

```python
while True:
    number = int(input("Enter number (0 to stop): "))

    if number == 0:
        break
```

## Mental Model

> "Keep going until I receive the special stop value."

---

# 22. Input → Process → Output

This is one of the most important overall programming patterns.

```text
INPUT
  ↓
PROCESS
  ↓
OUTPUT
```

## Example

```python
price = float(input("Enter price: "))

tax = price * 0.125

total = price + tax

print(total)
```

### Input

```python
price = float(input(...))
```

### Process

```python
tax = price * 0.125
total = price + tax
```

### Output

```python
print(total)
```

## Mental Model

When you don't know how to start a program, ask:

1. What information do I need?
2. What calculations or decisions do I need to make?
3. What result should I show?

---

# 23. Function for One Responsibility

## The Pattern

A function should ideally perform one clear job.

Instead of:

```python
def program():
    # 200 lines of code
```

break the program into smaller responsibilities.

Example:

```python
def get_price():
    ...

def calculate_total(prices):
    ...

def calculate_average(total, count):
    ...

def display_results(total, average):
    ...
```

## Example

```python
def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total
```

Then:

```python
prices = [10, 20, 30]

total = calculate_total(prices)

print(total)
```

## Mental Model

A function should answer:

> "What one job does this piece of code perform?"

---

# 24. Pattern Combinations

Real programs rarely use only one pattern.

They combine several.

## Example: Price Analyzer

Requirements:

* Get prices
* Validate prices
* Calculate total
* Count prices
* Find highest price
* Calculate average

This combines:

```text
Input
+
Validation
+
Loop
+
Accumulator
+
Counter
+
Maximum
+
Average
```

Example:

```python
prices = []

for _ in range(5):

    while True:
        try:
            price = float(input("Enter price: "))

            if price < 0:
                print("Price cannot be negative.")
                continue

            prices.append(price)
            break

        except ValueError:
            print("Invalid price.")

total = 0
count = 0
highest = prices[0]

for price in prices:
    total += price
    count += 1

    if price > highest:
        highest = price

average = total / count

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
```

---

# 25. Pattern Recognition

The goal is not to memorize hundreds of programs.

Instead, learn to recognize the question behind the requirement.

| Requirement                    | Pattern                    |
| ------------------------------ | -------------------------- |
| "Go through every price"       | Loop                       |
| "Add all prices"               | Accumulator                |
| "How many prices?"             | Counter                    |
| "Highest price"                | Maximum                    |
| "Lowest price"                 | Minimum                    |
| "Average price"                | Total + Count              |
| "Does this exist?"             | Search                     |
| "Remember whether it happened" | Boolean Flag               |
| "Keep only expensive items"    | Filtering                  |
| "Create a modified list"       | New Collection             |
| "How many in each category?"   | Category Counter           |
| "How much spent per category?" | Category Total             |
| "Total so far"                 | Running Total              |
| "What position is this?"       | `enumerate()`              |
| "Don't accept invalid input"   | Validation                 |
| "Keep showing options"         | `while True` Menu          |
| "Largest item and its name"    | Maximum + Associated Value |
| "Store many records"           | List of Dictionaries       |
| "Represent one object"         | Dictionary                 |
| "Stop when user enters X"      | Sentinel                   |
| "Organize code into jobs"      | Functions                  |

---

# 26. Quick Reference

## Loop

```python
for item in items:
    ...
```

## Total

```python
total = 0

for value in values:
    total += value
```

## Counter

```python
count = 0

for value in values:
    if condition:
        count += 1
```

## Maximum

```python
maximum = values[0]

for value in values:
    if value > maximum:
        maximum = value
```

## Minimum

```python
minimum = values[0]

for value in values:
    if value < minimum:
        minimum = value
```

## Average

```python
average = total / count
```

## Search

```python
found = False

for item in items:
    if item == target:
        found = True
        break
```

## Boolean Flag

```python
flag = False

if condition:
    flag = True
```

## Filtering

```python
results = []

for item in items:
    if condition:
        results.append(item)
```

## Category Count

```python
counts = {}

for item in items:
    category = item["category"]

    if category not in counts:
        counts[category] = 0

    counts[category] += 1
```

## Category Total

```python
totals = {}

for item in items:
    category = item["category"]
    amount = item["amount"]

    if category not in totals:
        totals[category] = 0

    totals[category] += amount
```

## Running Total

```python
total = 0

for value in values:
    total += value
    print(total)
```

## Position

```python
for index, item in enumerate(items):
    ...
```

## Validation

```python
while True:
    try:
        value = float(input("Enter value: "))
        break
    except ValueError:
        print("Invalid input.")
```

## Menu

```python
while True:

    choice = input("Choose: ")

    if choice == "1":
        ...
    elif choice == "2":
        ...
    elif choice == "3":
        break
```

## List of Dictionaries

```python
items = [
    {"name": "A", "value": 10},
    {"name": "B", "value": 20}
]
```

---

# 27. Mental Model

When you receive a programming problem, don't immediately start writing code.

First translate the requirements into patterns.

For example:

> Ask the user for 5 prices. Handle invalid prices. Calculate total, average, and highest price.

Break it down:

```text
Ask user for prices
        ↓
INPUT
        ↓
Need valid numbers
        ↓
VALIDATION
        ↓
Need to repeat 5 times
        ↓
LOOP
        ↓
Need to add prices
        ↓
ACCUMULATOR
        ↓
Need number of prices
        ↓
COUNTER / len()
        ↓
Need highest price
        ↓
MAXIMUM
        ↓
Need average
        ↓
TOTAL / COUNT
        ↓
OUTPUT
```

The problem becomes much easier once you recognize the patterns.

---

# 28. Review Checklist

When solving a programming problem, ask yourself:

## Step 1 — Input

* [ ] What information do I need?
* [ ] Where does it come from?
* [ ] Does the user enter it?
* [ ] Do I need to validate it?

## Step 2 — Data

* [ ] Do I need a variable?
* [ ] Do I need a list?
* [ ] Do I need a dictionary?
* [ ] Do I need a list of dictionaries?

## Step 3 — Loop

* [ ] Do I need to process multiple items?
* [ ] Should I use `for`?
* [ ] Should I use `while`?
* [ ] Do I need a menu?
* [ ] Do I need a sentinel value?

## Step 4 — Processing

Ask:

> "What question am I trying to answer?"

### If the question is:

**"How much?"**

Think:

```python
total = 0
```

**"How many?"**

Think:

```python
count = 0
```

**"What's the highest?"**

Think:

```python
maximum = values[0]
```

**"What's the lowest?"**

Think:

```python
minimum = values[0]
```

**"What's the average?"**

Think:

```python
total / count
```

**"Does it exist?"**

Think:

```python
found = False
```

**"Which items match?"**

Think:

```python
results = []
```

**"How much of each type?"**

Think:

```python
dictionary + accumulator
```

**"How many of each type?"**

Think:

```python
dictionary + counter
```

**"Which record has the highest value?"**

Think:

```python
maximum + associated record
```

---

# The Big Picture

Most beginner programs are combinations of a relatively small number of patterns.

The important ones to recognize are:

```text
LOOPS
  ↓
Process every item


ACCUMULATORS
  ↓
Calculate totals


COUNTERS
  ↓
Count things


MAX / MIN
  ↓
Find extremes


SEARCH
  ↓
Find something


FLAGS
  ↓
Remember a state


FILTERING
  ↓
Keep matching items


DICTIONARIES
  ↓
Group / organize information


LISTS
  ↓
Store collections


VALIDATION
  ↓
Reject bad input


WHILE LOOPS
  ↓
Repeat until a condition changes


FUNCTIONS
  ↓
Separate responsibilities
```

And these patterns can be combined:

```text
Loop
 +
Accumulator
 +
Counter
 =
Average
```

```text
Loop
 +
Condition
 +
Counter
 =
Count matching items
```

```text
Loop
 +
Condition
 +
Accumulator
 =
Conditional total
```

```text
Loop
 +
Dictionary
 +
Counter
 =
Count by category
```

```text
Loop
 +
Dictionary
 +
Accumulator
 =
Total by category
```

```text
Loop
 +
Maximum
 +
Dictionary
 =
Find record with highest value
```

The real skill I'm developing is not memorizing syntax.

It is learning to look at a problem and think:

> **"Which programming pattern does this requirement represent?"**

Once I can recognize the pattern, I can build the code around it.
