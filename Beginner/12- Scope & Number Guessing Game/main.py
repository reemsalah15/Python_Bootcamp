from art import logo
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    # Ask the user to choose the difficulty level: 'easy' or 'hard'.
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    # Return the number of turns based on the chosen difficulty.
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def compare(guess, actual_answer, turns):
    # Compare the user's guess with the actual answer.
    if guess < actual_answer:
        print("Too Low")
        # Reduce the number of turns remaining if the guess is too low.
        return turns - 1
    elif guess > actual_answer:
        print("Too High")
        # Reduce the number of turns remaining if the guess is too high.
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

def game():
    # Display the game logo and initial instructions.
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100 as the answer to guess.
    actual_answer = randint(1, 100)
    
    # Set the initial number of turns based on the chosen difficulty.
    turns = set_difficulty()
    
    # Initialize the user's initial guess.
    guess = 0

    # Start the game loop until the user guesses the correct answer or runs out of turns.
    while guess != actual_answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Ask the user to enter their guess.
        guess = int(input("Make a guess: "))
        # Compare the user's guess with the actual answer and update the turns accordingly.
        turns = compare(guess, actual_answer, turns)

        # Check if the user has run out of turns and print the result.
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != actual_answer:
            print("Guess again.")

# Start the game by calling the game() function.
game()
