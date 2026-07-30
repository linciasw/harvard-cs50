# Product 4: Compound Interest Calculator (CLI)

## Objective

Create a command-line application that calculates how much an investment will grow over time using compound interest.

The program should allow the user to enter an initial investment amount, interest rate, investment period, and compounding frequency.

---

# Functional Requirements

## 1. Display Menu

When the program starts, display:

```text
=== Compound Interest Calculator ===
1. Calculate Future Value
2. View Calculation History
3. Exit
```

The user should be able to select an option repeatedly until they choose Exit.

## 2. Calculate Future Value

When the user selects option 1, prompt:

```text
Enter initial investment amount:
```

Example:

```text
Enter initial investment amount: 10000
```

Prompt:

```text
Enter annual interest rate (%):
```

Example:

```text
Enter annual interest rate (%): 5
```

The program should convert the percentage into a decimal.

Example:

```text
5% = 0.05
```

Prompt:

```text
Enter investment period (years):
```

Example:

```text
Enter investment period (years): 10
```

Prompt:

```text
Choose compounding frequency:
1. Annually
2. Semi-Annually
3. Quarterly
4. Monthly
```

## 3. Calculation Formula

The program should calculate compound interest using:

```text
A = P(1 + r/n)^(nt)
```

Where:

- `A` = Final investment amount
- `P` = Initial investment amount
- `r` = Annual interest rate (decimal)
- `n` = Number of times interest compounds per year
- `t` = Number of years

Compounding values:

| Frequency      | n  |
|----------------|----|
| Annually       | 1  |
| Semi-Annually  | 2  |
| Quarterly      | 4  |
| Monthly        | 12 |

## 4. Display Results

After calculation, display:

```text
=== Investment Summary ===
Initial Investment: $10,000.00
Interest Rate: 5%
Investment Period: 10 years
Compounding Frequency: Monthly
Total Interest Earned: $6,470.09
Future Value: $16,470.09
```

## 5. Calculation History

The program should store previous calculations.

When the user selects:

```text
2. View Calculation History
```

Display:

```text
=== Calculation History ===
1.
Investment: $10,000
Rate: 5%
Years: 10
Future Value: $16,470.09

2.
Investment: $5,000
Rate: 7%
Years: 15
Future Value: $14,267.95
```

## 6. Input Validation

### Investment Amount

Cannot be zero or negative.

Example:

```text
Enter initial investment amount: -500
Invalid amount. Please enter a positive number.
```

### Interest Rate

Cannot be negative.

Example:

```text
Enter annual interest rate (%): -2
Invalid interest rate.
```

### Investment Period

Cannot be zero or negative.

Example:

```text
Enter investment period: 0
Investment period must be greater than zero.
```

### Menu Selection

If the user enters an invalid option:

```text
Choice: 7
Invalid option. Please select 1-3.
```

---

# Testing

## Test Case 1: Basic Calculation

**Input**

```text
Choice: 1
Investment Amount: 10000
Interest Rate: 5
Years: 10
Frequency: 1
```

**Expected Output**

```text
Future Value: $16,288.95
Total Interest Earned: $6,288.95
```

## Test Case 2: Monthly Compounding

**Input**

```text
Choice: 1
Investment Amount: 5000
Interest Rate: 7
Years: 15
Frequency: 4
```

**Expected Output**

```text
Future Value: $14,267.95
Total Interest Earned: $9,267.95
```

## Test Case 3: Invalid Investment

**Input**

```text
Investment Amount: -1000
```

**Expected Output**

```text
Invalid amount. Please enter a positive number.
```

## Test Case 4: View History

**Input**

```text
Choice: 2
```

**Expected Output**

```text
=== Calculation History ===
Previous calculations are displayed.
```

---

# Skills Practiced

This project should reinforce:

- Variables
- Data types
- Functions
- Conditionals
- Loops
- User input
- Error handling
- Lists
- Dictionaries
- File handling (optional)
- Mathematical calculations

---

# Optional Improvements

After completing the basic version:

- Export calculation history to CSV
- Allow recurring monthly deposits
- Add a graphical interface using Tkinter
- Create charts showing investment growth
- Add inflation adjustment
- Create a Streamlit web version