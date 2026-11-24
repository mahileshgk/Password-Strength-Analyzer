def analyze_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password): 
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    if password and len(set(password)) / len(password) >= 0.7:
        score += 1

    print("\n--- PASSWORD ANALYSIS ---")
    print("Score:", score, "/ 7")

    if score >= 6:
        print("Password Strength: STRONG")
    elif score >= 4:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: WEAK")

print("==============================")
print("   PASSWORD STRENGTH ANALYZER")
print("==============================")

password = input("Enter a test password: ")

if password:
    analyze_password(password)
else:
    print("Password cannot be empty!")
