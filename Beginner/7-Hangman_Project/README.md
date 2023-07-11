# Hangman Game

This is a simple implementation of the classic Hangman game in Python.

## How to Play

1. The game will randomly choose a word from a predefined word list.
2. The player's goal is to guess the letters in the word and complete it before running out of lives.
3. The player starts with 6 lives. For each incorrect guess, they lose a life.
4. If the player guesses a correct letter, it will be revealed in the word.
5. If the player guesses all the letters in the word before running out of lives, they win.
6. If the player runs out of lives before guessing all the letters, they lose.

## Prerequisites

- Python 3.x

## Getting Started

1. Clone the repository or download the `hangman.py` file.
2. Run the `hangman.py` file using the Python interpreter.

## Gameplay Instructions

1. The game will display the initial state of the hangman and the blank spaces for the word to guess.
2. Enter a letter as your guess and press enter.
3. If the letter is correct, it will be revealed in the word.
4. If the letter is incorrect, you will lose a life.
5. Keep guessing letters until you win or lose.
6. After each guess, the current state of the hangman and the word will be displayed.
7. If you win, a victory message will be displayed.
8. If you lose, a losing message will be displayed.

## Customization

You can customize the game by modifying the following variables in the `hangman.py` file:

- `word_list`: Contains the words that can be chosen for the game.
- `stages`: Contains the ASCII art representation of the hangman at different stages.
- `lives`: Specifies the number of lives the player starts with.

