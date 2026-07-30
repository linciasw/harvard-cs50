# Product 1: Personal Expense Tracker (CLI)

## Objective

Create a command-line application that allows a user to record expenses, view expenses, and calculate total spending.

---

# Functional Requirements

## 1. Display Menu

The program should repeatedly display:

```text
=== Expense Tracker ===

1. Add Expense
2. View Expenses
3. View Total Spending
4. Exit
```

The user should be able to choose an option.

---

## 2. Add Expense

The user enters:

- Expense description
- Expense amount

Example:

```text
Description: Groceries
Amount: 45
```

The program stores the expense.

---

## 3. View Expenses

The program displays all recorded expenses.

Example:

```text
Expenses:

1. Groceries - $45
2. Gas - $30
3. Lunch - $15
```

---

## 4. View Total Spending

The program calculates and displays the total.

Example:

```text
Total spending: $90
```

---

## 5. Exit

The program ends when the user selects:

```text
4
```

Output:

```text
Goodbye!
```

---

# Rules / Constraints

- Expense amount must be a number.
- Expense amount cannot be negative.
- The program should continue running until the user exits.
- If the user enters an invalid menu option, show an error.

---

# Suggested Functions

You don't have to use these, but they are good practice:

```python
display_menu()

add_expense()

view_expenses()

calculate_total()

validate_amount()
```

---

# Testing

## Test Case 1: Add Expense

### Input

```text
1
Groceries
45
```

### Expected Output

```text
Expense added successfully!
```

---

## Test Case 2: View Expenses

### Starting Data

```text
Groceries - $45
Gas - $30
```

### Input

```text
2
```

### Expected Output

```text
Expenses:

1. Groceries - $45
2. Gas - $30
```

---

## Test Case 3: Calculate Total

### Input

```text
3
```

### Expected Output

```text
Total spending: $75
```

---

## Test Case 4: Invalid Amount

### Input

```text
1
Coffee
hello
```

### Expected Output

```text
Invalid amount. Please enter a number.
```

---

## Test Case 5: Negative Amount

### Input

```text
1
Dinner
-20
```

### Expected Output

```text
Amount cannot be negative.
```