# ==========================================================
# PYTHON DATA STRUCTURES PRACTICE
# Real World Exercises
# Difficulty: Beginner → Advanced
# ==========================================================


# ==========================================================
# Exercise 1 - User Profile (Dictionary)
#
# Concepts:
# - Access dictionary values
# - Modify values
#
# Task:
# 1. Print the user's name.
# 2. Increase their age by 1.
# 3. Change the city to "San Fernando".
# 4. Print the updated dictionary.
# ==========================================================

user = {
    "name": "Lincia",
    "age": 35,
    "city": "Chaguanas"
}







# ==========================================================
# Exercise 2 - Shopping Cart (Dictionary with List)
#
# Concepts:
# - Lists inside dictionaries
#
# Task:
# 1. Print every item.
# 2. Count how many items are in the cart.
# 3. Add "Milk".
# 4. Remove "Eggs".
# ==========================================================

cart = {
    "customer": "Sarah",
    "items": ["Bread", "Eggs", "Butter"]
}


# ==========================================================
# Exercise 3 - Employee Skills (Dictionary with List)
#
# Concepts:
# - Membership testing
#
# Task:
# 1. Print every skill.
# 2. Check if "Python" exists.
# 3. Add "Docker".
# 4. Sort the skills alphabetically.
# ==========================================================

employee = {
    "name": "James",
    "skills": ["Excel", "SQL", "Power BI"]
}


# ==========================================================
# Exercise 4 - Course Grades
#
# Concepts:
# - Dictionary iteration
#
# Task:
# 1. Print each subject and grade.
# 2. Find the highest grade.
# 3. Calculate the average.
# ==========================================================

grades = {
    "Math": 82,
    "English": 75,
    "Science": 90,
    "History": 80
}


# ==========================================================
# Exercise 5 - Website Configuration
#
# Concepts:
# - Nested dictionaries
#
# Task:
# 1. Print the host.
# 2. Print the database name.
# 3. Change debug to False.
# 4. Change the database password.
# ==========================================================

config = {
    "host": "localhost",
    "debug": True,
    "database": {
        "name": "bank_app",
        "username": "admin",
        "password": "password123"
    }
}


# ==========================================================
# Exercise 6 - Bank Customer
#
# Concepts:
# - Dictionary
# - List
# - Nested dictionary
#
# Task:
# 1. Print the account holder.
# 2. Print every transaction.
# 3. Calculate the account balance.
# 4. Count deposits.
# 5. Count withdrawals.
# ==========================================================

account = {
    "holder": "Sarah",
    "transactions": [
        {"type": "Deposit", "amount": 1000},
        {"type": "Withdrawal", "amount": 250},
        {"type": "Deposit", "amount": 400}
    ]
}


# ==========================================================
# Exercise 7 - Student Database
#
# Concepts:
# - List of dictionaries inside a dictionary
#
# Task:
# 1. Print every student's name.
# 2. Find the oldest student.
# 3. Calculate the average age.
# ==========================================================

school = {
    "name": "ABC High School",
    "students": [
        {"name": "John", "age": 18},
        {"name": "Sarah", "age": 17},
        {"name": "Mike", "age": 19}
    ]
}


# ==========================================================
# Exercise 8 - Company Departments
#
# Concepts:
# - Nested dictionaries
#
# Task:
# 1. Print every department.
# 2. Print the manager of IT.
# 3. Count employees in each department.
# 4. Find the department with the most employees.
# ==========================================================

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


# ==========================================================
# Exercise 9 - API Response
#
# Concepts:
# - Working with JSON-like data
#
# This is very similar to data you'll receive
# from REST APIs.
#
# Task:
# 1. Print the weather.
# 2. Print the temperature.
# 3. Print each forecast day.
# 4. Find the hottest forecast.
# ==========================================================

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


# ==========================================================
# Exercise 10 - Mini Banking System
#
# Concepts:
# - Everything you've learned
#
# Write functions to:
#
# deposit(amount)
# withdraw(amount)
# show_balance()
# print_transactions()
#
# Store all transactions inside the account
# dictionary.
#
# Bonus:
#
# Reject withdrawals that exceed the balance.
# ==========================================================

account = {
    "holder": "Sarah",
    "balance": 1000,
    "transactions": []
}