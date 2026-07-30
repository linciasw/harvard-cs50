# Product: Loan Installment Calculator (CLI)

## Objective

Create a command-line application that calculates the monthly installment payment for a loan.

The program should allow a user to enter loan details, calculate the monthly payment, and display the repayment information.

---

# Functional Requirements

## 1. Display Program Title

When the program starts, display:

```text
=== Loan Installment Calculator ===
```

---

# 2. User Input

The program should ask the user for the following information:

## Loan Amount

Prompt:

```text
Enter loan amount:
```

Example:

```text
Enter loan amount: 50000
```

The loan amount should be stored as a number.

---

## Annual Interest Rate

Prompt:

```text
Enter annual interest rate (%):
```

Example:

```text
Enter annual interest rate (%): 6.5
```

The user should enter the interest rate as a percentage.

---

## Loan Term

Prompt:

```text
Enter loan term (years):
```

Example:

```text
Enter loan term (years): 5
```

The program should convert years into months for calculations.

---

# 3. Calculate Monthly Installment

The program should calculate the monthly loan payment using the formula:

```
M = P × r(1 + r)^n / ((1 + r)^n - 1)
```

Where:

```
M = Monthly installment

P = Loan principal amount

r = Monthly interest rate

n = Number of monthly payments
```

---

## Interest Conversion

The annual interest rate must be converted into a monthly interest rate:

```
monthly_interest_rate = annual_interest_rate / 12 / 100
```

Example:

```
6% annual interest

6 / 12 / 100

= 0.005 monthly interest
```

---

## Loan Term Conversion

Convert years into months:

```
number_of_payments = loan_years * 12
```

Example:

```
5 years

5 * 12

= 60 monthly payments
```

---

# 4. Display Results

After calculating, display:

```text
=== Loan Summary ===

Loan Amount: $50,000.00
Interest Rate: 6.5%
Loan Term: 5 years

Monthly Payment: $978.03
Total Payment: $58,681.80
Total Interest: $8,681.80
```

---

# 5. Calculate Total Payment

The program should calculate:

```
total_payment = monthly_payment * number_of_payments
```

---

# 6. Calculate Total Interest

The program should calculate:

```
total_interest = total_payment - loan_amount
```

---

# 7. Input Validation

The program should check for invalid inputs.

## Loan Amount

The loan amount cannot be:

- Zero
- Negative numbers
- Text values

Example:

```text
Enter loan amount: -5000

Error: Loan amount must be greater than zero.
```

---

## Interest Rate

The interest rate cannot be:

- Negative numbers
- Text values

Example:

```text
Enter annual interest rate (%): -3

Error: Interest rate cannot be negative.
```

---

## Loan Term

The loan term cannot be:

- Zero
- Negative numbers
- Text values

Example:

```text
Enter loan term (years): 0

Error: Loan term must be greater than zero.
```

---

# 8. Program Loop

After displaying the loan summary, ask:

```text
Would you like to calculate another loan? (yes/no):
```

If the user enters:

```
yes
```

Restart the program.

If the user enters:

```
no
```

Display:

```text
Thank you for using the Loan Installment Calculator!
```

---

# Testing Requirements

## Test Case 1: Standard Loan

### Input

```text
Loan Amount: 50000
Interest Rate: 6.5
Loan Term: 5
```

### Expected Output

```text
Monthly Payment: approximately $978.03

Total Payment: approximately $58,681.80

Total Interest: approximately $8,681.80
```

---

# Test Case 2: Zero Interest Loan

### Input

```text
Loan Amount: 12000
Interest Rate: 0
Loan Term: 2
```

### Expected Output

```text
Monthly Payment: $500.00

Total Payment: $12,000.00

Total Interest: $0.00
```

---

# Test Case 3: Invalid Loan Amount

### Input

```text
Loan Amount: -1000
```

### Expected Output

```text
Error: Loan amount must be greater than zero.
```

---

# Test Case 4: Invalid Interest Rate

### Input

```text
Interest Rate: -5
```

### Expected Output

```text
Error: Interest rate cannot be negative.
```

---

# Test Case 5: Invalid Loan Term

### Input

```text
Loan Term: 0
```

### Expected Output

```text
Error: Loan term must be greater than zero.
```

---

# Python Concepts Practiced

This project should reinforce:

- Variables
- Data types
- User input
- Functions
- Conditionals
- Loops
- Error handling (`try` / `except`)
- Mathematical calculations
- Formatting numbers
- Modular programming

---

# Suggested Program Structure

Your Python file could be organized like:

```
loan_calculator.py
```

Functions:

```python
def get_loan_details():
    pass


def calculate_monthly_payment():
    pass


def display_summary():
    pass


def main():
    pass
```

---

# Future Improvements

After completing the basic version, consider adding:

- Different loan types (mortgage, car loan, personal loan)
- Amortization schedule
- CSV export of payments
- GUI version using Tkinter
- Streamlit web version
- Currency selection
- Extra payments calculator