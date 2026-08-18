# Credit Card Transaction Categorizer — Python Spec Sheet

## 1. Project Goal

Build a basic Python program that reads credit card transactions and automatically assigns each transaction to a spending category.

**Initial goal:** Keep it simple. Use only basic Python concepts you've already been learning.

---

## 2. Input

Start with transactions entered directly into Python.

Example:

```python
transactions = [
    {"description": "Massy Stores", "amount": 450.00},
    {"description": "Netflix", "amount": 89.99},
    {"description": "Uber", "amount": 65.00},
    {"description": "KFC", "amount": 75.00}
]
```

Eventually, you can replace this with a CSV file.

---

## 3. Categories

Start with these categories:

* Groceries
* Dining
* Transportation
* Entertainment
* Shopping
* Bills
* Other

---

## 4. Categorization Rules

Create rules that associate keywords with categories.

Example:

```text
"massy"       → Groceries
"price smart" → Groceries
"kfc"         → Dining
"uber"        → Transportation
"netflix"     → Entertainment
"amazon"      → Shopping
```

The program should check the transaction description and determine which category it belongs to.

If no rule matches:

```text
→ Other
```

---

## 5. Required Functions

Try to break the program into functions.

### `categorize_transaction()`

**Input:**

* Transaction description

**Output:**

* Category

Example:

```python
categorize_transaction("MASSY STORES")
```

Expected result:

```text
"Groceries"
```

---

### `calculate_total()`

**Input:**

* List of transactions

**Output:**

* Total amount spent

Example:

```text
450 + 89.99 + 65 + 75
```

Expected result:

```text
679.99
```

---

### `display_transactions()`

Display each transaction in a readable format:

```text
Massy Stores       $450.00   Groceries
Netflix             $89.99   Entertainment
Uber                $65.00   Transportation
KFC                 $75.00   Dining
```

---

### `display_summary()`

Display spending totals by category:

```text
===== SPENDING SUMMARY =====

Groceries:       $450.00
Dining:           $75.00
Transportation:  $65.00
Entertainment:   $89.99

Total:           $679.99
```

---

## 6. Program Flow

Your program should roughly work like this:

```text
START
  ↓
Load transactions
  ↓
Categorize transactions
  ↓
Display transactions
  ↓
Calculate spending totals
  ↓
Display summary
  ↓
END
```

---

## 7. Python Concepts You Should Practice

**Do not use Pandas or NumPy yet.**

Use:

* Variables
* Strings
* Integers / floats
* Lists
* Dictionaries
* `for` loops
* `if / elif / else`
* Functions
* `return`
* String methods such as `.lower()`
* Basic exception handling
* Basic user input

This is a good project for where you are in CS50 because you can gradually add complexity instead of trying to build everything at once.

---

## 8. Version 1 Requirements

Your first version should be able to:

* [ ] Store transactions in a list
* [ ] Store transaction descriptions and amounts
* [ ] Categorize transactions using keywords
* [ ] Handle transactions with no matching category
* [ ] Display all transactions
* [ ] Calculate total spending
* [ ] Display spending by category
* [ ] Use separate functions for major tasks

---

## 9. Don't Add Yet

Do **not** add these features to Version 1:

* Pandas
* NumPy
* Machine learning
* GUI
* Streamlit
* Database
* CSV importing
* AI / API calls

**Get the basic Python version working first.**

---

## 10. Future Versions

Once the basic Python version works, gradually increase the complexity.

### Version 2 — CSV

Replace hardcoded transactions with a CSV file.

```text
CSV
 ↓
Python
 ↓
Categorization
 ↓
Summary
```

### Version 3 — Pandas

Use Pandas for:

* Reading CSV files
* Filtering transactions
* Grouping transactions
* Calculating totals
* Data analysis

```text
CSV
 ↓
Pandas
 ↓
Data Cleaning
 ↓
Categorization
 ↓
Analysis
```

### Version 4 — Visualization

Add charts and visualizations.

Possible analysis:

* Spending by category
* Spending over time
* Highest spending categories
* Monthly spending
* Average transaction amount

### Version 5 — Machine Learning

Eventually experiment with automatically categorizing transactions using machine learning.

```text
Transaction Description
          ↓
      Data Cleaning
          ↓
    Feature Extraction
          ↓
   Machine Learning Model
          ↓
       Category
```

---

## 11. Project Progression

The long-term progression could look like:

```text
Basic Python
     ↓
Lists + Dictionaries
     ↓
Functions + Loops
     ↓
CSV Files
     ↓
Pandas
     ↓
Data Cleaning
     ↓
Data Analysis
     ↓
Visualization
     ↓
Machine Learning
     ↓
Streamlit Application
```

This lets you keep building the **same application** while gradually introducing more advanced programming and data science concepts.

---

## 12. Main Rule

> **Build the simplest working version first.**

Don't worry about making the program impressive.

The goal of Version 1 is to strengthen your understanding of:

* Python data structures
* Functions
* Loops
* Conditions
* String manipulation
* Program decomposition
* Basic data processing

Once that works, make it better one version at a time.
