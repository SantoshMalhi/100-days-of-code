import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if len(characters) == 0:
        return "Error: No character types selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Python Password Generator!")
    length = int(input("Enter desired password length: "))
    lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    digits = input("Include digits? (yes/no): ").lower() == "yes"
    special = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, lowercase, uppercase, digits, special)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
