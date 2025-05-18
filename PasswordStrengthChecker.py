def password_strength(password):
    #Password strength score and feedback
    strength_score = 0
    feedback = []
    #Check password length- 8 char minimum
    if len(password) < 8:
        feedback.append("Whilst brevity may be the heart of wit, it is not the heart of a good password! Try for 8 characters or more :)")
    else:
        strength_score += 1
    #Check for uppercase letters
    if not any(char.isupper() for char in password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        strength_score += 1

        # Check for lowercase letters
    if not any(char.islower() for char in password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        strength_score += 1

        # Check for numbers
    if not any(char.isdigit() for char in password):
        feedback.append("Password should contain at least one number.")
    else:
        strength_score += 1

        # Check for special characters
    special_chars = "!@#$%^&*()_+={}[]:;<>,.?~\\/-'"
    if not any(char in special_chars for char in password):
        feedback.append("Password should contain at least one special character.")
    else:
        strength_score += 1

    # Determine overall strength
    if strength_score == 5:
        overall = "Strong"
    elif strength_score >= 3:
        overall = "Moderate"
    else:
        overall = "Weak"

    return {
        "score": strength_score,
        "strength": overall,
        "feedback": feedback
    }


test_password = input("Enter a password to check: ")
result = password_strength(test_password)

print(f"\nPassword Strength: {result['strength']} ({result['score']}/5)")

if result['feedback']:
    print("\nImprovement suggestions:")
    for suggestion in result['feedback']:
        print(f"- {suggestion}")
else:
    print("\nYour password meets all strength criteria!")


