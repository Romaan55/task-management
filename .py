#------------------Task 1-------------------------

password = input("Enter the Password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_character = "!@#$%^&*()+{}-?><:~"

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if ch in special_character:
        has_special = True     

         
score = 0
if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Moderate"
else:
    strength = "Strong"

print("\nPassword Security Report")
print("-" * 30)
print("Security Score:", score, "/5")
print("Password Strength:", strength)

print("\nFeedback: ")

if len(password) < 8:
    print("- Password should be at least 8 characters long.")

if not has_upper:
    print("- Add at least one uppercase letter (A-Z).")

if not has_lower:
    print("- Add at least one lowercase letter (a-z).")

if not has_digit:
    print("- Add at least one number (0-9).")

if not has_special:
    print("- Add at least one special character (!@#$%^&* etc.).")

if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_special
):
    print("Good JOB! Your password meets all security system.")