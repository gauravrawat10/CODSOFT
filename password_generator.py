import random
import string

def generate_password(length, complexity):
    # Define character sets based on complexity
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Determine the character set based on complexity level
    if complexity == 1:
        char_set = lowercase
    elif complexity == 2:
        char_set = lowercase + uppercase
    elif complexity == 3:
        char_set = lowercase + uppercase + digits
    elif complexity == 4:
        char_set = lowercase + uppercase + digits + special_chars
    else:
        print("Invalid complexity level. Choose between 1 and 4.")
        return None

    # Generate the password
    password = ''.join(random.choice(char_set) 
    for _ in range(length))
    return password

# Get user input for password length and complexity
try:
    length = int(input("Enter the desired password length: "))
    complexity = int(input("Enter the desired complexity level (1-4): "))
    password = generate_password(length, complexity)
    if password:
        print(f"Generated password: {password}")
except ValueError:
    print("Please enter valid numbers for length and complexity.")