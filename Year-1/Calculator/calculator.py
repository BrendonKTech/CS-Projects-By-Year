# Function Definitions: These make your code reusable and organized
def add(x, y):
    # Returns the sum of x and y
    return x + y

def sub(x, y):
    # Returns the difference between x and y
    return x - y

def mul(x, y):
    # Returns the product of x and y
    return x * y

def div(x, y):
    # Handles and prevents division by zero
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

# User Interface (UI) Introduction messages
print("Simple Python Calculator")
print("Welcome to the Simple Python Calculator.")
print("Please select an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# Takes input from the user to choose an operation
choice = input("Enter choice (1/2/3/4): ")

# Checks if th user made a valid choice
if choice in ['1', '2', '3', '4']:
    try:
        # Takes input from the user and converts to floats
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Performs the operation based on choice
        if choice == '1':
            print("Result: ", add(num1, num2))
        elif choice == '2':
            print("Result: ", sub(num1, num2))
        elif choice == '3':
            print("Result: ", mul(num1, num2))
        elif choice == '4':
            print("Result: ", div(num1, num2))
    except ValueError:
        # Handles when the user types non-numbers
        print("Error: Please enter valid numbers.")
else:
    # Handles invalid operation choice
    print("Invalid choice.")



# Uncomment this whole block to use a loop version
# Comment out the lines 21 - 53 by highlighting, then press Ctrl + / to comment out. Uncomment the section below by doing the same thing

# while True:
#     print("\nSimple Python Calculator")
#     print("Please select an operation:")
#     print("1. Add (+)")
#     print("2. Subtract (-)")
#     print("3. Multiply (*)")
#     print("4. Divide (/)")
#     print("5. Exit")

#     choice = input("Enter choice (1/2/3/4/5): ")

#     if choice == '5':
#         print("Goodbye!")
#         break  # Exit the loop

#     if choice in ['1', '2', '3', '4']:
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))

#             if choice == '1':
#                 print("Result: ", add(num1, num2))
#             elif choice == '2':
#                 print("Result: ", sub(num1, num2))
#             elif choice == '3':
#                 print("Result: ", mul(num1, num2))
#             elif choice == '4':
#                 print("Result: ", div(num1, num2))
#         except ValueError:
#             print("Error: Please enter valid numbers.")
#     else:
#         print("Invalid choice.")
