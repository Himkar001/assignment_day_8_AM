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

