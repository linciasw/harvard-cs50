# Product 3: Mini Banking System

## Objective

Create a simple ATM simulation where a user can check their balance, deposit money, and withdraw money.

---

# Starting State

When the program starts:

```text
Balance: $1000
```

Use this as the initial account balance.

---

# Functional Requirements

## Display Menu

The program should repeatedly display:

```text
=== Mini Bank ===

1. Check Balance
2. Deposit
3. Withdraw
4. Exit
```

The user should be able to choose an option.

---

## 1. Check Balance

Display the current account balance.

Example:

```text
Current balance: $1000
```

---

## 2. Deposit

The user enters a deposit amount.

Example:

```text
Deposit amount:
500
```

If the amount is valid, update the balance.

Example Output:

```text
Deposit successful!

New balance: $1500
```

---

## 3. Withdraw

The user enters a withdrawal amount.

Example:

```text
Withdrawal amount:
200
```

If the withdrawal is valid, subtract it from the balance.

Example Output:

```text
Withdrawal successful!

New balance: $800
```

---

## 4. Exit

The program ends when the user selects:

```text
4
```

Output:

```text
Thank you for banking with us!
```

---

# Rules / Constraints

- The starting balance is **$1000**.
- Deposit amounts must be numeric.
- Deposit amounts cannot be negative.
- Withdrawal amounts must be numeric.
- Withdrawal amounts cannot be negative.
- A withdrawal cannot exceed the current account balance.
- If the user enters an invalid menu option, display an error message.
- The program should continue running until the user chooses to exit.

---

# Suggested Functions

You don't have to use these, but they are good practice:

```python
display_menu()

check_balance()

deposit()

withdraw()

validate_amount()
```

---

# Testing

## Test Case 1: Check Balance

### Input

```text
1
```

### Expected Output

```text
Current balance: $1000
```

---

## Test Case 2: Deposit Money

### Input

```text
2
500
```

### Expected Output

```text
Deposit successful!

New balance: $1500
```

---

## Test Case 3: Withdraw Money

### Input

```text
3
200
```

### Expected Output

```text
Withdrawal successful!

New balance: $800
```

---

## Test Case 4: Insufficient Funds

### Input

```text
3
2000
```

### Expected Output

```text
Insufficient funds.
```

---

## Test Case 5: Invalid Deposit Amount

### Input

```text
2
abc
```

### Expected Output

```text
Invalid amount.
```

---

## Test Case 6: Negative Withdrawal

### Input

```text
3
-50
```

### Expected Output

```text
Amount cannot be negative.
```

---

## Test Case 7: Invalid Menu Option

### Input

```text
8
```

### Expected Output

```text
Invalid menu option. Please try again.
```