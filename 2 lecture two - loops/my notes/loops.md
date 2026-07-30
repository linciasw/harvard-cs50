# Python Files Documentation

A combined, sectioned reference covering all uploaded .py files, organized by topic. Each section includes what the code does and an example of its output.

## Table of Contents
- [Functions & Program Structure](#functions-program-structure)
  - [mario.py](#mariopy)
  - [letters.py](#letterspy)
- [Loops (while & for)](#loops-while-for)
  - [cat.py](#catpy)
  - [coke.py](#cokepy)
  - [water.py](#waterpy)
- [Lists & List Methods](#lists-list-methods)
  - [results.py](#resultspy)
  - [sokoban.py](#sokobanpy)
- [Dictionaries](#dictionaries)
  - [hogwarts.py](#hogwartspy)
  - [distances.py](#distancespy)
  - [report.py](#reportpy)
  - [bee.py](#beepy)
  - [coreyschafer.py](#coreyschaferpy)
  - [nutrition.py](#nutritionpy)
- [Comprehensions](#comprehensions)
  - [camel.py](#camelpy)
  - [comprehensions.py](#comprehensionspy)
  - [list_comprehensions.py](#list-comprehensionspy)
  - [dictionary_comprehensions.py](#dictionary-comprehensionspy)
- [Strings](#strings)
  - [shows.py](#showspy)
  - [phone.py](#phonepy)
  - [twttr.py](#twttrpy)
  - [plates.py](#platespy)
- [Tuples](#tuples)
  - [location.py](#locationpy)

---

## Functions & Program Structure

### mario.py


#### Overview
This script prints a solid square of `#` characters (a "block pyramid" building block exercise). It demonstrates how a program can be broken down (**decomposed**) into small, single-purpose functions rather than writing everything in one nested loop.

Python starts execution by first defining all functions, then running any code that sits outside a function — which is why `main()` is called at the very bottom of the file.

#### Execution Entry Point

```python
def main():
    print_square(3)
```

`main()` is the starting point of the program. It calls `print_square(3)`, telling the program to draw a 3x3 square of hashes.

#### Core Function: `print_square`

```python
def print_square(size):
    for i in range(size):
         print_row(size)
```

This function loops `size` times (once per row) and delegates the actual printing of each row to a helper function, `print_row`. This is the decomposed version of what could otherwise be written as a nested loop:

```python
def print_square(size):
    for i in range(size):
        print("#" * size)
```

Breaking it into `print_square` + `print_row` keeps each function focused on one job: `print_square` handles *how many rows*, and `print_row` handles *what a row looks like*.

#### Helper Function: `print_row`

```python
def print_row(width):
    print("#" * width)
```

Multiplying a string by an integer in Python repeats it, so `"#" * width` produces a single line of `width` hash characters.

#### Alternative Approaches (commented out in the file)

The file preserves earlier iterations of the same idea, showing the thought process behind the final design:

- **Basic loop, one line at a time:**
  ```python
  for _ in range(3):
      print("#")
  ```
- **Fully nested loop version** (printing a square character-by-character):
  ```python
  def print_square(size):
      for i in range(size):
          for j in range(size):
              print("#", end="")
          print()
  ```
- **String repetition with an escaped newline:**
  ```python
  def print_row(height):
      print("#\n" * height, end="")
  ```

#### Key Takeaway
The core idea demonstrated here is **function decomposition**: as long as a function's name, parameters, and return behavior stay the same, its internal implementation can be rewritten freely without breaking any code that depends on it.

#### Example Output

```
#####
#####
#####
```

### letters.py


#### Overview
This script generates a personalized invitation letter for each name in a list, demonstrating how a `for` loop combined with a reusable function avoids repetitive code (one `print` call per name).

#### Entry Point

```python
def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]

    for name in names:
        print(write_letter(name, "Princess Peach"))


main()
```

`main()` defines the list of recipients, then loops over each `name`, passing it (along with a fixed sender, `"Princess Peach"`) into `write_letter()` and printing the result.

#### Letter-Building Function

```python
def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at 
        Peach's Castle this evening, 7:00 PM. 

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """
```

`write_letter` takes two parameters — `receiver` and `sender` — and returns a multi-line f-string (a triple-quoted string with embedded variables) formatted as an invitation. Because the receiver/sender names are inserted via f-string interpolation (`{receiver}`, `{sender}`), the same template works for any pair of names.

#### Alternative / Earlier Approaches (commented out in the file)

- **Index-based loop:**
  ```python
  for i in range(len(names)):
      print(write_letter(names[i], "Princess Peach"))
  ```
  This works but is less readable than iterating directly over `names`.
- **Fully manual, no loop at all:** one `write_letter(...)` call per name, hardcoded — the version the final loop-based code replaces.

#### Key Takeaway
Whenever the same operation needs to run once per item in a collection, a `for name in names:` loop is generally more readable and maintainable than either manual repetition or an index-based loop with `range(len(...))`.

#### Example Output

One letter of four (for "Mario"):
```
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear Mario,

        You are cordially invited to a ball at 
        Peach's Castle this evening, 7:00 PM. 

        Sincerely,
        Princess Peach
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
```
(repeats for Luigi, Daisy, and Yoshi)

## Loops (while & for)

### cat.py


#### Overview
This script prompts the user for a positive number and prints "meow" that many times. The file is really a teaching progression: it keeps the same end result while walking through several different implementations, from a plain `while` loop to a fully decomposed pair of functions.

#### Final Implementation

```python
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
```

##### `get_number()`
Uses an infinite `while True` loop to keep re-prompting the user until they enter a positive integer, at which point it `return`s that value (which also exits the loop, since a `return` inside a function ends execution immediately).

##### `meow(n)`
Takes the validated number and loops `n` times, printing `"meow"` on each pass. The loop variable itself isn't needed, so it's named `_` — a Python convention signaling "this variable exists only because the loop syntax requires it."

#### Earlier / Alternative Approaches (commented out in the file)

- **Manual repetition:** three separate `print("meow")` calls.
- **Counting down with a while loop:**
  ```python
  i = 3
  while i != 0:
      print("Meow")
      i = i - 1
  ```
- **Counting up with a while loop:**
  ```python
  i = 1
  while i <= 3:
      print("meow")
      i = i + 1
  ```
- **Zero-indexed counting** (matching Python's usual indexing convention):
  ```python
  i = 0
  while i < 3:
      print("meow")
      i = i + 1
  ```
- **For loop over a list:**
  ```python
  for i in [0, 1, 2]:
      print("meow")
  ```
- **For loop with `range()`:** avoids hardcoding a list, scales to any number.
- **String multiplication:** `print("meow" * 3)` (with an escape-character fix to avoid `meowmeowmeow` running together: `print("meow\n" * 3, end="")`).
- **Manual input validation without a loop**, shown as an example of *why* a loop is better — nesting `if` statements to re-ask for input doesn't scale ("we could potentially be writing this for infinity").

#### Key Takeaway
`while True` combined with a `return` or `break` is a common pattern for **validating user input**: keep asking until the input meets the required condition, then exit the loop naturally.

#### Example Output

Input: `3`
```
What's n? 3
meow
meow
meow
```

### coke.py


#### Problem
Prompt the user to insert coins one at a time, informing them of the remaining amount due after each coin, until at least 50 cents has been inserted — then report any change owed. Only accepted coin denominations should be counted; anything else should be ignored.

#### Why a `while` loop (not a `for` loop)
The file's comments explain the design choice directly: a `for` loop is appropriate when the number of repetitions is known in advance. Here, the number of coins the user will insert is unknown — it could be two 25-cent coins, ten 5-cent coins, or any other combination — so a `while` loop (which keeps checking a condition rather than counting a fixed number of iterations) is the right tool.

#### Implementation

```python
def main():
    price = 50

    while price > 0:
        print(f"Amount due: {price}")
        coin = int(input("Insert coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            price = price - coin

    print("Change owed: 0")


main()
```

##### How it works
1. `price` starts at 50 (cents still owed).
2. While `price > 0`, the loop:
   - Prints the current amount due.
   - Reads a coin value from the user.
   - If the coin is a valid denomination (25, 10, or 5 cents), subtracts it from `price`.
   - If the coin isn't valid, it's simply ignored (no `else` branch needed — the loop just continues to the next iteration).
3. Once `price` reaches 0 or below, the loop ends and `"Change owed: 0"` is printed.

Note: the commented-out `else: continue` was considered but is unnecessary — reaching the end of a `while` loop's body naturally sends control back to re-check the loop's condition, so an explicit `continue` doesn't change behavior here.

#### Key Takeaway
Use a `for` loop when the number of repetitions is known ahead of time; use a `while` loop when repetition should continue until some condition changes, as with an unpredictable number of coin insertions.

#### Example Output

Inputs: `25`, then `25`
```
Amount due: 50
Insert coin: 25
Amount due: 25
Insert coin: 25
Change owed: 0
```

### water.py


#### Overview
This script simulates monitoring soil moisture over successive days, printing a daily reading until the moisture level drops to a point where watering is needed. It demonstrates a `while` loop driven by a changing external condition, and relies on an imported helper module (`soil`) to supply the moisture readings.

#### Dependency

```python
from soil import sample
```

`sample()` is imported from a separate `soil` module (not shown in this file) and is assumed to return the current moisture percentage each time it's called — likely simulating a sensor reading that changes over time.

#### Implementation

```python
def main():
    moisture = sample()
    days = 0
    print(f"Day {days}: Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Day {days}: Moisture is {moisture}")

    print("Time to water!")
    

main()
```

##### How it works
1. `moisture = sample()` takes an initial reading before the loop starts, and `days` is initialized to `0` to track how many days have passed.
2. The first day's reading is printed immediately, so the initial moisture level is shown even before any looping occurs.
3. **While the moisture stays above 20%,** the loop:
   - Takes a new reading (`sample()`).
   - Increments the day counter.
   - Prints the day number and new moisture level.
4. Once `moisture` drops to 20% or below, the loop condition becomes false, the loop exits, and `"Time to water!"` is printed.

##### Why a `while` loop
As the comments note, `while` loops are well-suited to situations where the number of iterations isn't known ahead of time — here, no one knows in advance how many days it will take for the soil to dry out, only that the checking should continue *while* a certain condition (`moisture > 20`) remains true.

#### Alternative Considered (commented out)
A simpler version without any looping was shown first, just checking the moisture once:
```python
def main():
    moisture = sample()
    print(f"Moisture is {moisture}%")
```
This doesn't track change over time, which is why the `while`-loop version replaces it.

#### Key Takeaway
A `while` loop is the right tool when a program needs to keep repeating an action *until* some real-world or externally-driven condition changes, rather than for a predetermined number of times.

#### Example Output

Using sample moisture readings that happen to come in as 45%, 33%, 27%, then 18%:
```
Day 0: Moisture is 45%
Day 1: Moisture is 33
Day 2: Moisture is 27
Day 3: Moisture is 18
Time to water!
```
(Actual output will vary since `sample()` is meant to represent a live, changing sensor reading.)

## Lists & List Methods

### results.py


#### Overview
A short demonstration of Python **list methods** — `append`, `extend`, `remove`, `insert`, and `reverse` — used to build up and rearrange a list of characters.

#### Final Code

```python
results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr"]

results.remove("Bowser")
results.insert(0, "Bowser")
results.reverse()

print(results)
```

##### Step-by-step behavior

1. **Starting list** already contains all 8 names.
2. `results.remove("Bowser")` — removes the first (and here, only) occurrence of `"Bowser"` from the list.
3. `results.insert(0, "Bowser")` — puts `"Bowser"` back into the list, but specifically at index `0` (the front), rather than appending it to the end.
4. `results.reverse()` — reverses the entire list in place, so the last item becomes first and vice versa.
5. `print(results)` — prints the final, reordered list.

#### Methods Explored (shown in comments as build-up)

- **`.append(item)`** — adds a single item to the end of the list:
  ```python
  results.append("Princess")
  ```
  Note: if you `.append()` a list (e.g. `results.append(["Bowser", "Donkey Kong Jr."])`), the whole list is added as a *single nested element*, not merged in — producing something like:
  ```python
  ['Mario', 'Luigi', ..., ['Bowser', 'Donkey Kong Jr.']]
  ```
- **`.extend(iterable)`** — the fix for the above: merges the items of another list directly into the original list, rather than nesting it:
  ```python
  results.extend(["Bowser", "Donkey Kong Jr."])
  # ['Mario', 'Luigi', ..., 'Bowser', 'Donkey Kong Jr.']
  ```
- **`.remove(item)`** — removes the first matching item from the list (used here to undo the earlier nested-list mistake, and again in the final version to reposition `"Bowser"`).
- **`.insert(index, item)`** — inserts an item at a specific position rather than at the end.
- **`.reverse()`** — reverses the list's order in place.

#### Key Takeaway
`append()` adds one item (even if that "item" is itself a list, it stays nested); `extend()` merges another iterable's *contents* in; `insert()` gives control over *where* an item lands; `reverse()` flips the whole list's order.

#### Example Output

```
['Donkey Kong Jr', 'Toad', 'Koopa Troopa', 'Yoshi', 'Princess', 'Luigi', 'Mario', 'Bowser']
```

### sokoban.py


#### Overview
This script simulates a simple **action history tracker**, similar to an undo/redo system in a game (referencing Sokoban, a puzzle game about pushing boxes). It demonstrates the list methods `append()`, `pop()`, and `clear()`.

#### Implementation

```python
def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)
    
        print(history)


main()
```

##### How it works
- `history = []` starts with an empty list that will track every action taken.
- The program runs in an infinite loop (`while True`), continuously asking the user for the next `action`.
- **If the action is `"Undo"`:** `history.pop()` removes and returns the *last* item added to the list, which is stored in `undone` and printed — effectively reversing the most recent action.
- **If the action is `"Restart"`:** `history.clear()` empties the entire list, wiping all recorded history.
- **Otherwise:** the action is treated as a new move and added to the end of the list via `history.append(action)`.
- After every input, the current state of `history` is printed, so the user can see the effect of their last command.

##### List methods demonstrated
- **`.append(item)`** — adds an item to the end of the list (used for recording a new action).
- **`.pop()`** — removes and returns the *last* item in the list (used for undoing the most recent action). Note: calling `.pop()` on an empty list would raise an error, so this program assumes there's always at least one action in `history` before `"Undo"` is used.
- **`.clear()`** — removes all items from the list at once (used for the "Restart" command).

#### Key Takeaway
A list's *end* naturally models a "most recent action" stack: appending records new actions, and popping removes the most recently added one — the same underlying idea behind undo functionality in many applications.

#### Example Output

Inputs: `push box`, `push box`, `Undo`
```
Action: push box
['push box']
Action: push box
['push box', 'push box']
Action: Undo
Undone: push box
['push box']
```
(The program then keeps looping forever, asking for the next `Action:`, since there's no built-in exit command.)

## Dictionaries

### hogwarts.py


#### Overview
This script demonstrates progressively richer ways to store and print structured data in Python: plain lists, dictionaries, and finally a **list of dictionaries** — the structure used to represent multiple records with multiple fields each (similar to a table of data).

#### Final Data Structure

```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Gryffindor", "patronus": None}
]
```

Each student is a dictionary with three keys (`name`, `house`, `patronus`), and all four student-dictionaries live inside one list. `None` is used for Draco's patronus to represent the absence of a value (he doesn't have a Patronus).

#### Printing Multiple Fields

```python
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
```

Looping over the list gives one dictionary (`student`) per iteration. Each field is accessed by its key (`student["name"]`), and `sep=", "` tells `print()` to join the three values with a comma and space instead of the default single space.

#### Progression Shown in Comments

The file builds up to this final structure step by step:

1. **Plain list, indexed manually:**
   ```python
   students = ["Hermione", "Harry", "Ron"]
   print(students[0])
   print(students[1])
   print(students[2])
   ```
2. **Plain list, looped over directly** (Python can iterate over any collection, not just strings):
   ```python
   for student in students:
       print(student)
   ```
3. **Plain list, looped by index with `range(len(...))`** — useful when you need the index itself (e.g. to print a rank: `i + 1`).
4. **Dictionary (single record, key-value pairs):**
   ```python
   students = {
       "Hermione": "Gryffindor",
       "Harry": "Gryffindor",
       "Ron": "Gryffindor",
       "Draco": "Slytherin"
   }
   ```
   Looping over a dictionary directly (`for student in students`) yields only the *keys*; to get key-value pairs you print both `student` and `students[student]`.
5. **List of dictionaries** (final version above) — needed once each record requires more than one associated field (here, both `house` and `patronus`).

#### Key Takeaway
As the data a program needs to represent grows more complex (more fields per record), the data structure should grow with it: single list → dictionary → list of dictionaries.

#### Example Output

```
Hermione, Gryffindor, Otter
Harry, Gryffindor, Stag
Ron, Gryffindor, Jack Russell terrier
Draco, Gryffindor, None
```

### distances.py


#### Overview
This script converts a set of astronomical distances (stored in Astronomical Units, AU) into meters, demonstrating how to loop over dictionary **values** specifically, and how to delegate a calculation to a separate helper function.

#### Data

```python
distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}
```

Each key is a spacecraft's name; each value is its distance from Earth in AU.

#### Implementation

```python
def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    return au * 149597870700


main()
```

##### `main()`
Loops over `distances.values()`, which yields only the numeric distance values (ignoring the spacecraft names entirely). For each value, it calls `convert(distance)` and prints both the original AU figure and its converted meter equivalent.

##### `convert(au)`
A small, focused helper function: multiplies a distance in AU by the fixed conversion constant (1 AU ≈ 149,597,870,700 meters) and returns the result in meters.

#### Alternative Considered (commented out)

```python
for name in distances.keys():
    print(f"{name} is {distances[name]} AU from Earth")
```

This version loops over the **keys** (`.keys()`) instead, using each name to look up its corresponding distance via `distances[name]` — useful when the *names* matter, as opposed to the final version, which only needs the raw distance values for conversion.

#### Key Takeaway
`.values()` is the right choice when a loop only needs a dictionary's values and doesn't care about which key each value belongs to; `.keys()` (paired with bracket lookup) is better when the key itself needs to appear in the output.

#### Example Output

```
163 AU is 24384452924100 m
136 AU is 20345310415200 m
80 AU is 11967829656000 m
58 AU is 8676676500600 m
44 AU is 6582306310800 m
```

### report.py


#### Overview
This script builds a formatted text "report" from a dictionary of spacecraft data, using an f-string template. It demonstrates the difference between accessing dictionary values directly (which can raise an error if a key is missing) versus safely with `.get()` and a fallback default — plus a short aside on docstrings and f-strings.

#### Background Concepts (explained in comments)
- **Triple-quoted strings (`"""`)** are not automatically comments — they create multi-line strings, and are commonly used as **docstrings**: descriptive strings placed right after a function, class, or module definition to explain what it does.
- **f-strings** (strings prefixed with `f` or `F`) let you embed expressions directly inside `{}` placeholders, which are evaluated at runtime — a concise way to interpolate variables into text.

#### Final Implementation

```python
def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ============== REPORT =============

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU     
    Orbit: {spacecraft.get("orbit", "Unknown")}   

    ===================================
    """

main()
```

##### `main()`
- Starts with a dictionary containing only the spacecraft's `name`.
- Uses `.update({...})` to add two more keys (`distance` and `orbit`) at once, rather than setting each one individually (e.g. `spacecraft["distance"] = 0.01`, shown as an alternative in a comment).
- Passes the completed dictionary to `create_report()` and prints the result.

##### `create_report(spacecraft)`
Returns a multi-line f-string formatted as a labeled report. Each field uses `.get(key, "Unknown")` rather than direct bracket access (`spacecraft["name"]`) — this means that if a key happens to be missing from the dictionary, the report displays `"Unknown"` instead of the whole program crashing with a `KeyError`.

#### Earlier Version (commented out)

```python
def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ============== REPORT =============

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ===================================
    """
```

This earlier draft used direct bracket access (`spacecraft["name"]`) instead of `.get()`, meaning it would only work correctly if every expected key was guaranteed to be present — any missing key (e.g. no `"orbit"` field) would raise an error rather than gracefully falling back to a default.

#### Key Takeaway
When building a formatted report from a dictionary that might not have every field filled in, `.get(key, default)` is safer than direct bracket indexing, since it prevents the program from crashing on a missing key and instead substitutes a sensible placeholder.

#### Example Output

```
    ============== REPORT =============

    Name: James Webb Space Telescope
    Distance: 0.01 AU     
    Orbit: Sun   

    ===================================
```

### bee.py


#### Overview
This script models the scoring board of a spelling-bee-style game, printing each valid word alongside its point value. The file preserves an earlier, more interactive version of the game (as a commented-out block) alongside the final, simplified version that just displays the word list.

#### Data

```python
WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}
```

A dictionary mapping each valid word to its point value.

#### Final Implementation

```python
def main():
    print("Welcome to Spelling Bee!")

    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")


main()
```

`WORDS.items()` yields each `(key, value)` pair in the dictionary, letting the loop unpack both the `word` and its `points` at once and print them together in a single f-string.

#### Earlier, Interactive Version (commented out)

```python
def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.")

    print("That's the game!")
```

This version actually plays the game:
- `len(WORDS)` reports the count of key-value pairs remaining, used both to display "words left" and as the loop's exit condition (the loop runs `while len(WORDS) > 0`, i.e. until the dictionary is empty).
- Guessing `"GRAPHIC"` (the designated "winning" word) clears the whole dictionary at once with `.clear()`, ending the game immediately.
- Any other correct guess is checked with `guess in WORDS.keys()`, and if found, `.pop(guess)` both **removes** that word from the dictionary and **returns** its point value in one step — which is stored in `points` and printed.

#### Key Takeaway
`dict.items()` is the standard way to loop over both keys and values together; `dict.pop(key)` is useful whenever you need to both retrieve a value and remove its entry in a single operation (as with "using up" a guessed word so it can't be guessed again).

#### Example Output

```
Welcome to Spelling Bee!
PAIR was worth 4 points.
HAIR was worth 4 points.
CHAIR was worth 5 points.
GRAPHIC was worth 7 points.
```

### coreyschafer.py


#### Overview
This file is a set of notes and experiments (following along with a Corey Schafer tutorial video, per the comment "reached 8:19 in video") exploring Python **dictionary methods and operations**: `get()`, `update()`, `del`, `pop()`, `len()`, `keys()`, `values()`, and `items()`.

#### Sample Data

```python
student = {"name": "John", "age": 25, "courses": {"Math", "CompSci"}}
```

A dictionary can hold values of any data type — here, strings, an integer, and a **set** (`{"Math", "CompSci"}`) all live inside one dictionary. Dictionary keys can also be any (hashable) data type.

#### Final Active Code

```python
for key, value in student.items():
    print(key, value)
```

Loops over every key-value pair in `student` and prints them together.

#### Methods & Operations Explored (commented out in the file)

- **Direct key access:** `student["name"]` — returns the value for `"name"`.
- **`.get(key)`** — safely retrieves a value; returns `None` if the key doesn't exist (rather than raising an error, unlike direct bracket access):
  ```python
  student.get("phone")
  ```
- **`.get(key, default)`** — same as above, but returns a custom fallback value instead of `None` when the key is missing:
  ```python
  student.get("phone", "Not Found")
  ```
- **Adding a new key-value pair:**
  ```python
  student["phone"] = "555-5555"
  ```
- **Overwriting an existing key's value:**
  ```python
  student["name"] = "Jane"
  ```
- **`.update(dict)`** — merges another dictionary's keys/values into `student`, adding new keys and overwriting existing ones in a single call:
  ```python
  student.update({"name": "Jane", "age": 26, "phone": "555-5555"})
  ```
- **`del student["age"]`** — removes a key-value pair entirely.
- **`.pop(key)`** — also removes a key-value pair, but additionally *returns* the removed value (useful when you need to keep the removed value for later use):
  ```python
  age = student.pop("age")
  print(age)
  ```
- **`len(student)`** — returns the number of key-value pairs in the dictionary.
- **`.keys()`** — returns a view of all keys.
- **`.values()`** — returns a view of all values.
- **`.items()`** — returns a view of all `(key, value)` pairs together.
- **Looping over keys only:**
  ```python
  for key in student:
      print(key)
  ```

#### Key Takeaway
`del` and `.pop()` both remove a key-value pair, but `.pop()` is preferable when the removed value is still needed afterward, since it returns that value directly. `.get()` (with or without a default) is the safe way to look up a key that might not exist, avoiding a `KeyError`.

#### Example Output

```
name John
age 25
courses {'CompSci', 'Math'}
```
(Set ordering isn't guaranteed, so `courses` may print in a different order on another run.)

### nutrition.py


#### Problem
Prompt the user to input a fruit name (case-insensitively) and output the number of calories in one portion, based on a fixed lookup table (the FDA's fruit poster). Any input that isn't a recognized fruit should be ignored.

#### Data: The Lookup Table

```python
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}
```

A dictionary maps each fruit name (key) to its calorie count (value), giving constant-time lookup by name.

#### Main Function

```python
def main():
    fruit_requested = input("Item: ").lower()

    for key, value in fruits.items():
        if fruit_requested == key:
            print(f"Calories: {value}")
        else:
            break

main()
```

- `input("Item: ").lower()` reads the user's input and converts it to lowercase, so the comparison against the dictionary's (lowercase) keys is case-insensitive.
- `fruits.items()` yields each `(key, value)` pair in the dictionary, letting the loop check both the fruit name and its calorie count together.
- If the requested fruit matches the current key, its calorie count is printed.

#### Behavior Note
Because the loop uses `break` inside an `else` branch, it stops checking as soon as the *first* non-matching key is encountered — so a match only prints correctly if the requested fruit happens to be the very first key in the dictionary, or if it matches on the first comparison. A more robust version would use `continue` (to keep checking remaining keys) or simply do a direct dictionary lookup: `fruits.get(fruit_requested)`.

#### Key Takeaway
Dictionaries are well-suited to "look something up by name" problems like this one, since each fruit name maps directly to its calorie value without needing to search through a list.

#### Example Output

Input `apple` (the first key in the dictionary) works correctly:
```
Item: apple
Calories: 130
```
But input `banana` prints nothing at all after `Item: ` — this confirms the behavior described above: the loop hits `"apple"` first, `"banana"` != `"apple"`, and the `else: break` exits before ever checking the actual `"banana"` key.
```
Item: banana
```

## Comprehensions

### camel.py


#### Problem
Prompt the user for a variable name written in **camelCase** and convert it to **snake_case**, assuming the input is valid camelCase.

#### Core Insight
The file's comments highlight the key problem-solving idea behind the whole script:

> When I see an uppercase letter, replace it with `"_" + lowercase version`.

Rather than asking "what's the code?", the more useful question is "what should happen to *one character at a time*?" — programming is often about solving a tiny, repeatable sub-problem.

#### Final Implementation (for loop)

```python
def main():
    camel = input("camelCase: ")

    snake = ""

    for letter in camel:
        if letter.isupper():
            snake += "_" + letter.lower()
        else:
            snake += letter

    print("snake_case:", snake)


main()
```

- `snake` starts as an empty string (the accumulator).
- For each `letter` in the input:
  - If it's uppercase (`letter.isupper()`), append an underscore plus its lowercase form.
  - Otherwise, append the letter unchanged.
- The result is printed as `snake_case: <converted string>`.

#### Alternative Implementations (commented out in the file)

**1. Using a list + `join` (decomposed version of the list comprehension):**
```python
def main():
    camel = input("camelCase: ")
    snake = []

    for letter in camel:
        if letter.isupper():
            snake.append("_")
            snake.append(letter.lower())
        else:
            snake.append(letter)

    print("snake_case:", "".join(snake))
```
This avoids repeated string concatenation (which creates a new string object each time) by building a list of pieces and joining them once at the end.

**2. List comprehension (most compact form):**
```python
def main():
    camel = input("camelCase: ")

    snake = "".join(
        ["_" + letter.lower() if letter.isupper() else letter for letter in camel]
    )

    print("snake_case:", snake)
```
This condenses the same logic (check each letter, transform it, join the results) into a single expression.

#### Key Takeaway
All three versions implement identical logic at different levels of compactness: a manual `for` loop with string concatenation, a `for` loop building a list, and a one-line list comprehension. Choosing between them is a tradeoff between readability and conciseness rather than correctness.

#### Example Output

Input: `preferredFirstName`
```
camelCase: preferredFirstName
snake_case: preferred_first_name
```

### comprehensions.py


#### Overview
This script reads a list of words from a text file, counts how many times each word appears, and saves the resulting word-frequency counts. It's the starting point in a small series of files (`comprehensions.py` → `list_comprehensions.py` → `dictionary_comprehensions.py`) that progressively refine the same word-counting task using comprehensions.

#### Docstring Summary
As stated directly in the file:
> Reads words from a text file, counts the number of occurrences of each word, and saves the resulting word frequencies.
>
> The function:
> 1. Creates an empty dictionary to store word counts.
> 2. Retrieves a list of words from `'address.txt'` using `get_words()`.
> 3. Iterates through the words and counts how many times each word appears.
> 4. Saves the completed word count dictionary using `save_counts()`.

The docstring also flags a known limitation: **this version counts title-case words as separate from their lowercase equivalents** (e.g., `"The"` and `"the"` would be counted as two different words), since no case-normalization step is applied yet.

#### Dependencies

```python
from helpers import get_words, save_counts
```

Two helper functions are imported from a separate `helpers` module:
- `get_words(filename)` — presumably reads a text file and returns a list of its words.
- `save_counts(counts)` — presumably writes the word-count dictionary to an output file (likely a CSV, based on later files in the series).

#### Implementation

```python
def main():
    counts = {}
    words = get_words("address.txt")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)

main()
```

##### How it works
1. `counts = {}` starts with an empty dictionary that will map each unique word to how many times it appears.
2. `words = get_words("address.txt")` retrieves every word from the source file as a list.
3. The loop checks each `word`:
   - If it's already a key in `counts`, its count is incremented.
   - Otherwise, it's added to `counts` with an initial count of 1.
4. `save_counts(counts)` persists the finished dictionary.

#### Key Takeaway
This is the baseline, most explicit version of the word-counting logic — a manually written accumulation loop — that later files in the series (`list_comprehensions.py`, `dictionary_comprehensions.py`) refine using comprehensions and case-normalization to fix the "title case counted separately" issue mentioned in the docstring.

#### Example Output

Using a small sample "address.txt" text:
```
Saved counts: {'Four': 1, 'score': 1, 'and': 2, 'seven': 1, 'years': 1, 'ago': 1, 'our': 1, 'fathers': 1, 'brought': 1, 'forth': 1, 'on': 1, 'this': 1, 'continent': 1, 'a': 1, 'new': 1, 'nation': 1, 'conceived': 1, 'in': 1, 'liberty': 1, 'dedicated': 1, 'to': 1, 'the': 1, 'proposition': 1, 'that': 1, 'all': 1, 'men': 1, 'are': 1, 'created': 1, 'equal': 1}
```
Every word is counted individually, and title-case/lowercase duplicates (e.g. any repeated capitalized word) would be counted separately here — the limitation the docstring mentions.

### list_comprehensions.py


#### Overview
This file refines `comprehensions.py` by fixing the case-sensitivity issue mentioned there (title-case and lowercase versions of the same word being counted separately) using a **list comprehension**, and adds a length filter as well. The bulk of the file is a detailed explanation, in comments, of how list comprehensions work and how to read them.

#### Dependencies

```python
from helpers import get_words, save_counts
```

Same helper functions as `comprehensions.py`: `get_words()` to read words from a file, `save_counts()` to persist the resulting counts.

#### Implementation

```python
def main():

    counts = {}
    words = get_words("address.txt")

    lowercase_words = [word.lower() for word in words if len(word) > 4]

    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        
    save_counts(counts)

main()
```

##### The list comprehension

```python
lowercase_words = [word.lower() for word in words if len(word) > 4]
```

This single line replaces what would otherwise be a multi-line loop. It builds a new list, `lowercase_words`, containing the **lowercased** version of every word from `words` that is **longer than 4 characters**.

##### Equivalent expanded `for` loop
The comments spell out exactly what the comprehension is shorthand for:
```python
lowercase_words = []
for word in words:
    if len(word) > 4:
        lowercase_words.append(word.lower())
```

##### Anatomy of a list comprehension
Per the file's explanation, a list comprehension has three parts:
- **What to put in the new list:** `word.lower()`
- **Where to get the values from:** `for word in words`
- **The condition (filtering):** `if len(word) > 4`

General pattern:
```python
new_list = [do_something(item) for item in collection if condition]
```
which expands to:
```python
new_list = []
for item in collection:
    if condition:
        new_list.append(do_something(item))
```

##### Reading tip
The comments suggest reading list comprehensions "from the middle outward" rather than strictly left-to-right: *"for each word in words, if its length is greater than 4, put `word.lower()` into the new list."*

##### List comprehensions vs. `for` loops
The file notes there's no single hard rule for choosing between them — it comes down to whether performance matters in the specific situation. If not, whichever approach produces the cleanest code is usually the better choice. It also mentions Python's `timeit` library as a tool for measuring and comparing the runtime of different approaches.

#### Key Takeaway
List comprehensions are a compact way of expressing a "build a new list by transforming and/or filtering an existing collection" loop — but they express the exact same logic as a standard `for` loop, just condensed into one line.

#### Example Output

Using the same sample text (words > 4 characters, lowercased):
```
Saved counts: {'score': 1, 'seven': 1, 'years': 1, 'fathers': 1, 'brought': 1, 'forth': 1, 'continent': 1, 'nation': 1, 'conceived': 1, 'liberty': 1, 'dedicated': 1, 'proposition': 1, 'created': 1, 'equal': 1}
```
Shorter words (≤4 characters) like "our", "on", "a", "in", "to", "the", "all" are filtered out, and everything is already lowercased before counting.

### dictionary_comprehensions.py


#### Overview
This file is the final refinement in the word-counting series, combining a **list comprehension** (from `list_comprehensions.py`) with a **dictionary comprehension** to condense the entire program down to just four lines.

#### Dependencies

```python
from helpers import get_words, save_counts
```

#### Implementation

```python
def main():
    words = get_words("address.txt")
    lowercase_words = [word.lower() for word in words if len(word) > 4]
    counts = {word: lowercase_words.count(word) for word in lowercase_words}
    save_counts(counts)

main()
```

##### What changed from `list_comprehensions.py`
The manual accumulation loop —
```python
for word in lowercase_words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
```
— is replaced entirely by a single **dictionary comprehension**:
```python
counts = {word: lowercase_words.count(word) for word in lowercase_words}
```

##### How the dictionary comprehension works
For every `word` in `lowercase_words`, this builds a dictionary entry where:
- the **key** is the word itself, and
- the **value** is `lowercase_words.count(word)` — the result of Python's built-in `.count()` method, which returns how many times that value appears in the list.

Since `.count()` is called once per unique word (even though the loop runs over every occurrence, later duplicate assignments to the same key simply overwrite earlier ones with the same value), the result is a dictionary mapping each word to its total frequency in the list — without ever needing an explicit `if word in counts` check.

#### Key Takeaway
List comprehensions and dictionary comprehensions can be combined in sequence — first filtering/transforming data into a list, then aggregating that list into a dictionary — to express a task that started as an explicit multi-line loop (in `comprehensions.py`) in just two lines of comprehension logic.

#### Example Output

Same sample text, same filtering:
```
Saved counts: {'score': 1, 'seven': 1, 'years': 1, 'fathers': 1, 'brought': 1, 'forth': 1, 'continent': 1, 'nation': 1, 'conceived': 1, 'liberty': 1, 'dedicated': 1, 'proposition': 1, 'created': 1, 'equal': 1}
```
Identical result to `list_comprehensions.py` — same logic, expressed with a dictionary comprehension instead of a manual accumulation loop.

## Strings

### shows.py


#### Overview
This script demonstrates Python **string methods** — functions that belong to string objects — used here to clean up a messy list of TV show titles (inconsistent leading/trailing spaces and capitalization) and print them as a single, neatly formatted line.

#### Data

```python
SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family"
]
```

The list mixes extra leading spaces and inconsistent capitalization across entries — the exact kind of "messy input" string methods are useful for cleaning up.

#### Implementation

```python
def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print(', '.join(cleaned_shows))

main()
```

##### String methods used
- **`.strip()`** — removes leading and trailing whitespace from a string (fixes entries like `" Avatar: the last airbender"`).
- **`.title()`** — capitalizes the first letter of every word in the string (fixes entries like `"Phineas and ferb"` → `"Phineas And Ferb"`).
- **Method chaining** — `.strip().title()` runs both operations in sequence on the same string, first trimming whitespace, then applying title case to the trimmed result.
- **`', '.join(cleaned_shows)`** — combines all the cleaned strings in the list into one single string, separated by `", "`.

##### Other methods explored (commented out)
- **`.capitalize()`** — capitalizes only the very first character of the *entire* string, leaving the rest as-is (contrasted with `.title()`, which capitalizes every word).

##### Resulting Output
```
Avatar: The Last Airbender, Ben 10, Arthur, Spongebob Squarepants, Phineas And Ferb, Kim Possible, Jimmy Neutron, The Proud Family
```

#### Key Takeaway
String methods can be **chained** together to apply multiple transformations in one expression, which is a concise way to clean up inconsistently formatted text data.

#### Example Output

```
Avatar: The Last Airbender, Ben 10, Arthur, Spongebob Squarepants, Phineas And Ferb, Kim Possible, Jimmy Neutron, The Proud Family
```

### phone.py


#### Overview
This script demonstrates Python **string slicing**, including a common pitfall (assuming digits are always at fixed positions) and its fix using negative indices.

#### Implementation

```python
def main():
    phone = "617-495-1000"
    print(phone[0:3])   # first 3 characters (area code)
    print(phone[:3])    # same as above; start index can be omitted, defaults to 0
    print(phone[8:12])  # last 4 digits, by fixed position
    print(phone[8:])    # same as above; end index can be omitted, defaults to end of string

    print(phone[-4:])   # last 4 digits, using negative indexing


main()
```

##### Slicing rules demonstrated
- `phone[start:end]` — the `start` index is **inclusive**, the `end` index is **exclusive**. So `phone[0:3]` returns characters at positions 0, 1, and 2 (the first three characters).
- Omitting the start index (`phone[:3]`) tells Python to begin from index 0 automatically.
- Omitting the end index (`phone[8:]`) tells Python to continue to the end of the string automatically.

##### Why fixed positions can break
Using `phone[8:12]` to grab "the last 4 digits" only works because this particular phone number string has a known, fixed length and format. If the input format changed — for example, adding a country code like `"+1-617-495-1000"` — the characters at index 8 through 12 would no longer correspond to the last four digits; the slice would grab the wrong substring entirely (e.g., landing on `"95-1000"` in that example, per the file's comment).

##### The fix: negative indexing
```python
print(phone[-4:])
```
Negative indices count from the *end* of the string backward (`-1` is the last character, `-4` is four characters from the end). Slicing this way always returns the last 4 characters regardless of how long the rest of the string is, making it robust to formatting changes at the front of the string.

#### Key Takeaway
When the part of a string you need is always at the *end*, slice using negative indices rather than hardcoded positive positions — it keeps the code correct even if content is added earlier in the string.

#### Example Output

```
617
617
1000
1000
1000
```

### twttr.py


#### Problem
Prompt the user for a string of text and output that same text with all vowels (A, E, I, O, U) removed, regardless of whether they were entered in uppercase or lowercase — mimicking how Twitter's early branding dropped vowels from its name.

#### Implementation

```python
def main():

    word = input("Input: ")
    vowels = ["a", "e", "i", "o", "u"]
    new_word = ""

    for letter in word:
        if letter not in vowels:
            new_word = new_word + letter.lower()
        else:
            continue 

    print(new_word)


main()
```

##### How it works
- `vowels` is a list of the five lowercase vowels used as the exclusion set.
- `new_word` starts as an empty string (the accumulator for the result).
- The loop checks each `letter` in the input: `letter not in vowels` evaluates to `True` when the value is *absent* from the list, which is how Python expresses "does not contain."
- If the letter isn't a vowel, its lowercase form is appended to `new_word`.
- If it is a vowel, `continue` skips straight to the next letter (functionally the same as doing nothing, since there's no code after the `if/else` inside the loop).

##### Note on case handling
Because `vowels` only contains lowercase letters, and the check is `letter not in vowels` (not `letter.lower() not in vowels`), an uppercase vowel like `"A"` would *not* match anything in `vowels` and would technically pass the `not in` test — but since every kept letter is lowercased when appended, and the vowel check happens on the raw letter, uppercase vowels are only correctly excluded if the comparison itself is case-sensitive-safe. In this implementation, checking `letter not in vowels` against an uppercase vowel (e.g., `"A"`) would actually return `True` (since `"A"` isn't in the lowercase list), meaning uppercase vowels could slip through as consonants would. This is worth double-checking against the assignment's requirement to handle both cases.

#### Key Takeaway
The `not in` operator is a clean way to check whether a value is absent from a collection — but it's case-sensitive, so exclusion lists built from lowercase values need the letter being tested to also be lowercased *before* the comparison, not just when appending it to the result.

#### Example Output

Input: `Hello World`
```
Input: Hello World
hll wrld
```

### plates.py


#### Problem
Prompt the user for a vanity license plate and print `Valid` or `Invalid` based on a set of formatting rules:

- Must start with at least two letters.
- Must be between 2 and 6 characters (letters or numbers).
- Numbers can only appear at the end (never in the middle), and the first number used cannot be `0`.
- No periods, spaces, or punctuation are allowed.

#### Implementation

```python
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s[0:2].isdigit(): 
        return False
    
    if len(s) < 2 or len(s) > 6:
        return False
    
    if not s.isalnum():
        return False

    if not s[:2].isalpha():
        return False

    for character in s:
        if s[0:5] == "0":
            return False


main()
```

##### `main()`
Reads the plate string, delegates the validation logic to `is_valid(plate)`, and prints `Valid` or `Invalid` based on the (truthy/falsy) result.

##### `is_valid(s)` — rule-by-rule breakdown
- **`s[0:2].isdigit()`** — checks whether the first two characters are digits; if so, the plate is immediately rejected (this is a partial check toward "must start with letters").
- **`len(s) < 2 or len(s) > 6`** — enforces the character-count rule (2 to 6 characters).
- **`not s.isalnum()`** — rejects any plate containing punctuation, spaces, or periods, since `.isalnum()` only returns `True` for strings made entirely of letters and/or numbers.
- **`not s[:2].isalpha()`** — enforces that the first two characters specifically must be letters (a more direct check than the digit check above).
- **The final `for` loop** — intended to catch the rule that a plate can't start its numeric portion with `0`, but as written it only checks whether the first five characters, as a whole, equal the string `"0"` — which can never be true for a 5-character comparison against a 1-character string. This part of the validation doesn't actually run as intended and the function has no final `return True` for a plate that passes all the earlier checks (meaning a fully valid plate would return `None`, which is falsy, rather than `True`).

#### Key Takeaway
The individual rules are broken into separate `if` conditions inside one validating function — a common pattern for multi-rule validation — though this version highlights how easy it is for a rule (here, "no interior numbers" and "first number can't be 0") to be implemented in a way that doesn't actually enforce it, and for a function to be missing an explicit `return True` at the end.

#### Example Output

Input `AAA222` — per the stated rules this *should* print `Valid`, but running the code prints `Invalid` instead:
```
Plate: AAA222
Invalid
```
This confirms the bug noted above: the function never reaches an explicit `return True` for a passing plate, so it implicitly returns `None`, which `if is_valid(plate):` treats as falsy.

## Tuples

### location.py


#### Overview
This script demonstrates Python **tuples** and compares their memory footprint against an equivalent **list**, illustrating why tuples are preferred for fixed, unchanging data.

#### Implementation

```python
import sys

def main():
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")


main()
```

- `coordinate_tuple` stores the same two values as `coordinate_list`, but using parentheses (`()`) instead of square brackets (`[]`) — the syntax that defines a tuple rather than a list.
- `sys.getsizeof(...)` returns the number of bytes an object occupies in memory, letting the script directly compare tuple size vs. list size for identical data.

#### Why Tuples?
The file's comments explain the reasoning:

- **Tuples are immutable** — once created, their contents cannot be changed. Lists, by contrast, are mutable.
- When you're certain a collection of data won't need to change (like a fixed pair of coordinates), a tuple is a more efficient way to represent it.
- Tuples generally **take up less space in memory** than an equivalent list, which `sys.getsizeof()` demonstrates directly.

#### Additional Concepts Shown (commented out)

- **Basic tuple creation and indexing:**
  ```python
  coordinates = (42.376, -71.115)
  print(f"Latitude: {coordinates[0]}")
  print(f"Longitude: {coordinates[1]}")
  ```
- **Tuple unpacking** — assigning each element of a tuple to its own named variable in one line:
  ```python
  latitude, longitude = coordinates
  print(f"Latitude: {latitude}")
  print(f"Longitude: {longitude}")
  ```

#### Key Takeaway
Use a tuple instead of a list when the collection of values is fixed and shouldn't change after creation — it communicates intent (immutability) and is more memory-efficient.

#### Example Output

```
56 bytes
72 bytes
```
(Confirms the tuple takes up less memory than the equivalent list.)