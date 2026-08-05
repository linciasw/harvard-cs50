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


# 1
# print(user["name"])

# 2
# user["age"] = user["age"] + 1
# print(user["age"])

# 3
# user["city"] = "San Fernando"

# 4
# print(user)




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

# CORRECT
# print(cart["items"])

# grocery_items = cart["items"]
# amount = 0

# for items in grocery_items:
#     amount += 1
    
# print(amount)


# grocery_items.append("Milk")
# print(cart)

# grocery_items.remove("Eggs")
# print(cart)





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


# CORRECT
# employee = {
#     "name": "James",
#     "skills": ["Excel", "SQL", "Power BI"]
# }

# skills = employee["skills"] 

# 1. Print every skill.
# print(employee["skills"])


# 2. Check if "Python" exists.
# if "Python" in skills:
#     print("Python does exist!")
# else:
#     print("Python does not exist!")


# 3. Add "Docker".
# skills.append("Docker")
# print(skills)


# 4. Sort the skills alphabetically.
# skills.sort()
# print(skills)




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



# 1. Print each subject and grade.
# for subject, grade in grades.items(): 
#     print(f"{subject}: {grade}")



# 2. Find the highest grade.
# max_value = 0

# for grade in grades.values():
#     if grade > max_value:
#         max_value = grade


# print(f"Highest grade: {max_value}")


# 3. Calculate the average 
# amount = 0 

# for key, grade in grades.items():
#     amount += grade           # amount = amount + grade

#     print(amount)

#     average = amount / 4 

# print(f"Average of all grades: {average}")





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



# 1.
#print(config["host"])


# 2. 
# database = config["database"]
# print(database["name"])


# 3.
# config["debug"] = False
# print(config)


# 4.
# database["password"] = "Password!23"
# print(config)




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


# 1. Print the account holder.
# print(account["holder"])


# 2. Print every transaction.
transactions = account["transactions"]

# for transaction in transactions:
#     print(transaction)


# 3. Calculate the account balance.
# total_deposits = 0
# total_withdrawals = 0

# for transaction in transactions:
#     type = transaction["type"]
#     amount = transaction["amount"]

#     if type == "Deposit":
#         total_deposits += amount
#     else:
#         total_withdrawals += amount


# DEBUGGING
# print(total_withdrawals)
# print(total_deposits)

# balance = total_deposits - total_withdrawals
# print(f"Account balance: {balance}")




# 4. Count deposits.
# 5. Count withdrawals.
deposit_amount = 0
withdrawal_amount = 0

for transaction in transactions:
    type = transaction["type"]


    if type == "Deposit":
        deposit_amount += 1
    elif type == "Withdrawal":
        withdrawal_amount += 1
        
print(deposit_amount)
print(withdrawal_amount)



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