# Indian Income Tax Calculator (New Regime FY 2024-25)

income = float(input("Enter your annual income (Rs): "))

STANDARD_DEDUCTION = 75000
taxable_income = income - STANDARD_DEDUCTION

if taxable_income < 0:
    taxable_income = 0

print("\nStandard Deduction Applied: Rs.", STANDARD_DEDUCTION)
print("Taxable Income:", taxable_income)

tax = 0

# Slab 1: 0 - 3L
if taxable_income > 300000:
    slab_tax = 0
    print("0 - 3L taxed at 0%: Rs.", slab_tax)
else:
    slab_tax = 0
    print("0 -", taxable_income, " taxed at 0%")
    print("\nTotal Tax:", tax)
    exit()

# Slab 2: 3L - 7L
if taxable_income > 700000:
    slab_tax = (700000 - 300000) * 0.05
    tax += slab_tax
    print("3L - 7L taxed at 5%:", slab_tax)
else:
    slab_tax = (taxable_income - 300000) * 0.05
    tax += slab_tax
    print("3L -", taxable_income, " taxed at 5%:", slab_tax)
    print("\nTotal Tax:", tax)
    exit()

# Slab 3: 7L - 10L
if taxable_income > 1000000:
    slab_tax = (1000000 - 700000) * 0.10
    tax += slab_tax
    print("7L - 10L taxed at 10%:", slab_tax)
else:
    slab_tax = (taxable_income - 700000) * 0.10
    tax += slab_tax
    print("7L -", taxable_income, " taxed at 10%:", slab_tax)
    print("\nTotal Tax:", tax)
    exit()

# Slab 4: 10L - 12L
if taxable_income > 1200000:
    slab_tax = (1200000 - 1000000) * 0.15
    tax += slab_tax
    print("10L - 12L taxed at 15%:", slab_tax)
else:
    slab_tax = (taxable_income - 1000000) * 0.15
    tax += slab_tax
    print("10L -", taxable_income, " taxed at 15%:", slab_tax)
    print("\nTotal Tax:", tax)
    exit()

# Slab 5: 12L - 15L
if taxable_income > 1500000:
    slab_tax = (1500000 - 1200000) * 0.20
    tax += slab_tax
    print("12L - 15L taxed at 20%:", slab_tax)
else:
    slab_tax = (taxable_income - 1200000) * 0.20
    tax += slab_tax
    print("12L -", taxable_income, " taxed at 20%:", slab_tax)
    print("\nTotal Tax:", tax)
    exit()

# Slab 6: Above 15L
slab_tax = (taxable_income - 1500000) * 0.30
tax += slab_tax
print("Above 15L taxed at 30%:", slab_tax)

print("\nTotal Tax Payable:", tax)

effective_rate = (tax / income) * 100
print("Effective Tax Rate:", round(effective_rate, 2), "%")