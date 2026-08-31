# Table of Contents

- [Table of Contents](#table-of-contents)
- [Python Reference — Lecture 4: Libraries](#python-reference--lecture-4-libraries)
- [1. The Big Picture: What Is a Library?](#1-the-big-picture-what-is-a-library)
- [2. Module vs Package vs Library](#2-module-vs-package-vs-library)
  - [Module](#module)
  - [Package](#package)
  - [Library](#library)
- [3. Importing Modules](#3-importing-modules)
- [4. Importing Specific Functions](#4-importing-specific-functions)
- [5. Exploring a Library](#5-exploring-a-library)
  - [`dir()`](#dir)
  - [`help()`](#help)
- [6. The `random` Module](#6-the-random-module)
  - [`random.choice()`](#randomchoice)
  - [`random.randint(a, b)`](#randomrandinta-b)
- [7. `random.choice()` vs `random.choices()` vs `random.sample()`](#7-randomchoice-vs-randomchoices-vs-randomsample)
  - [`choice()`](#choice)
  - [`choices()`](#choices)
  - [`sample()`](#sample)
- [8. Weighted Random Choices](#8-weighted-random-choices)
- [9. Random Seeds](#9-random-seeds)
- [10. Shuffling](#10-shuffling)
- [11. Command-Line Arguments](#11-command-line-arguments)
- [12. Why Command-Line Arguments Are Useful](#12-why-command-line-arguments-are-useful)
- [13. `sys.argv` Is Just a List](#13-sysargv-is-just-a-list)
- [14. Validating Command-Line Arguments](#14-validating-command-line-arguments)
- [15. `sys.exit()`](#15-sysexit)
- [16. Slicing](#16-slicing)
- [17. Third-Party Packages](#17-third-party-packages)
- [18. PyPI](#18-pypi)
- [19. `pip`](#19-pip)
- [20. Using My Own Modules](#20-using-my-own-modules)
- [21. `__name__ == "__main__"`](#21-__name__--__main__)
- [22. Packages and `__init__.py`](#22-packages-and-__init__py)
- [23. Importing From a Package](#23-importing-from-a-package)
- [24. APIs](#24-apis)
- [25. HTTP](#25-http)
- [26. GET](#26-get)
- [27. POST](#27-post)
- [28. The `requests` Library](#28-the-requests-library)
- [29. The URL](#29-the-url)
- [30. Query Parameters](#30-query-parameters)
- [31. Headers](#31-headers)
- [32. API Authentication](#32-api-authentication)
- [33. `timeout`](#33-timeout)
- [34. HTTP Status Codes](#34-http-status-codes)
- [35. `response.text`](#35-responsetext)
- [36. `response.json()`](#36-responsejson)
- [37. JSON](#37-json)
- [38. Lists of Dictionaries](#38-lists-of-dictionaries)
- [39. How to Read Nested API Data](#39-how-to-read-nested-api-data)
- [40. API Workflow](#40-api-workflow)
- [41. `raise_for_status()`](#41-raise_for_status)
- [42. API Error Handling](#42-api-error-handling)
- [43. Building My Own API Modules](#43-building-my-own-api-modules)
- [44. List Comprehensions](#44-list-comprehensions)
- [45. PEP 8 and Code Formatting](#45-pep-8-and-code-formatting)
- [46. Formatting Is Not Just Cosmetic](#46-formatting-is-not-just-cosmetic)
- [47. Programming With Multiple Loops](#47-programming-with-multiple-loops)
- [48. The Four Questions for Program Design](#48-the-four-questions-for-program-design)
- [49. `try` / `except` With Type Conversion](#49-try--except-with-type-conversion)
- [50. `continue`](#50-continue)
- [51. `break`](#51-break)
- [52. `else` With `try`](#52-else-with-try)
- [53. `inflect`](#53-inflect)
- [54. `emoji`](#54-emoji)
- [55. `pyfiglet`](#55-pyfiglet)
- [56. APIs + Command-Line Programs](#56-apis--command-line-programs)
- [57. Geocoding](#57-geocoding)
- [58. Building the Weather CLI](#58-building-the-weather-cli)
- [59. API Client Objects](#59-api-client-objects)
- [60. Objects vs Dictionaries](#60-objects-vs-dictionaries)
- [61. The Most Important API Mental Model](#61-the-most-important-api-mental-model)
- [62. My Overall API Mental Model](#62-my-overall-api-mental-model)
- [63. My Complete API Pattern](#63-my-complete-api-pattern)
- [64. The Five API Projects I Planned](#64-the-five-api-projects-i-planned)
- [65. The Professional Skill I'm Actually Learning](#65-the-professional-skill-im-actually-learning)
- [66. What Lecture 4 Added to My Python Ability](#66-what-lecture-4-added-to-my-python-ability)
- [67. The Core Concepts I Should Be Able to Explain](#67-the-core-concepts-i-should-be-able-to-explain)
    - [Python organization](#python-organization)
    - [Standard library](#standard-library)
    - [Randomness](#randomness)
    - [Command line](#command-line)
    - [Third-party packages](#third-party-packages)
    - [HTTP/API](#httpapi)
    - [`requests`](#requests)
    - [Data](#data)
    - [Program design](#program-design)
    - [Code quality](#code-quality)
- [68. Important Patterns to Remember](#68-important-patterns-to-remember)
  - [Import a module](#import-a-module)
  - [Import a specific function](#import-a-specific-function)
  - [Alias an import](#alias-an-import)
  - [Create your own module](#create-your-own-module)
  - [Protect main program execution](#protect-main-program-execution)
  - [Command-line argument](#command-line-argument)
  - [Validate command-line arguments](#validate-command-line-arguments)
  - [Make an API request](#make-an-api-request)
  - [Add parameters](#add-parameters)
  - [Add headers](#add-headers)
  - [Check HTTP errors](#check-http-errors)
  - [Read JSON](#read-json)
  - [Loop through API results](#loop-through-api-results)
  - [Handle API errors](#handle-api-errors)
- [69. The Bigger Programming Lesson](#69-the-bigger-programming-lesson)
- [70. What I Should NOT Try to Memorize](#70-what-i-should-not-try-to-memorize)
- [71. My Most Important Development Habit](#71-my-most-important-development-habit)
- [72. Final Mental Model](#72-final-mental-model)
- [Quick Reference Card](#quick-reference-card)
- [One Sentence to Remember](#one-sentence-to-remember)


# Python Reference — Lecture 4: Libraries

> Personal reference notes based on my CS50 Python Lecture 4 work.
>
> Main idea:
>
> **Libraries let me reuse code instead of constantly reinventing it.**
>
> This lecture expanded my Python skills from writing standalone programs to using code written by Python, other developers, APIs, and myself.

---

# 1. The Big Picture: What Is a Library?

A **library** is reusable code that I can use in my own programs.

Instead of writing everything myself, I can use functionality that already exists.

For example:

```python
import random

number = random.randint(1, 10)
```

I didn't have to write the random-number algorithm myself.

Python already provides it.

The main reason libraries exist is **code reuse**.

If I find myself copying the same code from one project into another, that is a sign that the code could potentially become a reusable module.

---

# 2. Module vs Package vs Library

These concepts are related but not identical.

## Module

A module is generally a Python file containing reusable code.

```text
sayings.py
```

It can contain:

```python
def hello(name):
    print(f"hello, {name}")
```

I can then import it somewhere else:

```python
from sayings import hello

hello("Lincia")
```

## Package

A package is a collection of related modules.

For example:

```text
museum/
    __init__.py
    artists.py
    artwork.py
```

The `museum` folder is a package containing multiple modules.

## Library

A library is a broader collection of reusable functionality.

A library can contain packages and modules.

The important mental model is:

```text
Library
   ↓
Package
   ↓
Module
   ↓
Functions / classes / other reusable code
```

My notes specifically explored this distinction while learning how Python libraries are organized.

---

# 3. Importing Modules

The simplest form is:

```python
import random
```

Then I access functionality through the module:

```python
random.choice(["heads", "tails"])

random.randint(1, 10)

random.shuffle(cards)
```

This is useful because the module name creates a namespace.

For example:

```python
random.choice(...)
```

clearly tells me that `choice()` came from the `random` module.

---

# 4. Importing Specific Functions

Instead of:

```python
import random

random.choice(cards)
```

I can write:

```python
from random import choice

choice(cards)
```

This can make code shorter.

However, there is a namespace risk.

If I later create:

```python
choice = ["apple", "banana"]
```

I have overwritten the imported function.

That can result in errors such as:

```text
TypeError: 'list' object is not callable
```

A safer alternative is an alias:

```python
from random import choice as choose_item
```

Or simply keep the module namespace:

```python
import random

choice = ["apple", "banana"]

random.choice(choice)
```

The important lesson:

> **Namespaces prevent names from unnecessarily colliding.**

I should be careful when importing individual functions because their names enter my current namespace.

---

# 5. Exploring a Library

Python gives me tools for investigating unfamiliar modules.

## `dir()`

```python
import random

print(dir(random))
```

This shows names available inside the module.

For example, I can discover:

```text
choice
randint
randrange
sample
seed
shuffle
```

I don't need to memorize everything.

I can inspect the library.

## `help()`

```python
help(random)
```

This provides documentation about the object/module.

The important professional habit is:

> **When I don't know how something works, investigate the object instead of guessing.**

---

# 6. The `random` Module

The `random` module provides functions for generating pseudo-random values.

## `random.choice()`

Selects one item:

```python
cards = ["jack", "queen", "king"]

card = random.choice(cards)
```

Possible result:

```text
queen
```

---

## `random.randint(a, b)`

Returns a random integer between `a` and `b`, **inclusive**.

```python
number = random.randint(1, 10)
```

Possible results include:

```text
1
2
3
...
10
```

Both endpoints are included.

I used this in:

* the guessing game
* the Little Professor problem
* random card selection exercises

---

# 7. `random.choice()` vs `random.choices()` vs `random.sample()`

These are different.

## `choice()`

Choose one:

```python
random.choice(cards)
```

## `choices()`

Choose multiple items **with replacement**:

```python
random.choices(cards, k=2)
```

With replacement means an item can be selected again.

Example:

```text
["jack", "jack"]
```

is possible.

## `sample()`

Choose multiple items **without replacement**:

```python
random.sample(cards, k=2)
```

An item cannot be selected twice.

Example:

```text
["jack", "queen"]
```

but not:

```text
["jack", "jack"]
```

provided the original collection contains only one `"jack"`.

This distinction is important when modelling real-world randomness such as drawing cards.

---

# 8. Weighted Random Choices

`random.choices()` can accept weights.

```python
random.choices(
    cards,
    weights=[75, 20, 5],
    k=2
)
```

The weights make some choices more likely than others.

The values don't have to literally add to 100, although thinking in percentages can make them easier to understand.

Mental model:

```text
weights = relative probability
```

This becomes useful when modelling situations where outcomes aren't equally likely.

---

# 9. Random Seeds

Randomness creates a problem when debugging.

Suppose my program randomly produces:

```text
["queen", "king"]
```

and then produces something different every time.

That makes debugging difficult.

I can use:

```python
random.seed(0)
```

This initializes the pseudo-random generator deterministically.

The same seed produces the same sequence of pseudo-random results.

```python
random.seed(0)

print(random.choices(cards, k=2))
```

Running the program again with the same seed produces the same result.

This is useful for:

* debugging
* testing
* reproducibility
* experiments
* machine learning

Important idea:

> Random programs can still be made reproducible.

---

# 10. Shuffling

`random.shuffle()` modifies a list in place.

```python
cards = ["jack", "queen", "king"]

random.shuffle(cards)

for card in cards:
    print(card)
```

The original list is changed.

This is an example of an important programming concept:

> Some functions return a new value, while others modify an existing object.

---

# 11. Command-Line Arguments

The `sys` module allows my program to receive information from the command line.

```python
import sys
```

The important object is:

```python
sys.argv
```

`sys.argv` is a **list**.

If I run:

```bash
python name.py Lincia
```

I might get:

```python
["name.py", "Lincia"]
```

Therefore:

```python
sys.argv[0]
```

is the program name.

And:

```python
sys.argv[1]
```

is the first argument supplied by the user.

---

# 12. Why Command-Line Arguments Are Useful

Instead of:

```python
name = input("Name: ")
```

I can run:

```bash
python name.py Lincia
```

This is especially useful for:

* command-line programs
* scripts
* automation
* quickly testing different inputs
* passing configuration to programs

As I become more comfortable programming, command-line arguments can be faster than repeatedly responding to prompts.

---

# 13. `sys.argv` Is Just a List

This is an important connection.

Because:

```python
sys.argv
```

is a list, I can use normal list operations.

For example:

```python
len(sys.argv)
```

tells me how many command-line arguments exist.

I can also use:

```python
for arg in sys.argv:
    print(arg)
```

and slicing:

```python
sys.argv[1:]
```

The slice removes the program name.

For example:

```python
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
```

---

# 14. Validating Command-Line Arguments

If I blindly do:

```python
print(sys.argv[1])
```

and the user doesn't provide an argument, Python can raise:

```text
IndexError
```

I can prevent that.

```python
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
```

I can also check for too many:

```python
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
```

The key lesson is:

> **Validate assumptions before accessing data.**

---

# 15. `sys.exit()`

`sys.exit()` terminates the program.

Example:

```python
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
```

This is better than merely printing:

```python
print("Too few arguments")
```

because printing the message does not automatically stop execution.

Without stopping execution, later code may still attempt:

```python
sys.argv[1]
```

and cause an `IndexError`.

---

# 16. Slicing

I reinforced list slicing:

```python
sys.argv[1:]
```

Meaning:

```text
start at index 1
go to the end
```

General form:

```python
sequence[start:stop]
```

Examples:

```python
numbers[1:]
numbers[:3]
numbers[1:4]
```

Slicing is particularly useful with `sys.argv` because I usually don't want the program name.

---

# 17. Third-Party Packages

Python also has packages created by developers outside the Python standard library.

Examples I encountered:

```text
cowsay
emoji
pyfiglet
inflect
requests
openmeteo_requests
```

These are installed separately.

---

# 18. PyPI

**PyPI = Python Package Index**

It is a major repository for Python packages.

I can find packages and their documentation there.

Examples from my work included packages such as:

```text
requests
cowsay
pyfiglet
emoji
inflect
```

The basic idea is:

```text
PyPI
 ↓
Find package
 ↓
Read documentation
 ↓
Install package
 ↓
Import package
 ↓
Use its functionality
```

---

# 19. `pip`

`pip` is Python's package installer/package manager.

It lets me install third-party packages.

Conceptually:

```bash
pip install package_name
```

For example:

```bash
pip install requests
```

Then:

```python
import requests
```

The important distinction is:

```text
pip → installs packages

import → makes installed functionality available to my program
```

---

# 20. Using My Own Modules

I learned that I don't only have to import code written by other people.

I can create my own reusable module.

Suppose I have:

```text
sayings.py
```

containing:

```python
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")
```

Another program can do:

```python
from sayings import hello

hello("Lincia")
```

This is the beginning of building reusable software rather than putting everything into one enormous Python file.

---

# 21. `__name__ == "__main__"`

This was one of the most important concepts in the lecture.

I can write:

```python
def main():
    hello("world")
    goodbye("world")


if __name__ == "__main__":
    main()
```

The condition:

```python
if __name__ == "__main__":
```

asks:

> "Is this file being run directly?"

If yes, Python executes:

```python
main()
```

If the file is imported by another program, the condition is false.

Therefore, importing the module doesn't automatically execute the whole program.

This allows me to write modules that contain reusable functions without accidentally running their demonstration/program code whenever they are imported.

---

# 22. Packages and `__init__.py`

I created a package structure like:

```text
museum/
    __init__.py
    artists.py
    artwork.py
```

`__init__.py` marks the directory as a Python package in the context of the lesson.

It can contain code, but it can also simply exist.

Then I can import from the package:

```python
from museum.artists import get_artists
```

This gives me a hierarchical organization:

```text
museum
  ↓
artists
  ↓
get_artists()
```

---

# 23. Importing From a Package

For example:

```python
from museum.artists import get_artists
```

means:

```text
from
    museum package

import
    artists module

import
    get_artists function
```

I can then simply call:

```python
get_artists(query="Picasso", limit=3)
```

This makes larger programs easier to organize.

---

# 24. APIs

An **API (Application Programming Interface)** allows programs to communicate with other software/services.

Many APIs are available over the internet.

The basic model is:

```text
My Python program
       |
       | request
       ↓
     Server
       |
       | response
       ↓
My Python program
```

Instead of manually opening a website, my Python program can communicate with a service programmatically.

Examples I worked with:

* iTunes API
* Art Institute of Chicago API
* Open-Meteo API
* CoinCap API

---

# 25. HTTP

APIs commonly communicate using **HTTP**.

HTTP defines how clients and servers communicate.

Some HTTP methods include:

```text
GET
POST
PUT
PATCH
DELETE
```

The `requests` library gives Python convenient methods corresponding to these:

```python
requests.get()
requests.post()
requests.put()
requests.patch()
requests.delete()
```

The key distinction:

```text
HTTP = communication protocol

requests = Python library that makes working with HTTP easier
```

---

# 26. GET

GET is commonly used to retrieve information.

```python
response = requests.get(url)
```

Mental model:

```text
GET = "Give me information."
```

---

# 27. POST

POST is commonly used to send information to a server.

```python
data = {
    "name": "Lincia"
}

response = requests.post(
    url,
    json=data
)
```

Mental model:

```text
POST = "Here is some information."
```

---

# 28. The `requests` Library

The `requests` library allows Python to make HTTP requests.

Basic example:

```python
import requests

response = requests.get(
    "https://api.example.com/data"
)
```

The result is stored in:

```python
response
```

This is a **Response object**.

---

# 29. The URL

The URL identifies where I am sending the request.

```python
url = "https://api.example.com/weather"

response = requests.get(url)
```

Mental model:

```text
URL = Where am I going?
```

---

# 30. Query Parameters

APIs often require information to be included in the URL.

For example:

```text
/weather?city=Port-of-Spain
```

Instead of manually constructing that string, I can use:

```python
params = {
    "city": "Port-of-Spain"
}

response = requests.get(
    url,
    params=params
)
```

`requests` constructs the query string.

Multiple parameters:

```python
params = {
    "city": "Port-of-Spain",
    "units": "metric"
}
```

Mental model:

```text
params = What specifically am I asking for?
```

---

# 31. Headers

Headers contain additional information about an HTTP request.

Example:

```python
headers = {
    "Authorization": "Bearer MY_API_KEY"
}

response = requests.get(
    url,
    headers=headers
)
```

Headers can be used for:

* authentication
* API keys
* authorization tokens
* accepted response formats
* client information

Mental model:

```text
headers = Additional information the server needs
```

---

# 32. API Authentication

Some APIs require authentication.

A common format is:

```python
headers = {
    "Authorization": "Bearer MY_API_KEY"
}
```

The API documentation tells me:

* whether authentication is required
* what type
* where the credential belongs
* whether `Bearer` is required

I should **not guess**.

Read the API documentation.

---

# 33. `timeout`

I can tell `requests` not to wait forever:

```python
response = requests.get(
    url,
    timeout=10
)
```

Mental model:

```text
timeout = How long should I wait?
```

If the server doesn't respond within the permitted time, a timeout-related exception can occur.

---

# 34. HTTP Status Codes

The server responds with a status code.

Important examples:

```text
200 → OK
201 → Created
400 → Bad Request
401 → Unauthorized
403 → Forbidden
404 → Not Found
500 → Internal Server Error
```

I can inspect it:

```python
print(response.status_code)
```

This is one of the first things I should check when debugging an API request.

---

# 35. `response.text`

I can inspect the raw response:

```python
print(response.text)
```

This is useful when debugging because I can see what the server actually sent.

For API work, I learned to investigate the response before blindly assuming what it contains.

---

# 36. `response.json()`

Many APIs return JSON.

I can convert the JSON response into Python data:

```python
data = response.json()
```

I can then work with it using familiar Python structures.

For example:

```python
print(data["city"])
```

This connects API programming directly to the Python concepts I already learned:

```text
JSON
 ↓
Python dictionaries
 ↓
Python lists
 ↓
loops
 ↓
indexing
 ↓
key access
```

---

# 37. JSON

JSON stands for:

**JavaScript Object Notation**

It is a text-based, language-independent format commonly used to exchange data between computers.

Example:

```json
{
    "city": "Port-of-Spain",
    "temperature": 30,
    "condition": "Sunny"
}
```

It looks very similar to a Python dictionary:

```python
{
    "city": "Port-of-Spain",
    "temperature": 30,
    "condition": "Sunny"
}
```

That makes JSON particularly convenient to work with in Python.

---

# 38. Lists of Dictionaries

This was an important data-modeling concept from the iTunes API.

An API response might contain:

```python
{
    "results": [
        {"trackName": "Song 1"},
        {"trackName": "Song 2"},
        {"trackName": "Song 3"}
    ]
}
```

Notice the structure:

```text
dictionary
   ↓
"results"
   ↓
list
   ↓
dictionaries
```

Therefore:

```python
for result in data["results"]:
    print(result["trackName"])
```

Mental model:

```text
data["results"]
        ↓
      LIST
        ↓
  one dictionary
        ↓
result["trackName"]
        ↓
      VALUE
```

This is extremely important because APIs frequently return nested data.

---

# 39. How to Read Nested API Data

When I encounter something complicated like:

```python
data["results"][0]["name"]
```

I should break it down.

Ask:

1. What is `data`?
2. What does `"results"` give me?
3. Is that a list?
4. What does `[0]` give me?
5. Is that a dictionary?
6. What does `"name"` give me?

Instead of seeing:

```python
data["results"][0]["name"]
```

as one scary expression, break it into layers.

---

# 40. API Workflow

The most important API workflow I learned is:

```text
READ DOCUMENTATION
        ↓
UNDERSTAND ENDPOINT
        ↓
IDENTIFY HTTP METHOD
        ↓
IDENTIFY PARAMETERS
        ↓
IDENTIFY AUTHENTICATION
        ↓
MAKE REQUEST
        ↓
CHECK RESPONSE
        ↓
READ JSON
        ↓
UNDERSTAND DATA STRUCTURE
        ↓
EXTRACT DATA
        ↓
USE DATA IN MY PROGRAM
```

This is more important than memorizing `requests` syntax.

---

# 41. `raise_for_status()`

The `requests` library provides:

```python
response.raise_for_status()
```

This raises an HTTP-related exception when the response indicates an unsuccessful HTTP status.

Example:

```python
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.HTTPError:
    print("Couldn't complete request!")
```

This is cleaner than manually checking every possible error status.

I used this in the Art Institute API work.

---

# 42. API Error Handling

Network requests can fail.

Possible causes include:

* server errors
* invalid requests
* authentication problems
* unavailable services
* network problems
* invalid parameters

Therefore API calls should often be protected with error handling.

Example:

```python
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.HTTPError:
    print("Couldn't complete request!")
```

The important concept is:

> **External systems are outside my control, so my program should expect failure.**

---

# 43. Building My Own API Modules

I started separating API functionality into modules.

For example:

```text
museum/
    artists.py
    artwork.py
```

`artists.py` can contain:

```python
def get_artists(query, limit):
    ...
```

`artwork.py` can contain:

```python
def get_artworks(query, limit):
    ...
```

Then another program can simply use:

```python
from museum.artists import get_artists
```

This is a major step toward **separation of concerns**.

The program asking the user for input doesn't necessarily need to know how the API request works.

---

# 44. List Comprehensions

I encountered list comprehensions while processing API results.

Example:

```python
return [artist["title"] for artist in content["data"]]
```

This means:

```text
For each artist in content["data"],
take artist["title"],
and build a new list.
```

Equivalent traditional loop:

```python
artists = []

for artist in content["data"]:
    artists.append(artist["title"])

return artists
```

List comprehensions provide a concise way to transform collections.

---

# 45. PEP 8 and Code Formatting

I also encountered **PEP 8**.

PEP stands for:

**Python Enhancement Proposal**

PEP 8 is the main style guide for Python.

The underlying lesson is that readable code matters.

Poor formatting makes code harder to understand and can make bugs easier to introduce.

I explored tools including:

```text
Black
pylint
pycodestyle
```

For example:

```bash
black students.py
```

can automatically format Python code.

---

# 46. Formatting Is Not Just Cosmetic

Readable code helps me:

* understand my own code
* debug
* maintain programs
* collaborate with other developers
* identify mistakes

Professional programming is not just:

> "Does the program work?"

It is also:

> "Can another programmer understand and maintain this?"

---

# 47. Programming With Multiple Loops

The `game.py` and `professor.py` exercises taught me to recognize when nested/repeated processes require multiple loops.

For example:

```text
PROGRAM
│
├── repeat questions
│
│     └── repeat attempts for current question
│
└── finish
```

This naturally leads to:

```python
for question in range(10):

    while attempts < 3:
        ...
```

The important thing isn't memorizing nested loops.

It's recognizing:

> **What is repeating?**

and:

> **What is repeating inside that repetition?**

---

# 48. The Four Questions for Program Design

One of my strongest notes from this lecture was:

When I receive a programming problem, I should not immediately start writing code.

Ask:

1. **What is the overall task repeating?**
2. **What is happening repeatedly inside that task?**
3. **What causes the inner repetition to stop?**
4. **What causes the outer repetition to stop?**

This helps me identify the appropriate loops before writing them.

---

# 49. `try` / `except` With Type Conversion

I reinforced that type conversion can cause exceptions.

For example:

```python
number = int(input("Number: "))
```

If the user enters:

```text
hello
```

Python cannot convert `"hello"` to an integer.

It raises:

```text
ValueError
```

I can handle it:

```python
try:
    number = int(input("Number: "))
except ValueError:
    continue
```

This became particularly important in:

* the guessing game
* Little Professor
* command-line argument validation

---

# 50. `continue`

Inside a loop:

```python
continue
```

means:

> Stop this iteration and go back to the beginning of the loop.

Example:

```python
while True:
    try:
        number = int(input("Number: "))
    except ValueError:
        continue

    print(number)
```

If conversion fails, the program doesn't continue executing the rest of that iteration.

It asks again.

---

# 51. `break`

`break` terminates the current loop.

Example:

```python
while True:
    answer = input("Answer: ")

    if answer == "correct":
        break
```

This gives me a common pattern:

```python
while True:

    try:
        ...
    except ValueError:
        continue

    if successful:
        break
```

This pattern is extremely useful for input validation.

---

# 52. `else` With `try`

I also used:

```python
try:
    ...
except ValueError:
    continue
else:
    break
```

The `else` runs when the `try` block succeeds without raising the exception.

Mental model:

```text
try
 ↓
Did an exception happen?
 ↓
YES → except
NO  → else
```

This can make loop control clearer.

---

# 53. `inflect`

I used the third-party `inflect` package for the Adieu problem.

Example:

```python
import inflect

p = inflect.engine()
```

Then:

```python
p.join(list_of_names)
```

can produce grammatically appropriate list joining such as:

```text
Liesl
Liesl and Friedrich
Liesl, Friedrich, and Louisa
```

The important lesson is not memorizing `inflect`.

It's recognizing:

> **A library can solve a specialized problem that would otherwise require me to write the logic myself.**

---

# 54. `emoji`

I used the `emoji` package:

```python
import emoji

print(emoji.emojize(input))
```

This demonstrated another fundamental pattern:

```text
install external package
        ↓
import package
        ↓
call package functionality
```

---

# 55. `pyfiglet`

I used:

```python
from pyfiglet import Figlet, FontNotFound
```

This demonstrated that a package can contain:

* classes
* functions
* exceptions

I can import the specific pieces I need.

For example:

```python
figlet = Figlet()
```

Then use methods provided by that class.

I also learned that if I want to catch a package-specific exception, I need access to that exception:

```python
from pyfiglet import Figlet, FontNotFound
```

Then:

```python
except FontNotFound:
    ...
```

---

# 56. APIs + Command-Line Programs

My API work combined several concepts I had already learned.

For example:

```python
import sys
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
```

This combines:

```text
imports
↓
sys.argv
↓
lists
↓
len()
↓
conditionals
↓
exceptions
↓
type conversion
↓
sys.exit()
```

This is important because programming concepts don't exist in isolation.

Real programs combine them.

---

# 57. Geocoding

I built a small program that takes a location name:

```python
location = input("Location: ")
```

and sends it to a geocoding API.

The API returns information such as:

```text
latitude
longitude
```

I then extracted:

```python
for data in content["results"]:
    latitude = data["latitude"]
    longitude = data["longitude"]
```

This taught me an important real-world API pattern:

```text
Human-friendly input
        ↓
API
        ↓
Structured data
        ↓
Extract required values
        ↓
Use those values elsewhere
```

---

# 58. Building the Weather CLI

I started combining APIs into a larger program.

The architecture is approximately:

```text
User enters location
        ↓
Geocoding API
        ↓
Latitude + longitude
        ↓
Weather API
        ↓
Weather data
        ↓
Display results
```

I separated the work into functions:

```python
def get_coordinates():
    ...
```

and:

```python
def get_weather(latitude, longitude):
    ...
```

Then:

```python
def main():
    latitude, longitude = get_coordinates()
    get_weather(latitude, longitude)
```

This is a major step toward **program decomposition**.

Instead of one giant function, I can divide a problem into logical responsibilities.

---

# 59. API Client Objects

The weather project also exposed me to something different from a simple dictionary response.

I used:

```python
openmeteo_requests.Client()
```

to create a client object.

Then:

```python
responses = openmeteo.weather_api(
    url,
    params=params
)
```

The returned value was a list containing specialized response objects.

I investigated these objects using:

```python
type(...)
dir(...)
help(...)
```

This reinforced a very important professional skill:

> **When an object is unfamiliar, inspect its type and available methods instead of guessing.**

---

# 60. Objects vs Dictionaries

Not every API/library gives me a dictionary.

Sometimes I receive an object:

```text
<SomeApiResponse object at ...>
```

In that situation:

```python
print(response)
```

may not tell me much.

I can investigate:

```python
type(response)
dir(response)
help(response)
```

Then I may discover methods such as:

```python
response.Latitude()
response.Longitude()
response.Current()
```

This is an important transition from:

```text
basic Python data structures
```

toward:

```text
objects + classes + external libraries
```

---

# 61. The Most Important API Mental Model

When learning a new API, I should NOT try to memorize everything.

Ask:

```text
1. What is the endpoint?
2. What HTTP method does it require?
3. What parameters are required?
4. Does it require authentication?
5. Where does authentication go?
6. What does the response look like?
7. What status codes can occur?
8. What data structure does the response contain?
9. How do I extract what I need?
```

The API documentation answers these questions.

My job is to translate those requirements into Python.

---

# 62. My Overall API Mental Model

Think of an HTTP request as layers:

```text
REQUEST
│
├── URL
│      Where am I going?
│
├── PARAMS
│      What specifically am I asking for?
│
├── HEADERS
│      What additional information does the server need?
│
└── TIMEOUT
       How long should I wait?
```

Then:

```text
RESPONSE
│
├── STATUS CODE
│      Did the request succeed?
│
├── HEADERS
│      Information about the response
│
└── BODY
       The actual data
```

---

# 63. My Complete API Pattern

A general starting point:

```python
import requests

url = "https://api.example.com/data"

params = {
    "query": "something"
}

headers = {
    "Authorization": "Bearer API_KEY"
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10
)

response.raise_for_status()

data = response.json()

print(data)
```

I don't necessarily need all of these.

The API documentation determines what I need.

---

# 64. The Five API Projects I Planned

I created a progression of API projects:

```text
1. Weather CLI
        ↓
2. Currency Converter
        ↓
3. Movie Search
        ↓
4. Cryptocurrency Tracker
        ↓
5. Stock / Portfolio Tracker
```

Each one increases complexity.

| Project   | Main Skill                         |
| --------- | ---------------------------------- |
| Weather   | `requests` fundamentals            |
| Currency  | Parameters + JSON                  |
| Movies    | API keys + nested JSON             |
| Crypto    | Authentication + multiple requests |
| Portfolio | Combining everything               |

---

# 65. The Professional Skill I'm Actually Learning

The biggest lesson from the API work isn't:

```python
requests.get(...)
```

The bigger skill is:

```text
I don't know how this API works
        ↓
Read documentation
        ↓
Find endpoint
        ↓
Understand parameters
        ↓
Make a small request
        ↓
Inspect response
        ↓
Understand data structure
        ↓
Extract information
        ↓
Build program around it
```

This same process applies beyond APIs.

It applies to:

* Python libraries
* frameworks
* SDKs
* databases
* cloud services
* machine-learning libraries
* web development tools

---

# 66. What Lecture 4 Added to My Python Ability

Before libraries, I was mostly thinking:

```text
Input
 ↓
Process
 ↓
Output
```

Now my mental model is expanding:

```text
User
 ↓
Python program
 ↓
My functions
 ↓
My modules
 ↓
Third-party libraries
 ↓
HTTP requests
 ↓
External APIs
 ↓
JSON / structured data
 ↓
My program
 ↓
Output
```

That's a significant jump in programming ability.

---

# 67. The Core Concepts I Should Be Able to Explain

After this lecture, I should be able to explain:

### Python organization

* module
* package
* library
* `import`
* `from ... import ...`
* namespaces
* `__init__.py`
* `__name__`
* `if __name__ == "__main__"`

### Standard library

* `random`
* `sys`
* `statistics`

### Randomness

* `choice()`
* `choices()`
* `sample()`
* `randint()`
* `shuffle()`
* `seed()`
* weighted choices
* replacement vs no replacement

### Command line

* `sys.argv`
* `len(sys.argv)`
* indexing
* slicing
* validation
* `sys.exit()`

### Third-party packages

* PyPI
* pip
* package installation
* importing classes/functions
* package-specific exceptions

### HTTP/API

* client
* server
* request
* response
* HTTP
* GET
* POST
* URL
* query parameters
* headers
* authentication
* timeout
* status codes

### `requests`

* `requests.get()`
* `requests.post()`
* `response.status_code`
* `response.text`
* `response.json()`
* `response.raise_for_status()`

### Data

* JSON
* dictionaries
* lists
* nested dictionaries
* lists of dictionaries
* extracting values from API responses

### Program design

* decomposition
* multiple functions
* multiple loops
* nested loops
* error handling
* inspecting unfamiliar objects

### Code quality

* PEP 8
* Black
* pylint
* pycodestyle

---

# 68. Important Patterns to Remember

## Import a module

```python
import random
```

## Import a specific function

```python
from random import choice
```

## Alias an import

```python
from random import choice as choose
```

## Create your own module

```python
# helpers.py

def hello(name):
    print(f"Hello {name}")
```

Then:

```python
from helpers import hello
```

## Protect main program execution

```python
if __name__ == "__main__":
    main()
```

## Command-line argument

```python
import sys

name = sys.argv[1]
```

## Validate command-line arguments

```python
if len(sys.argv) < 2:
    sys.exit("Missing argument")
```

## Make an API request

```python
import requests

response = requests.get(url)
```

## Add parameters

```python
response = requests.get(
    url,
    params=params
)
```

## Add headers

```python
response = requests.get(
    url,
    headers=headers
)
```

## Check HTTP errors

```python
response.raise_for_status()
```

## Read JSON

```python
data = response.json()
```

## Loop through API results

```python
for item in data["results"]:
    print(item["name"])
```

## Handle API errors

```python
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.HTTPError:
    print("Request failed")
```

---

# 69. The Bigger Programming Lesson

The biggest shift in my thinking from this lecture is:

> **I don't have to build everything myself.**

I can build software by combining existing pieces.

For example:

```text
Python
 +
standard library
 +
third-party package
 +
my own module
 +
API
 +
my program logic
 =
useful application
```

A professional developer isn't expected to memorize every library.

They need to know:

```text
What problem am I solving?
        ↓
Does something already exist that can help?
        ↓
Where is its documentation?
        ↓
How do I use it correctly?
        ↓
How do I integrate it into my program?
```

---

# 70. What I Should NOT Try to Memorize

I don't need to memorize:

* every function in `random`
* every function in `requests`
* every HTTP status code
* every API endpoint
* every package's API
* every method on every object
* every PyPI package
* every JSON response structure

Instead, I should memorize the **mental models**.

For example:

```text
Need randomness?
→ Look at random documentation.

Need HTTP?
→ Look at requests documentation.

Need an API?
→ Read the API documentation.

Don't know what an object does?
→ type()
→ dir()
→ help()
```

---

# 71. My Most Important Development Habit

When I get stuck:

```text
DON'T GUESS
     ↓
INVESTIGATE
     ↓
READ DOCUMENTATION
     ↓
INSPECT THE OBJECT
     ↓
MAKE A SMALL TEST
     ↓
OBSERVE THE RESULT
     ↓
THEN WRITE THE PROGRAM
```

This is a much more professional way of programming than trying to remember everything.

---

# 72. Final Mental Model

My Python journey through this lecture can be summarized as:

```text
VARIABLES
    ↓
CONDITIONALS
    ↓
LOOPS
    ↓
EXCEPTIONS
    ↓
LIBRARIES
    ↓
MODULES
    ↓
PACKAGES
    ↓
COMMAND-LINE PROGRAMS
    ↓
THIRD-PARTY PACKAGES
    ↓
HTTP
    ↓
APIs
    ↓
JSON
    ↓
EXTERNAL DATA
    ↓
PROGRAM DECOMPOSITION
    ↓
REAL-WORLD APPLICATIONS
```

The important transition is that I'm no longer learning Python merely as a language.

I'm learning how to use Python as a **tool for building systems**.

---

# Quick Reference Card

```python
# MODULE
import random

# SPECIFIC FUNCTION
from random import choice

# RANDOM
random.choice(items)
random.choices(items, k=2)
random.sample(items, k=2)
random.randint(1, 10)
random.shuffle(items)
random.seed(0)

# COMMAND LINE
import sys

sys.argv
sys.argv[0]
sys.argv[1]
sys.argv[1:]
len(sys.argv)

sys.exit("Error")

# OWN MODULE
from helpers import function

# MAIN GUARD
if __name__ == "__main__":
    main()

# HTTP
import requests

response = requests.get(url)

# PARAMETERS
response = requests.get(
    url,
    params=params
)

# HEADERS
response = requests.get(
    url,
    headers=headers
)

# STATUS
response.status_code

# RAW RESPONSE
response.text

# JSON
data = response.json()

# HTTP ERRORS
response.raise_for_status()

# API DATA
for item in data["results"]:
    print(item["name"])

# ERROR HANDLING
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.HTTPError:
    print("Request failed")
```

# One Sentence to Remember

> **Don't memorize the library. Understand the problem, read the documentation, inspect what you receive, and learn how to connect the pieces.**

