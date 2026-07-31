# Program Design Framework

## Project Name

**Name:**


---

# 1. Define the Problem

## Purpose

Explain why this program exists.

Do not describe the code, programming language, or technology.

Describe the problem being solved.

---

## Questions

### What problem does this program solve?

Answer:

---

### Who is using this program?

Answer:

---

### Why does someone need this program?

Answer:

---

## Problem Statement

Complete this sentence:

> This program helps __________ do __________.

Example:

> This program helps travelers track and manage vacation expenses.

Write your problem statement:

```text

```

---

# 2. Define User Goals

## Purpose

Understand what the user wants to accomplish.

Think:

> If this program worked perfectly, what would the user be able to do?

---

## The user should be able to:

- 
- 
- 
- 

---

## User Decisions

What choices does the user make?

Examples:

- Add expense
- View expenses
- Calculate totals
- Exit program

List decisions:

- 
- 
- 

---

# 3. Identify Things That Exist (Nouns)

## Purpose

Find the things your program needs to remember.

Look at your problem statement and user goals.

Ask:

> What nouns exist in this system?

Examples:

- Trip
- Expense
- Budget
- Category
- User

---

## Things in this program:

| Thing | Description |
|---|---|
| | |
| | |
| | |

---

# 4. Describe Each Thing

## Purpose

Determine what information describes each thing.

Ask:

> What details does this thing have?

---

# Thing 1

## Name:

## Information it contains:

- 
- 
- 

---

# Thing 2

## Name:

## Information it contains:

- 
- 
- 

---

# Thing 3

## Name:

## Information it contains:

- 
- 
- 

---

# 5. Determine Quantity (One vs Many)

## Purpose

Decide how many of each thing can exist.

Ask:

> Is this one thing or many things?

---

| Thing | Quantity | Reason |
|---|---|---|
| | One / Many | |
| | One / Many | |
| | One / Many | |

---

## Data Structure Thinking

Use these patterns:

### One thing with multiple details

Example:

```python
trip = {
    "destination": "New York",
    "budget": 2000
}
```

Usually:

```
Dictionary
```

---

### Many things

Example:

```python
expenses = [
    "Hotel",
    "Food",
    "Transport"
]
```

Usually:

```
List
```

---

### Many things with multiple details

Example:

```python
expenses = [
    {
        "name": "Hotel",
        "amount": 500
    },
    {
        "name": "Food",
        "amount": 100
    }
]
```

Usually:

```
List of dictionaries
```

---

# 6. Identify Actions (Verbs)

## Purpose

Find what the user and program can do.

Ask:

> What actions happen in this program?

Examples:

- Add
- View
- Update
- Delete
- Calculate
- Search

---

## Actions in this program:

| Action | Description |
|---|---|
| | |
| | |
| | |

---

# 7. Design Functions

## Purpose

Turn actions into functions.

A function should have one clear responsibility.

---

# Function 1

## Function Name:

```python
function_name()
```

---

## Purpose:

What does this function do?

Answer:

---

## Inputs:

What information does this function need?

- 
- 
- 

---

## Where does the information come from?

Examples:

- User input
- Another function
- Stored data

Answer:

---

## Process:

What steps happen inside this function?

1. 
2. 
3. 

---

## Does this function change data?

Yes / No

If yes, what changes?

---

## Output:

Does this function need to return something?

Yes / No

If yes:

What does it return?

---

# Function 2

## Function Name:

```python
function_name()
```

---

## Purpose:

---

## Inputs:

- 
- 
- 

---

## Process:

1. 
2. 
3. 

---

## Does this function change data?

Yes / No

---

## Output:

---

# 8. Define Data Relationships

## Purpose

Understand how things connect.

Ask:

> Does one thing contain or belong to another thing?

---

## Examples

A trip contains expenses:

```
Trip
 |
 └── Expenses
       |
       ├── Hotel
       ├── Food
       └── Transport
```

---

A bank system:

```
Customer
 |
 └── Accounts
       |
       └── Transactions
```

---

## Relationships in this program:

```

```

---

# 9. Define Program Flow

## Purpose

Describe what happens from start to finish.

Write the program as a story.

---

## Example

```
Program starts

Create required data

Display menu

User chooses option

Program performs action

Return to menu

User exits
```

---

## Program Flow:

```

```

---

# 10. Identify Repetition

## Purpose

Find things that happen repeatedly.

Ask:

> What keeps happening?

Examples:

- Menu keeps appearing
- Loop through expenses
- Check multiple records

---

## Repeated Actions:

- 
- 
- 

---

## Possible Solutions:

| Situation | Possible Tool |
|---|---|
| Repeat until user exits | while loop |
| Go through a collection | for loop |

---

# 11. Identify Decisions

## Purpose

Find where the program needs to choose.

Ask:

> Where does the program behave differently depending on a condition?

---

## Example

```
If user chooses option 1:
    Add expense

If user chooses option 2:
    View expenses

If user chooses option 3:
    Calculate total
```

---

## Decisions in this program:

- 
- 
- 

---

# Final Design Checklist

Before writing code:

- [ ] What problem does this solve?
- [ ] Who uses this program?
- [ ] What are the user's goals?
- [ ] What things exist?
- [ ] What information does each thing contain?
- [ ] Which things are one?
- [ ] Which things are many?
- [ ] What actions can happen?
- [ ] What functions are needed?
- [ ] How are things related?
- [ ] What repeats?
- [ ] Where are decisions made?
- [ ] What happens from start to finish?

---

# Coding Plan

Only begin coding after completing the design.

---

## Data Structures

What variables, lists, and dictionaries will exist?

```python

```

---

## Functions

List the functions you need:

```python

```

---

## Program Flow

Describe how the functions connect:

```python

```

---

# Reflection After Building

## What was easy?

---

## What was difficult?

---

## What would I improve?

---

## What new concepts did I learn?

---