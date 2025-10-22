import random
import string

print("Welcome to the Basic Password Generator")

try:
    length = int(input("Enter the desired password length: "))

    # Defines possible characters for the password
    characters = string.ascii_letters + string.digits
    # Generate password by randomly picking characters
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the generated password
    print("Your generated password is: ")
    print(password)

except ValueError:
    print("Please enter a valid number.")