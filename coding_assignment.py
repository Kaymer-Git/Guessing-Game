# import the method random
import random
# Generate a random interger nuumber between 1~10(inclusive)
random_number = random.randint(1, 10)

# Create a new list for 
previous_guesses = []

# Users guesses
attempts = 5

# Tell the user they have 5 attempts
print("You have", attempts, "attempts.")

# Ask the user to guess
user_guess = int(input("Enter a number between 1 - 10: "))

# Check if the number is in range
# Make the user keep guessing untill the number is in range
def guess_in_range(user_guess):
    # Make sure the user guess is in range
    while user_guess <= 0 or user_guess > 10:
        # Print "invalid input"
        print("Invalid input!")
        # Tell the user how many tries they have left
        print("You still have", attempts, "attempts.")
        # Ask the user to guess again when the number is out of range
        user_guess = int(input("Enter a number between 1 - 10: "))
    # Return the users guess
    return user_guess
# Make sure the user does not enter a duplicate number
def dup_guess(user_guess, previous_guesses):
    # Do Not Allow Duplicate Guesses
    while user_guess in previous_guesses:
        # Tell the user they guessed thenumber already
        print("You already guessed " + str(user_guess) + "!")
        # Ask the user to change a number
        print("Choose a different number.")
        # Give the user their previous guess
        print(previous_guesses)
        # Tell the user how many tries they have left
        print("You still have", attempts, "attempts.")
        # Let the user enter a new number again
        user_guess = int(input("Enter a number between 1 - 10: "))
    # return the user input
    return user_guess

# Keep comparing the guess with the number while they are not the same
while user_guess != random_number:
    # Check if the gues is in range
    user_guess = guess_in_range(user_guess)
    # Check if the guess is duplicate
    user_guess = dup_guess(user_guess, previous_guesses)
    # Add the guess to the list
    previous_guesses.append(user_guess)
    # Use 1 attempts
    attempts -= 1
    # Tell the user how many attempts they have left
    print("You have", attempts, "attempts left.")
    # Check if the user used all of their attempts
    if attempts == 0:
        # Tell the user the correct number
        print("The correct number is", random_number)
        # Tell the user the game is over
        print("Game over!")
        # Break out of the while loop
        break
    # Give the user their previous guess
    print(previous_guesses)
    # If the user guess is high
    if user_guess > random_number:
        # Tell the user to guess lower
        print("Try again! The random number is lower!")
        # Let the user type again
        user_guess = int(input("Enter a number between 1 - 10: "))
    # else if the user number is low
    elif user_guess < random_number:
        # Tell the user to guess higher
        print("Try again! The random number is higher!")
        # Let the user to guess again
        user_guess = int(input("Enter a number between 1 - 10: "))
# If they did not use all their guesses
if attempts > 0:
    # Tell the user they got the answer corrctly
    print("You guessed correctly! The number was ", random_number)
    # Print out the users previous guesses
    print(previous_guesses)
