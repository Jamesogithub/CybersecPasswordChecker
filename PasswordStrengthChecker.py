def password_strength(password):
    #Password strength score and feedback
    #test commit line
    strength_score = 0
    feedback = []
    #Check password length- 8 char minimum
    if len(password) < 8:
        feedback.append("Whilst brevity may be the soul of wit, it is \x1B[3mnot\x1B[0m the soul of a good password! Try for 8 characters or more :)")
    else:
        strength_score += 1
    #Check for uppercase letters
    if not any(char.isupper() for char in password):
        feedback.append("You should add an uppercase letter- it adds some authority!")
    else:
        strength_score += 1

        # Check for lowercase letters
    if not any(char.islower() for char in password):
        feedback.append("No need to shout, add some lowercase letters!")
    else:
        strength_score += 1

        # Check for numbers
    if not any(char.isdigit() for char in password):
        feedback.append("Adding some numbers will strengthen your password- count on it!")
    else:
        strength_score += 1

        # Check for special characters
    special_chars = "!@#$%^&*()_+={}[]:;<>,.?~\\/-'"
    if not any(char in special_chars for char in password):
        feedback.append("A little punctuation can do wonders for strength \x1B[3mand\x1B[0m style.")
    else:
        strength_score += 1

    # Determine overall strength
    if strength_score == 5:
        overall = "Pretty strong, good effort! Now don't forget it..."
    elif strength_score >= 3:
        overall = "Not too bad, but you can do better!"
    else:
        overall = "Definitely could be better, try again!"

    return {
        "score": strength_score,
        "strength": overall,
        "feedback": feedback
    }


while True:
    test_password = input("Enter a password to check, or enter 'quit' to exit: ")
    
    if test_password.lower() == 'quit':
        print("Thank you for using the password checker!")
        break
        
    result = password_strength(test_password)
    
    print(f"\nPassword Strength: {result['strength']} ({result['score']}/5)")
    
    if result['feedback']:
        print("\nImprovement suggestions:")
        for suggestion in result['feedback']:
            print(f"- {suggestion}")
    else:
        print("\nYour password meets all strength criteria!")
    
    print("\n" + "-"*50 + "\n")  # Add a separator line between attempts