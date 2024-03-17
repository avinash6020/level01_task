
import random

def guess_the_number():
    # Step 1: Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 5  # Step 2: Initialize the number of attempts to 5

    print("Welcome to Guess the Number!")
    print("I've picked a number between 1 and 100. Can you guess it?")

    # Step 3: Start a loop for each attempt
    while attempts > 0:
        print("\nAttempts left:", attempts)
        guess = int(input("Enter your guess: "))

        # Step 3c: Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number:", secret_number)
            return  # End the game
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

        attempts -= 1  # Decrement the number of attempts left

    # Step 3d: Inform the player that the game is over
    print("\nGame over! You ran out of attempts.")
    print("The correct number was:", secret_number)

# Call the function to start the game
guess_the_number()
