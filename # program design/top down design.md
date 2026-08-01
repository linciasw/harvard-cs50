# Program Design Template (Top-Down Design)

**Project:** ______________________

Top-down design means starting with the big goal, then breaking it into smaller and smaller pieces until each piece is small enough to code directly. You don't decide data structures or write code until the breakdown is done.

---

## 1. Main Goal

One sentence, plain English, no code:

> This program helps ______________________ do ______________________.

**Who uses it?**
______________________

---

## 2. Level 1 — Major Tasks

Break the main goal into the 3–5 big jobs the program has to do. Don't go into detail yet — just name the major pieces.

Example for a vacation expense tracker:
- Manage the trip
- Manage expenses
- Show reports/totals
- Run the menu

**Your Level 1 tasks:**
-
-
-
-

---

## 3. Level 2 — Break Each Task Down

For each Level 1 task, break it into the smaller actions inside it. Keep breaking down until an action is small enough that you could write it as a single function in a few lines.

**Task 1:** ______________________
-
-

**Task 2:** ______________________
-
-

**Task 3:** ______________________
-
-

**Task 4:** ______________________
-
-

---

## 4. Hierarchy Chart

Draw the breakdown as a tree — main goal at top, Level 1 tasks below it, Level 2 actions below those. Each leaf will become one function.

```
                    Main Goal
         ┌──────────┬──────────┬──────────┐
      Task 1      Task 2      Task 3     Task 4
      ┌──┴──┐     ┌──┴──┐
   action  action action  action
```

Redraw it here with your actual tasks:

```

```

---

## 5. Data — Now Decide Structures

Only now, once you know what each function needs to work with, figure out the data. For every noun your leaf-level actions touch, ask **"is this one thing, or many things?"**

| Thing | One or Many? | Details it holds | Structure |
|---|---|---|---|
| | One / Many | | dict / list / list of dicts |
| | One / Many | | dict / list / list of dicts |
| | One / Many | | dict / list / list of dicts |

**Quick reference:**
- One thing, several details → `dict` — e.g. `trip = {"destination": "NY", "budget": 2000}`
- Many identical things, no details → `list` — e.g. `categories = ["Food", "Transport"]`
- Many things, each with details → `list of dicts` — e.g. `expenses = [{"name": "Hotel", "amount": 500}, ...]`

**Watch for this trap:** a word can describe a *property of another thing* rather than being an independent thing itself. Ask: "is this standalone, or is it describing one instance of something else?"
- "Category" of an expense → not its own list, it's a key inside the expense dict: `{"name": "Hotel", "amount": 500, "category": "Lodging"}`
- A separate `categories` list only makes sense if you need the full set independently — e.g. to build a menu or validate input

---

## 6. Turn Each Leaf Into a Function

One row per leaf from your hierarchy chart.

| Function name | Inputs | Where inputs come from | What it does (1-2 steps) | Returns? |
|---|---|---|---|---|
| | | user input / stored data / another function | | |
| | | | | |
| | | | | |

---

## 7. Program Flow

Write start to finish, in order, using the functions from Section 6:

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

## 8. Before You Code — Checklist

- [ ] Main goal written in plain English
- [ ] Major tasks identified (Level 1)
- [ ] Each task broken down to function-sized pieces (Level 2)
- [ ] Hierarchy chart drawn
- [ ] Every "thing" has a structure (dict / list / list of dicts)
- [ ] Every leaf action has a matching function
- [ ] Flow written start to finish
- [ ] Repetition and decisions identified

---

## 9. Reflection (after building)

**What was hardest?**
______________________

**What would you change?**
______________________

**New concept learned?**
______________________