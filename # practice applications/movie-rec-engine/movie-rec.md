# 🎬 Movie Recommendation Engine — Python Project

A small Python project designed to practice problem-solving, program design, CSV files, loops, dictionaries, functions, conditionals, and exception handling.

The important part of this project is **designing the program yourself**.

You are given the requirements, dataset, testing inputs, and expected behavior.

**You decide:**

* What functions are needed
* What each function should do
* What parameters each function needs
* What each function should return
* How the data should flow through the program
* How to calculate the recommendation score
* How to handle errors

---

# 1. Project Goal

Build a Python program that reads a movie dataset from a CSV file and recommends movies to a user based on their preferences.

The user should be able to enter preferences such as:

* Genre
* Minimum rating
* Minimum release year

The program should examine the movies in the CSV file, calculate how well each movie matches the user's preferences, and recommend the best matches.

---

# 2. What You Are Practicing

This project should give you practice with:

* Variables
* Strings
* Integers
* Floats
* Lists
* Dictionaries
* `for` loops
* `while` loops
* `if` / `elif` / `else`
* Boolean expressions
* Comparison operators
* Functions
* Return values
* `.lower()`
* `.strip()`
* `try` / `except`
* `csv`
* Reading files
* Working with datasets
* Counters
* Accumulators
* Finding maximum values
* Sorting
* Program decomposition
* Input validation

---

# 3. Dataset

Create a file called:

```text
movies.csv
```

Put the following data inside it:

```csv
title,genre,year,rating
Inception,sci-fi,2010,8.8
The Dark Knight,action,2008,9.0
Interstellar,sci-fi,2014,8.7
The Hangover,comedy,2009,7.7
The Matrix,sci-fi,1999,8.7
John Wick,action,2014,7.4
Toy Story,animation,1995,8.3
Finding Nemo,animation,2003,8.2
Superbad,comedy,2007,7.6
Gladiator,action,2000,8.5
```

Your Python program should read this file.

**Do not put the movie data directly inside your Python program.**

---

# 4. User Input

The program should ask the user for:

```text
Genre:
Minimum rating:
Minimum year:
```

Example:

```text
Genre: sci-fi
Minimum rating: 8
Minimum year: 2000
```

---

# 5. Recommendation Scoring

Each movie receives points based on how well it matches the user's preferences.

### Genre Match

If the movie's genre matches the user's chosen genre:

```text
+3 points
```

### Rating

If the movie's rating is greater than or equal to the user's minimum rating:

```text
+2 points
```

### Release Year

If the movie's release year is greater than or equal to the user's minimum year:

```text
+1 point
```

Therefore, a movie can receive a maximum score of:

```text
6 points
```

---

# 6. Example

Suppose the user enters:

```text
Genre: sci-fi
Minimum rating: 8
Minimum year: 2000
```

For:

```text
Inception
```

the program should determine:

```text
Genre matches       → +3
Rating >= 8         → +2
Year >= 2000        → +1
```

Total:

```text
6
```

For:

```text
The Matrix
```

the program should determine:

```text
Genre matches       → +3
Rating >= 8         → +2
Year >= 2000        →  0
```

Total:

```text
5
```

---

# 7. Expected Behavior

The program should examine **every movie in the CSV file**.

It should calculate a score for each movie.

It should then identify the movies with the strongest recommendations.

The final output should contain information such as:

```text
Recommendations:

Inception
Genre: sci-fi
Year: 2010
Rating: 8.8
Score: 6

Interstellar
Genre: sci-fi
Year: 2014
Rating: 8.7
Score: 6

The Matrix
Genre: sci-fi
Year: 1999
Rating: 8.7
Score: 5
```

You decide the exact formatting.

---

# 8. Testing Input #1

Use:

```text
Genre: sci-fi
Minimum rating: 8
Minimum year: 2000
```

You should get:

```text
Inception → 6
Interstellar → 6
The Matrix → 5
```

---

# 9. Testing Input #2

Use:

```text
Genre: action
Minimum rating: 8
Minimum year: 2000
```

You should get:

```text
The Dark Knight → 6
Gladiator → 6
John Wick → 3
```

---

# 10. Testing Input #3

Use:

```text
Genre: comedy
Minimum rating: 7
Minimum year: 2000
```

You should get:

```text
The Hangover → 6
Superbad → 6
```

---

# 11. Testing Input #4

Try:

```text
Genre: horror
Minimum rating: 8
Minimum year: 2000
```

There are no horror movies in the dataset.

Your program should handle this without crashing.

Decide what message makes sense.

For example:

```text
No movies matched your preferences.
```

---

# 12. Input Validation

Your program should handle invalid input.

Test:

```text
Minimum rating: hello
```

Test:

```text
Minimum rating: -5
```

Test:

```text
Minimum rating: 15
```

Test:

```text
Minimum year: hello
```

Your program should not crash.

Use exception handling where appropriate.

---

# 13. Case Sensitivity

These should all be treated as the same genre:

```text
sci-fi
SCI-FI
Sci-Fi
ScI-Fi
```

Your program should normalize the user's input appropriately.

---

# 14. CSV Requirement

You must use Python's CSV functionality.

Start by importing:

```python
import csv
```

Your program should open and read:

```text
movies.csv
```

Do not manually create the movie dictionaries inside the Python program.

The CSV should be the source of your movie data.

---

# 15. Program Design Challenge

This is where **you take over**.

Do not create your program by following a predetermined function structure.

Before writing much code, think about:

### What information does the program need?

For example:

```text
Movie data
User preferences
Movie score
Recommendations
```

### What jobs does the program need to perform?

Think about:

```text
Reading data
Getting input
Validating input
Calculating scores
Finding recommendations
Displaying results
```

You decide whether each job deserves its own function.

---

# 16. Design Before Coding

Before you start coding, write down:

```text
1. What does my program need to do?

2. What data does it need?

3. What should happen first?

4. What should happen next?

5. What information needs to move between parts of the program?

6. Which parts should become functions?

7. What should each function receive?

8. What should each function return?
```

Don't worry about getting the design perfect.

Your first design will probably change as you code.

That's normal.

---

# 17. First Milestone

Your first goal is **not** to build the recommendation engine.

Your first goal is simply:

```text
Python program
      ↓
Open movies.csv
      ↓
Read the data
      ↓
Display the movies
```

For example:

```text
Inception
The Dark Knight
Interstellar
The Hangover
...
```

Once that works, move on.

---

# 18. Second Milestone

Get the user's preferences.

For example:

```text
Genre: sci-fi
Minimum rating: 8
Minimum year: 2000
```

Don't worry about recommendations yet.

Just make sure you can correctly obtain and validate the information.

---

# 19. Third Milestone

Loop through the movies.

For each movie, determine whether:

```text
Genre matches?
Rating meets requirement?
Year meets requirement?
```

Then calculate its score.

---

# 20. Fourth Milestone

Determine which movies are the strongest recommendations.

You should think about:

```text
How do I keep track of the best score?

How do I keep track of the movies that achieved it?

What happens if two movies have the same score?

What happens if five movies have the same score?
```

Don't look for a complicated algorithm.

You already know enough Python to solve the basic version.

---

# 21. Fifth Milestone

Improve the output.

Your final program should be pleasant to use.

For example:

```text
========================================
       MOVIE RECOMMENDATION ENGINE
========================================

Genre: sci-fi
Minimum rating: 8
Minimum year: 2000

----------------------------------------
RECOMMENDATIONS
----------------------------------------

1. Inception
   Rating: 8.8
   Year: 2010
   Score: 6

2. Interstellar
   Rating: 8.7
   Year: 2014
   Score: 6
```

The formatting is completely up to you.

---

# 22. Stretch Goals

Once the basic program works, add features one at a time.

## Stretch Goal 1 — Top 3

Instead of displaying every recommendation, display the top 3.

---

## Stretch Goal 2 — Maximum Year

Ask the user for:

```text
Maximum year:
```

The movie must then fall within the selected year range.

---

## Stretch Goal 3 — Director

Add a `director` column to the CSV.

Allow the user to optionally choose a preferred director.

---

## Stretch Goal 4 — More Genres

Expand the CSV with more movies and genres.

---

## Stretch Goal 5 — Better Scoring

Experiment with the weights.

For example:

```text
Genre match      = 5 points
Rating match     = 3 points
Year match       = 1 point
Director match   = 4 points
```

Think about what makes sense for a recommendation system.

---

# 23. Final Challenge

Once everything works, add enough movies to your CSV that manually predicting the recommendations becomes difficult.

Then test your program with different combinations of:

```text
Genre
Rating
Year
```

Your program should be able to process the dataset without you changing the Python code.

That is the point at which you've moved from:

```text
"programming exercise"
```

toward:

```text
"small data-driven application"
```

---

# 24. Rules for This Project

When you're stuck:

### First

Read your own code.

### Second

Use `print()` to inspect your variables.

### Third

Break the problem into a smaller problem.

### Fourth

Look at the Python documentation.

### Fifth

Ask for a hint.

### Avoid

Immediately asking for the complete solution.

The purpose of this project is to make **you** design the solution.

---

# 25. Definition of Done

The project is complete when your program can:

* [ ] Read movies from `movies.csv`
* [ ] Accept user preferences
* [ ] Validate numeric input
* [ ] Handle invalid input without crashing
* [ ] Compare the user's preferences with every movie
* [ ] Calculate a recommendation score
* [ ] Identify the strongest recommendations
* [ ] Handle ties
* [ ] Handle no matching movies
* [ ] Display the recommendations clearly
* [ ] Run without modifying the CSV manually for each search

---

# 🚀 Your Starting Point

Don't write the whole program.

Start with only:

```text
movies.csv
    ↓
Python
    ↓
Read CSV
    ↓
Print the movies
```

Once you've got that working, **you design the next step yourself**.

The important part of this exercise isn't whether you can eventually write the code.

It's whether you can look at the requirements and think:

> "Okay. What pieces do I need to build to make this work?"
