import random # Import random module to generate random numbers

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")

# Generates a random value between 1 and 100
number = random.randint(1, 100) # Change the values if you want a smaller or bigger range

# Initialize guess count
guess_count = 0

while True:
    try:
        # User input
        guess = int(input("Enter your guess: "))
        guess_count += 1 # Counts how many guesses the user makes

        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Correct! The number was {number}")
            print(f"You guessed it in {guess_count} tries.")
            break # Exits the loop when guessed correctly
    except ValueError:
        # Handles non-integers
        print("Please enter a valid number")
