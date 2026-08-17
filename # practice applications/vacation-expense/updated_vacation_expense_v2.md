# Vacation Expense Tracker — Project Specifications

## 1. Project Overview

A personal vacation expense tracker that allows users to create trips, record expenses, manage existing expenses, and review spending.

The application should work like a lightweight spreadsheet/database specifically designed for tracking vacation spending.

### Main Goal

The user should be able to answer:

* How much have I spent?
* What did I spend it on?
* How much did each category cost?
* Am I within my vacation budget?
* What expenses have I recorded?
* Can I edit or delete an expense?
* Can I save my trip and continue working on it later?

---

# 2. Core Features

## Trip Management

The application should allow the user to create a trip containing:

* Trip name
* Destination
* Start date
* End date
* Total budget
* Currency

Example:

```text
Trip: New York Vacation
Destination: New York
Start Date: 2026-09-17
End Date: 2026-09-25
Budget: $2,000 USD
Currency: USD
```

---

# 3. Expense Data

Each expense should contain:

```text
Expense ID
Date
Description
Category
Amount
Currency
Payment Method
Notes
```

Example:

```text
ID: 001
Date: 2026-09-17
Description: Airport Taxi
Category: Transport
Amount: 45.00
Currency: USD
Payment Method: Card
Notes: Airport to accommodation
```

---

# 4. Expense Categories

Initial categories:

```python
categories = [
    "flight",
    "accommodation",
    "food",
    "activities",
    "transport",
    "esim",
    "shopping",
    "other"
]
```

The application should eventually allow users to create custom categories.

---

# 5. Main Menu

The application should present a menu similar to:

```text
================================
       VACATION EXPENSE TRACKER
================================

1. Create New Trip
2. View Trip
3. Add Expense
4. View Expenses
5. Edit Expense
6. Delete Expense
7. View Summary
8. Export Expenses
9. Save Trip
10. Load Trip
11. Exit

Select an option:
```

The menu should continue running until the user chooses `Exit`.

---

# 6. Add Expense

The user should be prompted for:

```text
Date:
Description:
Category:
Amount:
Currency:
Payment Method:
Notes:
```

The application should validate the input.

### Validation

The application should prevent:

* Empty descriptions
* Invalid dates
* Negative expenses
* Non-numeric amounts
* Invalid categories

Example:

```text
Enter expense amount: abc

Invalid amount.
Please enter a number.
```

---

# 7. View Expenses

Display expenses in a table-like format.

Example:

```text
ID   Date        Description       Category      Amount
----------------------------------------------------------
1    09/17/26    Airport Taxi      Transport     $45.00
2    09/17/26    Dinner            Food          $32.50
3    09/18/26    Museum             Activities    $25.00
```

The user should be able to see all expenses recorded for the trip.

---

# 8. Edit Expense

The user should be able to select an expense by its ID.

Example:

```text
Enter Expense ID: 2

Current Expense:
Description: Dinner
Category: Food
Amount: $32.50

What would you like to edit?

1. Date
2. Description
3. Category
4. Amount
5. Payment Method
6. Notes
7. Cancel
```

The application should update only the selected field.

---

# 9. Delete Expense

The user should be able to delete an expense using its ID.

Before deletion:

```text
Are you sure you want to delete this expense?

1. Yes
2. No
```

The application should require confirmation before deleting data.

---

# 10. Expense Summary

The application should calculate:

### Total Spending

```text
Total Spent: $1,245.50
```

### Remaining Budget

```text
Budget:        $2,000.00
Total Spent:   $1,245.50
Remaining:       $754.50
```

### Spending by Category

```text
Food:           $350.00
Transport:      $185.00
Accommodation:  $500.00
Activities:     $160.50
eSIM:            $50.00
```

### Percentage of Budget Used

```text
Budget Used: 62.28%
```

---

# 11. Budget Warnings

The application should warn the user when spending approaches or exceeds the budget.

Example:

```text
WARNING:
You have used 85% of your vacation budget.
```

If the budget is exceeded:

```text
WARNING:
You have exceeded your vacation budget by $125.50.
```

---

# 12. Filtering and Searching

The user should eventually be able to filter expenses by:

* Category
* Date
* Payment method
* Amount range

Example:

```text
Show all Food expenses
Show expenses above $100
Show expenses from September 18
```

This feature can be added after the basic tracker works.

---

# 13. Data Storage

The application should persist data so that expenses are not lost when the program closes.

### Initial Version

Use JSON for saving and loading trips.

Example:

```text
trip.json
```

Possible structure:

```python
trip = {
    "name": "New York Vacation",
    "destination": "New York",
    "start_date": "2026-09-17",
    "end_date": "2026-09-25",
    "budget": 2000,
    "currency": "USD",
    "expenses": [
        {
            "id": 1,
            "date": "2026-09-17",
            "description": "Airport Taxi",
            "category": "transport",
            "amount": 45,
            "currency": "USD",
            "payment_method": "card",
            "notes": "Airport to accommodation"
        }
    ]
}
```

---

# 14. CSV Export

The application should allow the user to export expenses to a CSV file.

Example:

```text
vacation_expenses.csv
```

CSV columns:

```text
ID
Date
Description
Category
Amount
Currency
Payment Method
Notes
```

The CSV can then be opened in:

* Excel
* Google Sheets
* Power BI
* Python/Pandas

This creates an opportunity to use the project later for actual data analysis.

---

# 15. Future Data Analysis

Once enough expenses have been recorded, the exported CSV should allow analysis such as:

### Spending by Category

```text
Food            $450
Accommodation   $800
Transport       $225
Activities      $300
Shopping        $175
```

### Daily Spending

```text
Day 1: $125
Day 2: $210
Day 3: $175
Day 4: $95
```

### Average Daily Spending

```text
Average Daily Spending: $168.75
```

### Largest Expense

```text
Largest Expense:
Hotel — $800
```

### Most Expensive Category

```text
Accommodation
```

These analyses could eventually become charts in a web application.

---

# 16. Recommended Python Structure

Start with a single Python file while learning.

```text
vacation_tracker.py
```

Once the application becomes larger, separate it into modules:

```text
vacation-expense-tracker/
│
├── main.py
├── trip.py
├── expenses.py
├── storage.py
├── analysis.py
├── csv_export.py
│
├── data/
│   └── trips.json
│
└── exports/
    └── vacation_expenses.csv
```

---

# 17. Functions

The project should be broken into functions.

Possible functions:

```python
create_trip()
add_expense()
view_expenses()
edit_expense()
delete_expense()
calculate_total()
calculate_remaining_budget()
calculate_category_totals()
display_summary()
save_trip()
load_trip()
export_csv()
```

The goal is to avoid putting the entire application inside one large `while` loop.

---

# 18. Recommended Development Order

Do not try to build everything at once.

## Version 1 — Basic Tracker

Build:

* Create trip
* Add expense
* View expenses
* Calculate total
* Menu system

Focus on:

* Variables
* Lists
* Dictionaries
* Functions
* Loops
* Conditionals

---

## Version 2 — Data Validation

Add:

* Exception handling
* Numeric validation
* Date validation
* Category validation
* Empty input handling

Focus on:

* `try`
* `except`
* `ValueError`
* `while` loops

---

## Version 3 — Expense Management

Add:

* Expense IDs
* Edit expenses
* Delete expenses
* Confirmation prompts

Focus on manipulating lists of dictionaries.

---

## Version 4 — Persistence

Add:

* JSON saving
* JSON loading
* Multiple trips

Focus on:

```python
import json
```

---

## Version 5 — Analysis

Add:

* Spending by category
* Daily spending
* Remaining budget
* Percentage of budget used
* Largest expense
* Average daily spending

---

## Version 6 — CSV

Add:

```python
import csv
```

Allow users to export their expenses.

---

## Version 7 — Data Analysis

Use:

```python
import pandas as pd
```

Analyze the exported data.

Eventually create charts showing:

* Spending by category
* Spending over time
* Budget vs actual spending
* Daily spending

---

# 19. Future Web Application

The Python CLI version should eventually become a web application.

Possible technology:

```text
Frontend:
HTML
CSS
Bootstrap

Backend:
Python
Streamlit initially

Data:
SQLite

Analysis:
Pandas

Visualization:
Plotly
```

Possible web interface:

```text
------------------------------------------------
 New York Vacation
 Budget: $2,000
 Spent:  $1,245
 Remaining: $755
------------------------------------------------

[ Add Expense ]

Expenses
------------------------------------------------
Date       Description       Category    Amount
09/17      Taxi              Transport   $45
09/17      Dinner            Food        $32
09/18      Museum            Activities  $25
------------------------------------------------

Spending Breakdown
[ Chart ]

Daily Spending
[ Chart ]
```

---

# 20. Long-Term Vision

The project can eventually become a small **Personal Finance Toolkit** rather than remaining only a vacation tracker.

Potential tools:

```text
Personal Finance Toolkit

├── Vacation Expense Tracker
├── Loan Calculator
├── Compound Interest Calculator
├── Budget Tracker
├── Savings Goal Calculator
├── Debt Payoff Calculator
└── Investment Calculator
```

The vacation tracker would therefore become one real application within a larger portfolio project.

---

# 21. Definition of Done — Version 1

Version 1 is complete when the user can:

* [ ] Create a trip
* [ ] Enter a vacation budget
* [ ] Add an expense
* [ ] View all expenses
* [ ] Calculate total spending
* [ ] Calculate remaining budget
* [ ] Use categories
* [ ] Navigate through a menu
* [ ] Exit the program without errors

Do **not** add CSV, Pandas, databases, charts, or a web interface until the basic version works reliably.

The goal of the first version is to practice **program design and data modelling**, not to build the final product immediately.
