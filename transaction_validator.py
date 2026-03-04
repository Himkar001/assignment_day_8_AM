# Smart Transaction Validator

amount = float(input("Transaction amount (Rs): "))
category = input("Category (food/travel/electronics/other): ").lower()
hour = int(input("Hour of transaction (0-23): "))
daily_spent = float(input("Amount already spent today (Rs): "))
vip = input("VIP customer? (yes/no): ").lower()

# VIP multiplier using ternary operator
multiplier = 2 if vip == "yes" else 1

# Limits
single_limit = 50000 * multiplier
daily_limit = 100000 * multiplier

food_limit = 5000 * multiplier
electronics_limit = 30000 * multiplier


# -------- BLOCK RULES --------

if amount > single_limit:
    print("BLOCKED: exceeds single transaction limit")

elif daily_spent + amount > daily_limit:
    print("BLOCKED: exceeds daily spending limit")


# -------- FLAG RULES --------

elif hour < 6 or hour > 23:
    print("FLAGGED: unusual transaction hour")


# -------- CATEGORY RULES --------

elif category == "food" and amount > food_limit:
    print("FLAGGED: food category limit exceeded")

elif category == "electronics" and amount > electronics_limit:
    print("FLAGGED: electronics category limit exceeded")


# -------- APPROVED --------

else:
    print("APPROVED")