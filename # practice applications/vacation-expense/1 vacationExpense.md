# Product: Vacation Expense Tracker (CLI)

## Objective

Create a command-line application that allows a user to plan a vacation budget, record trip expenses, view spending, and track how much money remains from their budget.

---

# Functional Requirements

## 1. Display Menu

The program should repeatedly display:

```text
=== Vacation Expense Tracker ===

1. Create Trip
2. Add Expense
3. View Expenses
4. View Budget Status
5. View Spending by Category
6. Exit
```

The user should be able to choose an option.

---

# 2. Create Trip

The user should be able to create a vacation by entering:

- Destination
- Number of days
- Total budget

Example:

```text
Destination: New York
Trip Length (days): 8
Budget: 3000
```

The program should store the trip details.

Example:

```text
Trip created successfully!

Destination: New York
Duration: 8 days
Budget: $3000
```

---

# 3. Add Expense

The user enters:

- Expense category
- Expense description
- Expense amount

Example:

```text
Category: Food
Description: Dinner at restaurant
Amount: 65
```

The program stores the expense.

Example:

```text
Expense added successfully!
```

---

# 4. View Expenses

The program displays all recorded expenses.

Example:

```text
Trip Expenses:

1. Food - Dinner at restaurant - $65
2. Transport - Subway - $30
3. Activities - Museum ticket - $25
```

---

# 5. View Budget Status

The program calculates:

- Total budget
- Total spent
- Remaining budget

Example:

```text
Vacation Budget:

Budget:
$3000

Spent:
$120

Remaining:
$2880
```

---

# 6. View Spending by Category

The program should calculate spending grouped by category.

Example:

```text
Spending Breakdown:

Food:
$65

Transport:
$30

Activities:
$25
```

---

# 7. Exit

The program ends when the user selects:

```text
6
```

Output:

```text
Thank you for using Vacation Expense Tracker!
```

---

# Rules / Constraints

- The user must create a trip before adding expenses.
- Budget amount must be a number.
- Expense amount must be a number.
- Budget cannot be negative.
- Expense amount cannot be negative.
- The program should continue running until the user exits.
- If the user enters an invalid menu option, show an error message.
- Expense categories should not be empty.
- The program should handle invalid input without crashing.

---

# Suggested Functions

You don't have to use these, but they are good practice:

```python
display_menu()

create_trip()

add_expense()

view_expenses()

calculate_total_spending()

calculate_remaining_budget()

view_category_summary()

validate_amount()
```

---

# Suggested Data Structure

You can store trip information using variables:

```python
destination = ""
days = 0
budget = 0
```

Expenses can be stored using a list:

```python
expenses = [
    {
        "category": "Food",
        "description": "Dinner",
        "amount": 65
    }
]
```

---

# Testing

## Test Case 1: Create Trip

### Input

```text
1
New York
8
3000
```

### Expected Output

```text
Trip created successfully!

Destination: New York
Duration: 8 days
Budget: $3000
```

---

## Test Case 2: Add Expense

### Input

```text
2
Food
Dinner
65
```

### Expected Output

```text
Expense added successfully!
```

---

## Test Case 3: View Expenses

### Starting Data

```text
Food - Dinner - $65
Transport - Subway - $30
```

### Input

```text
3
```

### Expected Output

```text
Trip Expenses:

1. Food - Dinner - $65
2. Transport - Subway - $30
```

---

## Test Case 4: View Budget Status

### Starting Data

```text
Budget:
3000

Expenses:
Food - $65
Transport - $30
```

### Input

```text
4
```

### Expected Output

```text
Vacation Budget:

Budget:
$3000

Spent:
$95

Remaining:
$2905
```

---

## Test Case 5: View Spending by Category

### Starting Data

```text
Food - $65
Transport - $30
Food - $20
```

### Input

```text
5
```

### Expected Output

```text
Spending Breakdown:

Food:
$85

Transport:
$30
```

---

## Test Case 6: Invalid Amount

### Input

```text
2
Food
Dinner
hello
```

### Expected Output

```text
Invalid amount. Please enter a number.
```

---

## Test Case 7: Negative Amount

### Input

```text
2
Food
Dinner
-50
```

### Expected Output

```text
Amount cannot be negative.
```

---

## Test Case 8: Add Expense Before Creating Trip

### Input

```text
2
Food
Dinner
50
```

### Expected Output

```text
Please create a trip before adding expenses.
```