# Generate a Random Number
import random
random_number = random.randint(1, 10)

# Create a List for Previous Guesses
previous_guesses = []

# Ask the User to Guess
user_guess = int(input("Enter a number between 1 - 10: "))

#Validate the Number Range
while user_guess <= 0 or user_guess > 10:
    print("Invalid input!")
    user_guess = int(input("Enter a number between 1 - 10:"))

# Do Not Allow Duplicate Guesses
for p in previous_guesses:
    if user_guess == p:
        print("You already guessed " + str(user_guess) + "!")
        print("Choose a different number.")
        print("")
        print("Previous guesses: " + str(previous_guesses))

# Add the New Guess to the List
previous_guesses.append(user_guess)