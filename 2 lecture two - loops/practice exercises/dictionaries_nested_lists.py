# ==========================================================
# PYTHON PRACTICE EXERCISES
# Lists • Dictionaries • Loops • Functions
# Difficulty: Beginner → Advanced
# ==========================================================

# ==========================================================
# Exercise 1 — Customer List (Beginner)
# Concepts:
# - Loop through a list
# - Access dictionary values
#
# Task:
# Print each customer's name.
# ==========================================================

customers = [
    {"Name": "Sarah", "Age": 25},
    {"Name": "John", "Age": 32},
    {"Name": "Maria", "Age": 28},
]


# CORRECT
# for customer in customers:
#     print(customer["Name"])
    

# Expected Output:
# Sarah
# John
# Maria


# ==========================================================
# Exercise 2 — Calculate Total Sales (Beginner)
# Concepts:
# - Accumulator variable
# - Dictionary values
#
# Task:
# Calculate the total sales amount.
# ==========================================================

sales = [
    {"Product": "Laptop", "Price": 2500},
    {"Product": "Mouse", "Price": 100},
    {"Product": "Keyboard", "Price": 200},
]


# CORRECT
# amount = 0

# for sale in sales:
#     amount = sale["Price"] + amount


# print(amount)

# Expected Output:
# 2800


# ==========================================================
# Exercise 3 — Find Expensive Items (Beginner → Intermediate)
# Concepts:
# - Loops
# - If statements
#
# Task:
# Print the names of all products costing more than $500.
# ==========================================================

products = [
    {"Name": "Laptop", "Price": 2500},
    {"Name": "Mouse", "Price": 100},
    {"Name": "Monitor", "Price": 900},
]


# CORRECT
# for product in products:
#     if product["Price"] > 500:
#         print(product["Name"])

# Expected Output:
# Laptop
# Monitor


# ==========================================================
# Exercise 4 — Count Categories (Intermediate)
# Concepts:
# - Dictionaries
# - Counting
#
# Task:
# Count how many times each category appears.
# ==========================================================

transactions = [
    {"Category": "Food"},
    {"Category": "Transport"},
    {"Category": "Food"},
    {"Category": "Bills"},
    {"Category": "Food"},
]



# CORRECT
# new_dict = {}

# for transaction in transactions:
#     category = transaction["Category"]

#     if transaction["Category"] not in new_dict:
#         new_dict[category] = 1      # new_dict[transaction["Category"]] this line takes the value of transaction["Category"] and makes a new key in new_dict
#     elif transaction["Category"] in new_dict:
#         new_dict[category] = new_dict[category] + 1
#     else:
#         break

# print(new_dict)


# Expected Output:
# {
#     "Food": 3,
#     "Transport": 1,
#     "Bills": 1
# }


# ==========================================================
# Exercise 5 — Student Grade Report (Intermediate)
# Concepts:
# - Loops
# - Dictionaries
# - If statements
#
# Task:
# Create a dictionary showing whether each student passed.
#
# Passing grade = 70
# ==========================================================

students = [
    {"Name": "Alex", "Grade": 80},
    {"Name": "James", "Grade": 65},
    {"Name": "Lisa", "Grade": 90},
]


# CORRECT
# grade = {}

# for student in students:
#     name = student["Name"]
#     score = student["Grade"]

#     if name not in grade and score > 70:
#         grade[name] = "Pass"
#     elif name not in grade and score < 70:
#         grade[name] = "Fail"
#     else:
#         break

# print(grade)


# Expected Output:
# {
#     "Alex": "Pass",
#     "James": "Fail",
#     "Lisa": "Pass"
# }


# ==========================================================
# Exercise 6 — Bank Account Analyzer (Intermediate)
# Concepts:
# - Filtering
# - Accumulators
#
# Task:
# Calculate:
# - Total deposits
# - Total withdrawals
# - Final balance
# ==========================================================

transactions = [
    {"Type": "Deposit", "Amount": 1000},
    {"Type": "Withdrawal", "Amount": 200},
    {"Type": "Deposit", "Amount": 500},
    {"Type": "Withdrawal", "Amount": 100},
]

# Expected Output:
# Deposits: 1500
# Withdrawals: 300
# Balance: 1200


# ==========================================================
# Exercise 7 — Expense Tracker Summary (Intermediate+)
# Concepts:
# - Dictionaries
# - Running totals
#
# Task:
# Create a dictionary showing the total spent
# in each category.
# ==========================================================

expenses = [
    {"Category": "Food", "Amount": 50},
    {"Category": "Travel", "Amount": 200},
    {"Category": "Food", "Amount": 30},
    {"Category": "Bills", "Amount": 500},
]

# Expected Output:
# {
#     "Food": 80,
#     "Travel": 200,
#     "Bills": 500
# }


# ==========================================================
# Exercise 8 — Employee Department Report (Advanced)
# Concepts:
# - Grouping data
# - Counting
#
# Task:
# Count how many employees work in each department.
# ==========================================================

employees = [
    {"Name": "John", "Department": "IT"},
    {"Name": "Sarah", "Department": "HR"},
    {"Name": "Mike", "Department": "IT"},
    {"Name": "Lisa", "Department": "Finance"},
]

# Expected Output:
# {
#     "IT": 2,
#     "HR": 1,
#     "Finance": 1
# }


# ==========================================================
# Exercise 9 — Sales Dashboard Data (Advanced)
# Concepts:
# - Multiple accumulators
# - Dictionaries
#
# Tasks:
# 1. Create a dictionary containing total sales
#    for each region.
# 2. Find the highest-selling region.
# 3. Calculate total company sales.
# ==========================================================

sales = [
    {"Region": "North", "Amount": 500},
    {"Region": "South", "Amount": 700},
    {"Region": "North", "Amount": 300},
    {"Region": "East", "Amount": 900},
]

# Expected Output:
# {
#     "North": 800,
#     "South": 700,
#     "East": 900
# }
#
# Highest-selling region: East
# Total company sales: 2400


# ==========================================================
# Exercise 10 — Mini Expense Analyzer (Challenge)
# Concepts:
# - Functions
# - Lists
# - Dictionaries
# - Loops
#
# Create the following functions:
#
# add_expense()
# view_expenses()
# calculate_total()
# category_summary()
# largest_expense()
#
# Example:
#
# expenses = []
#
# add_expense("Food", 50)
# add_expense("Transport", 20)
# add_expense("Food", 30)
#
# Expected Output:
#
# Total spent: $100
#
# Category Summary
# Food: $80
# Transport: $20
#
# Largest expense:
# Food $50
# ==========================================================