# Student Admission Decision System

# -------- INPUT --------
entrance_score = int(input("Entrance Score (0-100): "))
gpa = float(input("GPA (0-10): "))
has_recommendation = input("Recommendation letter (yes/no): ").lower()
category = input("Category (general/obc/sc_st): ").lower()
extracurricular_score = float(input("Extracurricular Score (0-10): "))

# -------- INPUT VALIDATION --------
if entrance_score < 0 or entrance_score > 100:
    print("REJECTED: Entrance score must be between 0 and 100")
    exit()

if gpa < 0 or gpa > 10:
    print("REJECTED: GPA must be between 0 and 10")
    exit()

if has_recommendation not in ["yes", "no"]:
    print("REJECTED: Recommendation must be yes or no")
    exit()

if category not in ["general", "obc", "sc_st"]:
    print("REJECTED: Invalid category")
    exit()

if extracurricular_score < 0 or extracurricular_score > 10:
    print("REJECTED: Extracurricular score must be between 0 and 10")
    exit()

# -------- MERIT RULE --------
if entrance_score >= 95:
    print("\nResult: ADMITTED (Scholarship)")
    print("Reason: Entrance score >= 95 (Merit Rule)")
    exit()

# -------- BONUS CALCULATION --------
bonus = 0

if has_recommendation == "yes":
    bonus += 5

if extracurricular_score > 8:
    bonus += 3

effective_score = entrance_score + bonus

print("\nBonus Applied:", bonus)
print("Effective Score:", effective_score)

# -------- CATEGORY CUT-OFF --------
if category == "general":
    cutoff = 75
elif category == "obc":
    cutoff = 65
else:
    cutoff = 55

# -------- DECISION --------
if gpa < 7.0:
    print("\nResult: REJECTED")
    print("Reason: GPA below minimum requirement (7.0)")
elif effective_score >= cutoff:
    print("\nResult: ADMITTED (Regular)")
    print("Reason: Meets category cutoff and GPA requirement")
elif effective_score >= cutoff - 5:
    print("\nResult: WAITLISTED")
    print("Reason: Slightly below cutoff")
else:
    print("\nResult: REJECTED")
    print("Reason: Score below cutoff")