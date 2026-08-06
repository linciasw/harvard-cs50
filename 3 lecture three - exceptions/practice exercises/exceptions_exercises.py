```python
"""
Python Exceptions Practice Exercises

Topics covered:
- Variables
- Input/output
- Conditionals
- Loops
- Functions
- Lists
- Dictionaries
- Nested dictionaries
- try/except
- else
- pass
- break
- Debugging

Complete each exercise one at a time.
"""



# ============================================================
# EXERCISE 1 - SAFE AGE CHECKER
# Difficulty: 1/10
# ============================================================

"""
Task:

Ask the user for their age.

Requirements:
- Convert input into an integer.
- Handle invalid input using try/except.
- Print:
    Child (0-12)
    Teen (13-17)
    Adult (18+)

Example:

Age: cat

Invalid age.


Age: 15

Teen
"""

# TODO: Write your solution here





# ============================================================
# EXERCISE 2 - GUESS THE SECRET NUMBER
# Difficulty: 2/10
# ============================================================

"""
Task:

The secret number is 25.

Keep asking the user to guess until they get it correct.

Requirements:
- Use while True
- Use try/except for invalid numbers
- Use break when the correct answer is entered

Example:

Guess: hello

Please enter a number.

Guess: 18

Too low.

Guess: 25

Correct!
"""

# TODO: Write your solution here





# ============================================================
# EXERCISE 3 - SHOPPING CART TOTAL
# Difficulty: 3/10
# ============================================================

"""
Task:

Ask the user for 5 prices.

Requirements:
- Store prices in a list.
- Handle invalid prices.
- Calculate:
    - Total
    - Average
    - Highest price

Example:

Price 1: 10
Price 2: apple

Invalid price.

Total: 56
Average: 11.2
Highest: 20
"""

# TODO: Write your solution here





# ============================================================
# EXERCISE 4 - COMPANY DIRECTORY
# Difficulty: 4/10
# ============================================================

"""
Given this dictionary:

company = {
    "IT": {
        "manager": "Alice",
        "employees": 12
    },
    "Finance": {
        "manager": "Bob",
        "employees": 8
    },
    "HR": {
        "manager": "Karen",
        "employees": 5
    }
}


Task:

Ask the user for a department.

If it exists:
    Display manager and employees.

If it does not exist:
    Handle the error.

Example:

Department: Finance

Manager: Bob
Employees: 8
"""

company = {
    "IT": {
        "manager": "Alice",
        "employees": 12
    },
    "Finance": {
        "manager": "Bob",
        "employees": 8
    },
    "HR": {
        "manager": "Karen",
        "employees": 5
    }
}


# TODO: Write your solution here





# ============================================================
# EXERCISE 5 - CREATE YOUR OWN GET_INT FUNCTION
# Difficulty: 5/10
# ============================================================

"""
Task:

Create a reusable function:

get_positive_int(prompt)


Requirements:
- Keep asking until the user enters a positive integer.
- Return the value.

Example:

Age: cat

Invalid number.

Age: -5

Must be positive.

Age: 22

You entered 22
"""


def get_positive_int(prompt):

    # TODO: Add your try/except loop here

    pass



# TODO: Call your function here





# ============================================================
# EXERCISE 6 - EMPLOYEE ANALYZER
# Difficulty: 6/10
# ============================================================

"""
Given:

employees = [
    {"name": "Alice", "salary": 5000},
    {"name": "Bob", "salary": 7500},
    {"name": "Karen", "salary": 6200}
]


Task:

Ask the user for a minimum salary.

Display employees who earn at least that amount.

Requirements:
- Handle invalid salary input.
- Loop through the list.
"""

employees = [
    {"name": "Alice", "salary": 5000},
    {"name": "Bob", "salary": 7500},
    {"name": "Karen", "salary": 6200}
]


# TODO: Write your solution here





# ============================================================
# EXERCISE 7 - WEATHER FORECAST ANALYZER
# Difficulty: 7/10
# ============================================================

"""
Task:

Use this data:

response = {
    "city": "Port of Spain",
    "current": {
        "temperature": 31,
        "weather": "Sunny"
    },
    "forecast": [
        {"day": "Monday", "temp": 30},
        {"day": "Tuesday", "temp": 32},
        {"day": "Wednesday", "temp": 29}
    ]
}


Ask the user for a temperature.

Display days hotter than that temperature.

Example:

Enter temperature: 30

Tuesday - 32
"""


response = {
    "city": "Port of Spain",
    "current": {
        "temperature": 31,
        "weather": "Sunny"
    },
    "forecast": [
        {"day": "Monday", "temp": 30},
        {"day": "Tuesday", "temp": 32},
        {"day": "Wednesday", "temp": 29}
    ]
}


# TODO: Write your solution here





# ============================================================
# EXERCISE 8 - MINI ATM
# Difficulty: 8/10
# ============================================================

"""
Create an ATM program.

Starting balance:

balance = 1000


Menu:

1. Deposit
2. Withdraw
3. View Balance
4. Exit


Requirements:

- Use a while loop.
- Use functions.
- Handle invalid input.
- Prevent overdrawing.
"""


balance = 1000


# TODO:
# Create functions:
#
# deposit()
# withdraw()
# view_balance()
#
# Create your menu loop





# ============================================================
# EXERCISE 9 - STUDENT GRADE BOOK
# Difficulty: 9/10
# ============================================================

"""
Create a menu program.

Menu:

1. Add student
2. View students
3. Find highest grade
4. Exit


Requirements:

Store students in a dictionary.

Example:

students = {
    "Alice": 90,
    "Bob": 75
}


Handle invalid grades using exceptions.
"""


students = {}


# TODO: Write your solution here





# ============================================================
# EXERCISE 10 - VACATION EXPENSE TRACKER V2
# Difficulty: 10/10
# ============================================================

"""
Final Challenge

Build a complete expense tracker.


Menu:

1. Create Trip
2. Add Expense
3. View Expenses
4. View Total
5. View Highest Expense
6. View Spending By Category
7. Exit


Each expense should look like:

{
    "category": "Food",
    "amount": 120,
    "description": "Lunch"
}


Requirements:

- Use functions.
- Use lists and dictionaries.
- Validate user input.
- Handle exceptions.
- Use loops.
- Debug using print statements when needed.


Suggested functions:

create_trip()

add_expense()

view_expenses()

calculate_total()

highest_expense()

spending_by_category()

"""


expenses = []


# TODO:
# Build your program here
```
```python
"""
Python Exceptions Practice Exercises

Topics covered:
- Variables
- Input/output
- Conditionals
- Loops
- Functions
- Lists
- Dictionaries
- Nested dictionaries
- try/except
- else
- pass
- break
- Debugging

Complete each exercise one at a time.
"""



# ============================================================
# EXERCISE 1 - SAFE AGE CHECKER
# Difficulty: 1/10
# ============================================================

"""
Task:

Ask the user for their age.

Requirements:
- Convert input into an integer.
- Handle invalid input using try/except.
- Print:
    Child (0-12)
    Teen (13-17)
    Adult (18+)

Example:

Age: cat

Invalid age.


Age: 15

Teen
"""

# TODO: Write your solution here





# ============================================================
# EXERCISE 2 - GUESS THE SECRET NUMBER
# Difficulty: 2/10
# ============================================================

"""
Task:

The secret number is 25.

Keep asking the user to guess until they get it correct.

Requirements:
- Use while True
- Use try/except for invalid numbers
- Use break when the correct answer is entered

Example:

Guess: hello

Please enter a number.

Guess: 18

Too low.

Guess: 25

Correct!
"""

# TODO: Write your solution here





# ============================================================
# EXERCISE 3 - SHOPPING CART TOTAL
# Difficulty: 3/10
# ============================================================

"""
Task:

Ask the user for 5 prices.

Requirements:
- Store prices in a list.
- Handle invalid prices.
- Calculate:
    - Total
    - Average
    - Highest price

Example:

Price 1: 10
Price 2: apple

Invalid price.

Total: 56
Average: 11.2
Highest: 20
"""

# TODO: Write your solution here





# ============================================================
# EXERCISE 4 - COMPANY DIRECTORY
# Difficulty: 4/10
# ============================================================

"""
Given this dictionary:

company = {
    "IT": {
        "manager": "Alice",
        "employees": 12
    },
    "Finance": {
        "manager": "Bob",
        "employees": 8
    },
    "HR": {
        "manager": "Karen",
        "employees": 5
    }
}


Task:

Ask the user for a department.

If it exists:
    Display manager and employees.

If it does not exist:
    Handle the error.

Example:

Department: Finance

Manager: Bob
Employees: 8
"""

company = {
    "IT": {
        "manager": "Alice",
        "employees": 12
    },
    "Finance": {
        "manager": "Bob",
        "employees": 8
    },
    "HR": {
        "manager": "Karen",
        "employees": 5
    }
}


# TODO: Write your solution here





# ============================================================
# EXERCISE 5 - CREATE YOUR OWN GET_INT FUNCTION
# Difficulty: 5/10
# ============================================================

"""
Task:

Create a reusable function:

get_positive_int(prompt)


Requirements:
- Keep asking until the user enters a positive integer.
- Return the value.

Example:

Age: cat

Invalid number.

Age: -5

Must be positive.

Age: 22

You entered 22
"""


def get_positive_int(prompt):

    # TODO: Add your try/except loop here

    pass



# TODO: Call your function here





# ============================================================
# EXERCISE 6 - EMPLOYEE ANALYZER
# Difficulty: 6/10
# ============================================================

"""
Given:

employees = [
    {"name": "Alice", "salary": 5000},
    {"name": "Bob", "salary": 7500},
    {"name": "Karen", "salary": 6200}
]


Task:

Ask the user for a minimum salary.

Display employees who earn at least that amount.

Requirements:
- Handle invalid salary input.
- Loop through the list.
"""

employees = [
    {"name": "Alice", "salary": 5000},
    {"name": "Bob", "salary": 7500},
    {"name": "Karen", "salary": 6200}
]


# TODO: Write your solution here





# ============================================================
# EXERCISE 7 - WEATHER FORECAST ANALYZER
# Difficulty: 7/10
# ============================================================

"""
Task:

Use this data:

response = {
    "city": "Port of Spain",
    "current": {
        "temperature": 31,
        "weather": "Sunny"
    },
    "forecast": [
        {"day": "Monday", "temp": 30},
        {"day": "Tuesday", "temp": 32},
        {"day": "Wednesday", "temp": 29}
    ]
}


Ask the user for a temperature.

Display days hotter than that temperature.

Example:

Enter temperature: 30

Tuesday - 32
"""


response = {
    "city": "Port of Spain",
    "current": {
        "temperature": 31,
        "weather": "Sunny"
    },
    "forecast": [
        {"day": "Monday", "temp": 30},
        {"day": "Tuesday", "temp": 32},
        {"day": "Wednesday", "temp": 29}
    ]
}


# TODO: Write your solution here





# ============================================================
# EXERCISE 8 - MINI ATM
# Difficulty: 8/10
# ============================================================

"""
Create an ATM program.

Starting balance:

balance = 1000


Menu:

1. Deposit
2. Withdraw
3. View Balance
4. Exit


Requirements:

- Use a while loop.
- Use functions.
- Handle invalid input.
- Prevent overdrawing.
"""


balance = 1000


# TODO:
# Create functions:
#
# deposit()
# withdraw()
# view_balance()
#
# Create your menu loop





# ============================================================
# EXERCISE 9 - STUDENT GRADE BOOK
# Difficulty: 9/10
# ============================================================

"""
Create a menu program.

Menu:

1. Add student
2. View students
3. Find highest grade
4. Exit


Requirements:

Store students in a dictionary.

Example:

students = {
    "Alice": 90,
    "Bob": 75
}


Handle invalid grades using exceptions.
"""


students = {}


# TODO: Write your solution here





# ============================================================
# EXERCISE 10 - VACATION EXPENSE TRACKER V2
# Difficulty: 10/10
# ============================================================

"""
Final Challenge

Build a complete expense tracker.


Menu:

1. Create Trip
2. Add Expense
3. View Expenses
4. View Total
5. View Highest Expense
6. View Spending By Category
7. Exit


Each expense should look like:

{
    "category": "Food",
    "amount": 120,
    "description": "Lunch"
}


Requirements:

- Use functions.
- Use lists and dictionaries.
- Validate user input.
- Handle exceptions.
- Use loops.
- Debug using print statements when needed.


Suggested functions:

create_trip()

add_expense()

view_expenses()

calculate_total()

highest_expense()

spending_by_category()

"""


expenses = []


# TODO:
# Build your program here
```
