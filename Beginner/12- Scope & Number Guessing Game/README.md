Certainly! Here's a README.md file for the Number Guessing Game:

# Number Guessing Game

A simple command-line-based Number Guessing Game implemented in Python. The game generates a random number between 1 and 100, and the player has to guess the number within a limited number of attempts based on the chosen difficulty level.

## How to Play

1. Clone the repository to your local machine.

2. Make sure you have Python installed. This project was developed using Python 3.x.

3. Run the game by executing the `main.py` file:
   ```
   python main.py
   ```

4. The game will prompt you to choose the difficulty level: 'easy' or 'hard'.
   - 'easy': You have 10 attempts to guess the number.
   - 'hard': You have 5 attempts to guess the number.

5. After choosing the difficulty, the game will display the logo and initial instructions, asking you to guess a number between 1 and 100.

6. Enter your guess. The game will provide feedback on whether your guess is too high, too low, or correct. The remaining attempts will be displayed.

7. Keep guessing until you either guess the correct number or run out of attempts.

8. The game will display the result, informing you if you won or lost.

## Functionality

The game consists of the following Python functions:

1. `set_difficulty()`: This function asks the user to choose the difficulty level ('easy' or 'hard') and returns the number of turns based on the chosen difficulty.

2. `compare(guess, actual_answer, turns)`: This function compares the user's guess with the actual answer and provides feedback. It also reduces the number of turns remaining if the guess is incorrect.

3. `game()`: The main function to play the Number Guessing Game. It displays the logo, initial instructions, and handles the game loop until the user guesses the correct number or runs out of turns.

