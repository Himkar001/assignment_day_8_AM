# Day 08 – Conditional Logic Assignment

## Topics Covered
- if / elif / else
- comparison operators
- logical operators
- nested if
- ternary operator
- input validation

---

# PART A – Student Admission Decision System

A rule-based admission system that evaluates students using:

Inputs:
- entrance_score
- gpa
- recommendation letter
- category
- extracurricular score

Rules Implemented:
- Category cutoffs  
  - General ≥ 75  
  - OBC ≥ 65  
  - SC/ST ≥ 55  

- Minimum GPA requirement = 7.0

- Merit Rule  
  - Entrance score ≥ 95 → automatic scholarship admission

- Bonus points
  - Recommendation letter → +5
  - Extracurricular score > 8 → +3

Outputs:
- ADMITTED (Scholarship)
- ADMITTED (Regular)
- WAITLISTED
- REJECTED (with reason)

---

# PART B – Indian Income Tax Calculator

Implements progressive taxation using the **New Tax Regime FY 2024–25**.

Standard Deduction: ₹75,000

Tax Slabs:

| Income Range | Tax Rate |
|--------------|----------|
| 0 – 3L | 0% |
| 3 – 7L | 5% |
| 7 – 10L | 10% |
| 10 – 12L | 15% |
| 12 – 15L | 20% |
| Above 15L | 30% |

Program Output:
- Tax per slab
- Total tax payable
- Effective tax rate

How to Run Programs
python Day_08/admission_system.py
python Day_08/tax_calculator.py

---

# PART C – Interview Questions

## Q1: Difference between `elif` and multiple `if`

### Using multiple `if`

score = 85

if score >= 60:
print("D")

if score >= 70:
print("C")

if score >= 80:
print("B")


Output:

D
C
B


All conditions run independently.

---

### Using `elif`

score = 85

if score >= 80:
print("B")
elif score >= 70:
print("C")
elif score >= 60:
print("D")


Output:

B


Reason:  
`elif` stops checking after the first true condition.

---

## Q2: Triangle Classification Function

```python
def classify_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle"

    if a >= b + c or b >= a + c or c >= a + b:
        return "Not a triangle"

    if a == b == c:
        return "Equilateral"

    elif a == b or b == c or a == c:
        return "Isosceles"

    else:
        return "Scalene"
Q3: Debugging Conditional Logic
Given Code
score = 85

if score >= 60:
    grade = 'D'

if score >= 70:
    grade = 'C'

if score >= 80:
    grade = 'B'

if score >= 90:
    grade = 'A'

print(grade)
Problem

Multiple if statements overwrite the variable grade.

Each condition runs independently.

Correct Fix
if score >= 90:
    grade = 'A'

elif score >= 80:
    grade = 'B'

elif score >= 70:
    grade = 'C'

else:
    grade = 'D'

Now only one condition executes.


---

# PART D – PAN Card Validator

## Objective

Validate an **Indian PAN card number** using conditional logic.

### PAN Format

```
ABCDE1234F
```

Structure:

| Position | Requirement       |
| -------- | ----------------- |
| 1–5      | Uppercase letters |
| 6–9      | Digits            |
| 10       | Uppercase letter  |

Example of a valid PAN:

```
ABCDE1234F
```

### Program Validation Steps

The program checks:

1. PAN length must be **10 characters**
2. First **5 characters must be letters**
3. Next **4 characters must be digits**
4. Last **character must be a letter**
5. Entire PAN must be **uppercase**

### Output

Valid PAN example:

```
Valid PAN Number
Taxpayer type indicator: D
```

Invalid PAN example:

```
Invalid PAN: Length must be 10 characters
```

---

# PART E – Smart Transaction Validator

## Objective

Simulate a **rule-based fraud detection system** for financial transactions.

### Inputs

* transaction amount
* transaction category
* transaction hour
* amount already spent today
* VIP status

### Blocking Rules

Transaction is **BLOCKED** if:

* amount > ₹50,000
* daily spending exceeds ₹100,000

Blocking rules override all other checks.

---

### Flag Rules

Transaction is **FLAGGED** if:

* transaction occurs **before 6 AM**
* transaction occurs **after 11 PM**

---

### Category Limits

| Category    | Limit   |
| ----------- | ------- |
| Food        | ₹5,000  |
| Electronics | ₹30,000 |

If exceeded → **FLAGGED**

---

### VIP Enhancement

VIP users get **double limits**.

Example:

| Rule               | Normal   | VIP      |
| ------------------ | -------- | -------- |
| Single transaction | ₹50,000  | ₹100,000 |
| Daily limit        | ₹100,000 | ₹200,000 |

Implemented using **Python ternary operator**.

---

### Possible Outputs

```
APPROVED
FLAGGED: unusual transaction hour
FLAGGED: category limit exceeded
BLOCKED: exceeds single transaction limit
BLOCKED: exceeds daily spending limit
```

---

# Repository Structure

```

├── admission_system.py
├── tax_calculator.py
├── pan_validator.py
├── transaction_validator.py
└── README.md
```



