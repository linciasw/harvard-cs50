# Program Design Template

**Project:** ______________________

---

## 1. Define the Problem

Describe the problem — not the code. Fill in:

> This program helps ______________________ do ______________________.

**Who uses it?**
______________________

**What should the user be able to do?** (their goals/decisions — this will become your menu)
-
-
-
-

---

## 2. Data — Things That Exist

For every noun in your problem statement, fill one row. This table *is* your data structures.

| Thing | One or Many? | What details does it hold? | Structure |
|---|---|---|---|
| | One / Many | | dict / list / list of dicts |
| | One / Many | | dict / list / list of dicts |
| | One / Many | | dict / list / list of dicts |

**Quick reference:**
- One thing, several details → `dict` — e.g. `trip = {"destination": "NY", "budget": 2000}`
- Many identical things, no details → `list` — e.g. `categories = ["Food", "Transport"]`
- Many things, each with details → `list of dicts` — e.g. `expenses = [{"name": "Hotel", "amount": 500}, ...]`

**How do the things relate?** (does one contain/belong to another?)
```
e.g. Trip
      └── Expenses
```

---

## 3. Actions → Functions

For each user goal from Section 1, define the function that does it.

| Function name | Inputs | Where do inputs come from? | What it does (1-2 steps) | Returns? |
|---|---|---|---|---|
| | | user input / stored data / another function | | |
| | | | | |
| | | | | |

---

## 4. Program Flow

Write it as a story, start to finish:

```
Program starts
Create/load data
Display menu
User chooses option → call matching function
Return to menu
User exits
```

**What repeats?** (→ usually a `while` loop, or `for` when looping over a list)
-

**Where does the program decide differently based on a condition?** (→ `if`/`elif`)
-

---

## 5. Before You Code — Checklist

- [ ] Problem statement written in plain English
- [ ] Every "thing" has a structure (dict / list / list of dicts)
- [ ] Every user goal has a matching function
- [ ] Flow is written start to finish
- [ ] Repetition and decisions identified

---

## 6. Reflection (after building)

**What was hardest?**
______________________

**What would you change?**
______________________

**New concept learned?**
______________________