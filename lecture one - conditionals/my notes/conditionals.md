# Lecture One — Conditionals

## 1. What Is a Conditional Test?

At the heart of every `if` statement is an expression that evaluates to either `True` or `False` — a **conditional test**. Python runs the code under the `if` when the test is `True`, and skips it when the test is `False`.

```python
age = 18

if age >= 18:
    print("You can vote.")
```

**Example output:**
```
You can vote.
```

---

## 2. Comparison Operators

Conditionals are the forks in the road of your program's logic.

| Operator | Meaning |
|---|---|
| `>` | greater than |
| `>=` | greater than or equal to |
| `<` | less than |
| `<=` | less than or equal to |
| `==` | equal to |
| `!=` | not equal to |

### `=` vs `==`
- `car = "audi"` → **assignment**: "set `car` equal to `audi`"
- `car == "bmw"` → **comparison**: "is `car` equal to `bmw`?"

```python
car = "Audi"
print(car == "audi")   # case-sensitive comparison
print(car.lower() == "audi")
print(car)              # original variable is unaffected
```

**Example output:**
```
False
True
Audi
```

`.lower()` returns a *new* string — it doesn't modify the original variable because strings are immutable.

---

## 3. The `if` / `elif` / `else` Family

### 3.1 Plain `if` (checks every condition, regardless of earlier matches)

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
```

**Example output** (x = 3, y = 7):
```
What's x? 3
What's y? 7
x is less than y
```

### 3.2 `if` / `elif` (stops at the first true branch)

```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
```

### 3.3 `if` / `elif` / `else` (most efficient — makes the fewest checks)

```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```

`else` is a catch-all for whatever wasn't matched by an earlier `if`/`elif` — which is also why it's efficient (fewer explicit comparisons) but can silently swallow invalid or unexpected input if you're not careful.

### 3.4 Simplifying with `or` / `!=`

```python
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# equivalent, and simpler:
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```

**Habit to build:** always ask — *could this code be simpler? Could I ask fewer questions?*

> **Note:** Indentation is significant in Python — misaligned blocks will raise an `IndentationError` or change your program's logic.

---

## 4. Testing Multiple Conditions vs. `elif` Chains

Use a **chain of `elif`** when outcomes are mutually exclusive (only one should ever fire). Use **separate `if` statements** when more than one condition can be true at the same time and you want to act on *all* of them.

```python
toppings = ["pepperoni", "mushrooms", "olives"]

if "pepperoni" in toppings:
    print("Adding pepperoni")
if "mushrooms" in toppings:
    print("Adding mushrooms")
if "olives" in toppings:
    print("Adding olives")
```

**Example output:**
```
Adding pepperoni
Adding mushrooms
Adding olives
```

If you rewrote this using `elif`, only the *first* matching topping ("pepperoni") would print — the rest would be skipped, since an `elif` chain stops after its first `True` branch.

Omitting the final `else` is fine when there's no meaningful default action to take.

---

## 5. Grade Calculator (Numeric Ranges)

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

**Example output** (score = 87):
```
Score: 87
Grade: B
```

Two earlier (more verbose) versions of the same logic used explicit double-bounded ranges:

```python
if score >= 90 and score <= 100:
    print("Grade: A")
...
```
and the chained-comparison shorthand:
```python
if 90 <= score <= 100:
    print("Grade: A")
...
```
Once conditions are checked top-to-bottom with `elif`, the upper bound is redundant — if you've reached `elif score >= 80`, you already know `score < 90`, since the `>= 90` branch would have caught it first.

---

## 6. String Equality — Hogwarts Houses (`if/elif` vs `match`)

```python
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
```

**Example output** (name = "Ron"):
```
What's your name? Ron
Gryffindor
```

The same logic using Python's `match` statement (structural pattern matching), with `|` to combine multiple matching values in one `case`:

```python
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

**Example output** (name = "Draco"):
```
What's your name? Draco
Slytherin
```

`case _` is the wildcard — Python's equivalent of `else` inside a `match` block.

---

## 7. Parity Check & Function Return Simplification

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

**Example output** (x = 7):
```
What's x? 7
Odd
```

The `%` (modulo) operator returns the *remainder* of division: `4 % 2` asks "how many times does 2 go into 4, and what's left over?" → `2` times, remainder `0`.

**Key simplification pattern:** whenever you see

```python
if condition:
    return True
else:
    return False
```

it can always be reduced to:

```python
return condition
```

since the condition itself already evaluates to `True` or `False`.

---

## 8. Boolean Logic (`and` / `or` / `not`)

Boolean expressions always resolve to `True` or `False`. Python provides three boolean operators:

| Operator | Meaning |
|---|---|
| `and` | both sides must be `True` |
| `or` | at least one side must be `True` |
| `not` | inverts a boolean value |

```python
5 > 3      # True
5 < 3      # False
10 == 10   # True
10 != 10   # False

18 >= 18 and True   # True
False or True       # True
```

---

## 9. String Methods Used in Conditionals

Common string methods you'll pair with conditionals:

`.startswith()` · `.endswith()` · `.lower()` · `.upper()` · `.strip()` · `.replace()` · `.split()` · `.join()` · `.find()`

### Greeting classifier (`.startswith()`)

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

**Example output** (greeting = "hi there"):
```
Greeting: hi there
$20
```

### File extension → MIME type (`.endswith()`)

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

**Example output** (file_name = "photo.PNG"):
```
File name: photo.PNG
image/png
```

---

## 10. String Equality — The Answer to Life, the Universe, and Everything

```python
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
```

**Example output** (answer = "forty two"):
```
What is the Answer to the Great Question of Life, the Universe, and Everything? forty two
Yes
```

---

## 11. Simple Interpreter (`.split()` + `elif`)

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

**Example output** (expression = "6 * 7"):
```
Expression: 6 * 7
42.0
```

---

## 12. Meal Time Converter (numeric ranges + `__name__ == "__main__"`)

```python
def main():
    meal_time = input("What time is it? 24-hour format ")
    convert(meal_time)

def convert(time):
    hour, minutes = time.split(":")
    x = float(hour)
    y = float(minutes)
    z = y / 60  # minutes as a decimal fraction of an hour
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

**Example output** (time = "12:15"):
```
What time is it? 24-hour format 12:15
lunch time
```

`if __name__ == "__main__":` isn't there because `main()` wouldn't otherwise work — it's there to stop `main()` from auto-running whenever this file is *imported* by another script, rather than run directly. In plain terms it asks: *"Am I the file the user started?"* If yes, run `main()`; if no, stay quiet — you're just being imported.

---

## 13. Nested Conditionals — Game Recommender

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

**Example output** (difficulty = "Casual", players = "Multiplayer"):
```
Difficult or Casual? Casual
Multiplayer or Single-player? Multiplayer
You might like Hearts
```

### Flattened version using boolean logic (`and`, `or`, `not`)

The same recommender, rewritten to validate input up front with `not (... or ...)`, then flatten the nested `if`s into a single `elif` chain using `and`:

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
    else:  # only 4 valid combinations remain, so a plain else is safe here
        recommend("Clock")

def recommend(game):
    print("You might like", game)

main()
```

**Example output** (difficulty = "Difficult", players = "xyz"):
```
Difficult or Casual? Difficult
Multiplayer or Single-player? xyz
Enter a valid number of players
```

This version demonstrates that combining `and`/`or`/`not` can flatten nested conditionals into fewer, flatter branches — worth comparing against the nested version above to see the trade-off between readability and conciseness.

---

## 14. Choosing the Right Conditional — Quick Reference

| Statement | Best used when |
|---|---|
| `if` | Only one condition needs checking |
| `if...else` | Exactly two possible outcomes |
| `if...elif...else` | Several mutually exclusive outcomes |
| Multiple `elif` | Many exclusive choices |
| Multiple separate `if` statements | More than one condition may be true at the same time |
| `match` / `case` | Matching one variable against many discrete values |

---

## 15. Common Beginner Mistakes

**Using `=` instead of `==`:**
```python
if age = 18:      # ❌ SyntaxError
if age == 18:     # ✅ correct
```

**Forgetting comparisons are case-sensitive:**
```python
"Audi" == "audi"          # False
car.lower() == "audi"     # True — use this when case shouldn't matter
```

**Using `elif` when every condition should be checked independently** — switch to multiple `if` statements instead.

---

## 16. Key Takeaways

- Conditionals let a program make decisions; every conditional test evaluates to `True` or `False`.
- `=` assigns values; `==` compares them.
- Use `!=` for inequality, and `>`, `<`, `>=`, `<=` for numeric comparisons.
- Combine conditions with `and`, `or`, and `not`.
- String comparisons are case-sensitive — use `.lower()`/`.upper()` to normalize.
- `if` → one condition; `if...else` → two outcomes; `if...elif...else` → several mutually exclusive outcomes.
- Use multiple independent `if` statements when more than one condition can be true at once.
- `match`/`case` is a clean alternative to long `elif` chains for matching one value.
- `if condition: return True else: return False` can always be simplified to `return condition`.
- The `else` block is optional and best reserved for a genuinely meaningful default.

---

## Mini Practice

Try these without looking back at the notes:

1. Ask the user for their age and print whether they are an adult.
2. Compare two numbers and print which is larger.
3. Check whether a username matches `"admin"` regardless of capitalization.
4. Write an `if...elif...else` statement to print a letter grade.
5. Create a pizza topping list and use multiple `if` statements to print each topping that should be added.
6. Rewrite the Hogwarts house sorter using `match`/`case` instead of `if`/`elif`.