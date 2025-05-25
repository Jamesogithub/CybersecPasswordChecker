def load_common_passwords(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return {line.strip().lower() for line in file}
    except FileNotFoundError:
        print(f"Warning: Password list file '{filename}' not found.")
        return set()
    except Exception as e:
        print(f"Warning: Error loading password list: {e}")
        return set()

def password_strength(password, common_passwords):
    # First check if password is in common password list
    if password.lower() in common_passwords:
        return {
            "score": 0,
            "strength": "Unsafe - This is a commonly used password!",
            "feedback": ["This password appears in a list of commonly used passwords. Try being a bit more unique, don't be a sheep."]
        }
    
    #Password strength score and feedback
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

# Load the common passwords at startup
common_passwords = load_common_passwords('100kcommonpasswords.txt')

while True:
    test_password = input("Enter a password to check, or enter 'quit' to exit: ")
    
    if test_password.lower() == 'quit':
        print("Thank you for using the password checker!")
        break
        
    result = password_strength(test_password, common_passwords)
    
    print(f"\nPassword Strength: {result['strength']}")
    if result['score'] > 0:  # Only show score if it's not a common password
        print(f"Score: ({result['score']}/5)")
    
    if result['feedback']:
        print("\nImprovement suggestions:")
        for suggestion in result['feedback']:
            print(f"- {suggestion}")
    else:
        print("\nYour password meets all strength criteria!")
    
    print("\n" + "-"*50 + "\n")  # Add a separator line between attempts