# Product 2: Password Strength Checker

## Objective

Create a program that analyzes a password and rates its strength.

---

# Functional Requirements

The program asks:

```text
Enter password:
```

It checks the password against the following requirements.

---

## Requirement 1: Length

The password must contain **at least 8 characters**.

---

## Requirement 2: Uppercase Letter

The password must contain **at least one uppercase letter**.

---

## Requirement 3: Lowercase Letter

The password must contain **at least one lowercase letter**.

---

## Requirement 4: Number

The password must contain **at least one digit**.

---

## Requirement 5: Special Character

The password must contain **at least one** of the following special characters:

```text
! @ # $ % & *
```

---

# Scoring System

Each requirement satisfied is worth **1 point**.

| Score | Rating |
|-------:|---------|
| 0–2 | Weak |
| 3–4 | Medium |
| 5 | Strong |

---

# Rules / Constraints

- The password cannot be empty.
- Check every requirement, even if one fails.
- Display which requirements passed and which failed.
- Display the final strength rating after all checks are complete.

---

# Suggested Functions

You don't have to use these, but they are good practice:

```python
check_length()

check_uppercase()

check_lowercase()

check_number()

check_special()

calculate_strength()
```

---

# Testing

## Test Case 1: Strong Password

### Input

```text
Password:
Secure123!
```

### Expected Output

```text
Password Analysis:

✓ Length
✓ Uppercase
✓ Lowercase
✓ Number
✓ Special Character

Strength: Strong
```

---

## Test Case 2: Weak Password

### Input

```text
Password:
hello
```

### Expected Output

```text
Password Analysis:

✗ Length
✗ Uppercase
✓ Lowercase
✗ Number
✗ Special Character

Strength: Weak
```

---

## Test Case 3: Medium Password

### Input

```text
Password:
Hello123
```

### Expected Output

```text
Password Analysis:

✓ Length
✓ Uppercase
✓ Lowercase
✓ Number
✗ Special Character

Strength: Medium
```

---

## Test Case 4: Empty Password

### Input

```text
Password:
```

### Expected Output

```text
Password cannot be empty.
```