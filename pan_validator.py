# PAN Card Validator

pan = input("Enter PAN number: ").strip()

# Check length
if len(pan) != 10:
    print("Invalid PAN: Length must be 10 characters")

# Check first 5 characters (letters)
elif not pan[:5].isalpha():
    print("Invalid PAN: First 5 characters must be letters")

# Check next 4 characters (digits)
elif not pan[5:9].isdigit():
    print("Invalid PAN: Characters 6-9 must be digits")

# Check last character (letter)
elif not pan[9].isalpha():
    print("Invalid PAN: Last character must be a letter")

# Check uppercase
elif pan != pan.upper():
    print("Invalid PAN: Must be uppercase")

else:
    print("Valid PAN Number")

    taxpayer_type = pan[3]

    print("Taxpayer type indicator:", taxpayer_type)