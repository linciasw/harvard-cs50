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


new_transactions = {}

for transaction in transactions:
    if transaction["Amount"] not in new_transactions:
        


# CORRECT
# rebuild the entire dictionary and use an accumulator
# you're transforming the data into a new structure that's more useful for your goal.

'''
Think of it like this:
Original (list of records)

[
  {"Type": "Deposit", "Amount": 1000},
  {"Type": "Withdrawal", "Amount": 200},
  {"Type": "Deposit", "Amount": 500},
  {"Type": "Withdrawal", "Amount": 100}
]

           │
           │ loop through each transaction
           ▼

New structure (summary)

{
    "Deposit": 1500,
    "Withdrawal": 300
}
'''

'''
This pattern is one of the most important in programming:

Raw data → Loop → Summary
Raw data → Loop → Filtered data
Raw data → Loop → Different data structure

You'll use it constantly in data analysis, backend development, and machine learning preprocessing.

In fact, many real-world programs follow this exact workflow:

Read raw data (CSV, JSON, database, API).
Loop through each record.
Build one or more new dictionaries/lists that are easier to work with.
Use those new structures to calculate totals, generate reports, create charts, or feed into another system.
This is one of the fundamental patterns behind data processing
'''


# new_dict = {}

# for transaction in transactions:
#     type = transaction["Type"]
#     amount = transaction["Amount"]

#     if type not in new_dict:
#         new_dict[type] = amount
#     else:
#         new_dict[type] = new_dict[type] + amount              # new_dict[type] += amount


# balance = new_dict["Deposit"] - new_dict["Withdrawal"]


# print(f"Deposits: {new_dict["Deposit"]}")
# print(f"Withdrawals: {new_dict["Withdrawal"]}")
# print(f"Balance: {balance}")

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


# CORRECT
# new_dict = {}

# for expense in expenses:
#     category = expense["Category"] 
#     amount = expense["Amount"]

#     if category not in new_dict:
#         new_dict[category] = amount
#     elif category in new_dict:
#         new_dict[category] += amount

# print(new_dict)



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


# CORRECT
# new_dict = {}

# for employee in employees:
#     department = employee["Department"]
#     amount = 1


#     if department not in new_dict:
#         new_dict[department] = amount
#     else:
#         new_dict[department] += amount


# print(new_dict)


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


# new_dict = {}

# for sale in sales:
#     region = sale["Region"]
#     amount = sale["Amount"]
    
#     if region not in new_dict:
#         new_dict[region] = amount
#     else:
#         new_dict[region] += amount

# print(new_dict)



# to find the highest-selling region
# for key, value in new_dict.items():
#     max_value = 0
#     max_key = None

#     if value > max_value:
#         max_value = value
#         max_key = key


# print(f"Highest-selling region: {max_key}")




# # to calculate total sales of all regions
# total_sum = 0

# for total in new_dict.values():
#     total_sum += total

# print(total_sum)




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