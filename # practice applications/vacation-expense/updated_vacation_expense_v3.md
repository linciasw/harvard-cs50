# Vacation Expense Tracker

A personal vacation budgeting and expense-tracking application that allows users to plan a trip financially, record expenses as they occur, and analyze their spending afterward.

---

# 1. Project Goal

Build a simple application that answers three questions:

1. **How much can I afford to spend?**
2. **How much have I actually spent?**
3. **Where did my money go?**

The application should work somewhat like a lightweight spreadsheet, while adding automatic calculations and analysis.

---

# 2. Core Features

The application should have three main stages:

```text
PLAN → TRACK → ANALYZE
```

### Plan

Create a budget before the trip.

### Track

Enter, edit, delete, and view expenses during the trip.

### Analyze

Compare the actual spending against the original budget.

---

# 3. Trip Information

The user should be able to create a trip containing:

* Trip name
* Destination
* Start date
* End date
* Number of travelers
* Total trip budget
* Currency

Example:

```text
Trip Name: New York Vacation
Destination: New York
Start Date: 2026-09-17
End Date: 2026-09-25
Travelers: 1
Total Budget: $3,000 USD
```

---

# 4. Budget Planning

Before recording expenses, the user should be able to create a planned budget.

## Budget Categories

Initial categories:

* Flight
* Accommodation
* Food
* Activities
* Transportation
* eSIM / Internet
* Shopping
* Other

The user should be able to assign a budget to each category.

Example:

| Category       |     Budget |
| -------------- | ---------: |
| Flight         |       $500 |
| Accommodation  |       $900 |
| Food           |       $800 |
| Activities     |       $300 |
| Transportation |       $200 |
| eSIM           |        $50 |
| Shopping       |       $150 |
| Other          |       $100 |
| **Total**      | **$3,000** |

---

# 5. Expense Tracking

The user should be able to add individual expenses.

Each expense should contain:

* Expense ID
* Date
* Description
* Category
* Amount
* Currency
* Optional notes

Example:

```text
Expense ID: 001
Date: 2026-09-18
Description: Dinner at restaurant
Category: Food
Amount: $45
Currency: USD
Notes: Dinner after Broadway show
```

---

# 6. Expense Management

The application should support basic CRUD functionality.

## Create

Add a new expense.

## Read

View existing expenses.

## Update

Edit an existing expense.

## Delete

Delete an expense.

The user should be able to view expenses in a table-like format.

Example:

| ID  | Date   | Description | Category       | Amount |
| --- | ------ | ----------- | -------------- | -----: |
| 001 | Sep 18 | Dinner      | Food           |    $45 |
| 002 | Sep 19 | Subway      | Transportation |  $2.90 |
| 003 | Sep 19 | Museum      | Activities     |    $30 |

---

# 7. Expense Filtering

The user should be able to filter expenses by:

* Category
* Date
* Date range
* Amount
* Description

Example:

```text
Show all Food expenses.

Show expenses between September 18 and September 21.

Show expenses greater than $50.
```

---

# 8. Budget vs Actual Spending

The application should compare the original budget with actual spending.

Example:

| Category      | Budget | Actual | Remaining | Status    |
| ------------- | -----: | -----: | --------: | --------- |
| Flight        |   $500 |   $480 |       $20 | Under     |
| Accommodation |   $900 |   $900 |        $0 | On Budget |
| Food          |   $800 |   $925 |     -$125 | Over      |
| Activities    |   $300 |   $250 |       $50 | Under     |

The application should calculate:

```text
Remaining = Budget - Actual
```

---

# 9. Overall Spending Summary

The application should display:

* Total budget
* Total spent
* Remaining budget
* Percentage of budget spent
* Number of expenses
* Average expense

Example:

```text
Total Budget:       $3,000
Total Spent:        $2,455
Remaining:          $545
Budget Used:        81.8%
Number of Expenses: 37
Average Expense:    $66.35
```

---

# 10. Spending Analysis

After expenses have been entered, the application should provide an analysis of spending.

## Category Analysis

Show how much was spent in each category.

Example:

```text
Food             $925
Accommodation    $900
Activities       $250
Transportation   $180
Shopping         $120
Other             $80
```

---

# 11. Budget Performance

Identify categories where spending was:

* Under budget
* On budget
* Over budget

The application should highlight categories that significantly exceed their budget.

Example:

```text
Food
Budget: $800
Actual: $925
Over Budget: $125
```

---

# 12. Spending Percentages

Calculate what percentage of total spending belongs to each category.

Example:

```text
Food:             37.7%
Accommodation:    36.7%
Activities:       10.2%
Transportation:    7.3%
Shopping:          4.9%
Other:             3.2%
```

This should help the user understand where most of their money went.

---

# 13. Daily Spending Analysis

The application should calculate spending by day.

Example:

| Date   | Total Spent |
| ------ | ----------: |
| Sep 18 |        $120 |
| Sep 19 |         $85 |
| Sep 20 |        $210 |
| Sep 21 |         $95 |

The application should identify:

* Highest-spending day
* Lowest-spending day
* Average daily spending

---

# 14. Analysis Insights

The application should eventually generate simple observations based on the data.

Examples:

```text
You spent 15% more on food than your budget.

Food was your largest spending category.

You spent the most money on September 20.

You have $545 remaining from your original budget.
```

Keep these insights simple initially.

---

# 15. Data Model

The application should use a structure similar to:

```python
trip = {
    "name": "",
    "destination": "",
    "start_date": "",
    "end_date": "",
    "travelers": 1,
    "currency": "",
    "total_budget": 0,
    "budget": {},
    "expenses": []
}
```

Budget:

```python
budget = {
    "flight": 0,
    "accommodation": 0,
    "food": 0,
    "activities": 0,
    "transportation": 0,
    "esim": 0,
    "shopping": 0,
    "other": 0
}
```

Expense:

```python
expense = {
    "id": 1,
    "date": "",
    "description": "",
    "category": "",
    "amount": 0,
    "currency": "",
    "notes": ""
}
```

---

# 16. Data Persistence

Expenses and trip information should not disappear when the application closes.

The first version should use a simple local storage solution.

Possible options:

1. JSON
2. CSV
3. SQLite

### Recommended progression

Start with:

```text
Python dictionaries/lists
        ↓
JSON
        ↓
SQLite
        ↓
Web application database
```

SQLite should eventually become the preferred solution once the application becomes more sophisticated.

---

# 17. User Interface Progression

The project should be developed progressively.

## Version 1 — Command Line

Create the core functionality using Python.

Features:

* Create trip
* Set budget
* Add expense
* View expenses
* Edit expense
* Delete expense
* Calculate totals
* Compare budget vs actual

---

## Version 2 — Persistent Data

Add JSON or SQLite storage.

The application should retain information after closing.

---

## Version 3 — Streamlit Web App

Convert the application into a web application.

Suggested pages:

```text
Dashboard
Budget
Expenses
Analysis
Settings
```

---

# 18. Dashboard

The dashboard should provide a quick overview.

Example:

```text
NEW YORK VACATION

Budget
$3,000

Spent
$2,455

Remaining
$545

Budget Used
81.8%

----------------------------

Top Spending Categories

Food             $925
Accommodation    $900
Activities       $250

----------------------------

Recent Expenses

Dinner            $45
Museum            $30
Subway             $2.90
```

---

# 19. Expenses Page

The expenses page should behave somewhat like a simple spreadsheet.

Users should be able to:

* View all expenses
* Add expenses
* Edit expenses
* Delete expenses
* Sort expenses
* Filter expenses
* Search expenses

---

# 20. Budget Page

The budget page should allow users to:

* Set the total budget
* Set category budgets
* Edit category budgets
* See allocated vs unallocated money
* Compare budget allocations

The application should warn the user if category budgets exceed the total trip budget.

---

# 21. Analysis Page

The analysis page should contain:

* Total spending
* Category breakdown
* Budget vs actual
* Spending percentages
* Daily spending
* Highest spending category
* Highest spending day
* Budget overruns

Charts can eventually be added using Python visualization libraries.

Possible charts:

* Spending by category
* Budget vs actual
* Spending over time
* Daily spending

---

# 22. Validation

The application should validate user input.

Examples:

### Amount

Must be a valid positive number.

```text
$50       ✓
50.25     ✓
-20       ✗
hello     ✗
```

### Category

Must be one of the available categories.

### Date

Must be a valid date.

### Budget

Cannot be negative.

### Required fields

Trip name, destination, dates, and expense amount should not be empty.

---

# 23. Error Handling

The application should gracefully handle invalid input.

Examples:

```python
try:
    amount = float(input("Amount: "))
except ValueError:
    print("Please enter a valid number.")
```

The user should not have to restart the application because of an invalid input.

---

# 24. Future Features

These should NOT be part of the first version.

Potential future improvements:

* Multiple trips
* Multiple currencies
* Currency conversion
* Receipt uploads
* Receipt image/OCR processing
* Authentication
* Cloud database
* User accounts
* Export to CSV
* Export to Excel
* PDF reports
* Interactive charts
* Mobile-friendly interface
* Shared trips
* Multiple travelers
* Individual spending per traveler
* Automatic exchange-rate retrieval

---

# 25. Project Development Strategy

Build the project in layers rather than trying to create the complete application immediately.

### Phase 1 — Core Python

```text
Trip
Budget
Expenses
CRUD
Calculations
```

### Phase 2 — Data Persistence

```text
JSON
or
SQLite
```

### Phase 3 — Analysis

```text
Category totals
Budget vs actual
Daily spending
Percentages
Insights
```

### Phase 4 — Web Interface

```text
Streamlit
Dashboard
Budget
Expenses
Analysis
```

### Phase 5 — Advanced Features

```text
Charts
Exports
Multiple trips
Currency conversion
Receipt processing
```

---

# 26. Success Criteria

The project is successful when a user can:

1. Create a vacation.
2. Set an overall budget.
3. Allocate the budget across categories.
4. Add expenses.
5. View all expenses.
6. Edit expenses.
7. Delete expenses.
8. Filter expenses.
9. Automatically calculate total spending.
10. See how much of the budget remains.
11. Compare budget vs actual spending.
12. Identify categories that went over budget.
13. Analyze spending by category.
14. Analyze spending by day.
15. Close and reopen the application without losing their data.

---

# 27. Core Concept

The application should ultimately feel like:

```text
             VACATION EXPENSE TRACKER
                       │
          ┌────────────┴────────────┐
          │                         │
        PLAN                      TRACK
          │                         │
      Set Budget              Add Expenses
          │                         │
          └────────────┬────────────┘
                       │
                    ANALYZE
                       │
          ┌────────────┼────────────┐
          │            │            │
       Budget       Categories     Daily
       vs Actual     Spending     Spending
          │            │            │
          └────────────┼────────────┘
                       │
                   INSIGHTS
```

The main purpose is not simply to record expenses. It is to let the user **plan their money, track what actually happened, and understand the difference afterward**.
