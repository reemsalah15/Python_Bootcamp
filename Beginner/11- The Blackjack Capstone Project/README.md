# Python Blackjack Game

This is a simple command-line-based implementation of the classic Blackjack game using Python. The game allows you to play against a computer-controlled dealer. The rules are standard: get as close to 21 as possible without going over, and beat the dealer's hand.

## How to Play

1. Clone the repository to your local machine.

2. Make sure you have Python installed. This project was developed using Python 3.x.

3. Install the required dependencies:
   ```
   pip install replit
   ```

4. Run the game by executing the `blackjack.py` file:
   ```
   python blackjack.py
   ```

5. The game will prompt you to play by asking for input:
   - Type 'y' to get another card.
   - Type 'n' to pass and end your turn.

6. The computer will then play its turn, trying to reach a minimum score of 17.

7. The game will display the final hands and scores of both you and the computer, along with the result of the game.

## Functionality

The project consists of the following Python functions:

1. `deal_card()`: This function returns a random card from the deck (values 2-10, Jack, Queen, King, or Ace (which is 11)).

2. `calculate_score(list_of_cards)`: This function calculates the score of a list of cards and accounts for the special case of an Ace being worth 1 or 11 points.

3. `compare(user_score, computer_score)`: This function compares the user's and computer's scores and returns the result of the game.

4. `play_game()`: This function contains the game loop and manages the overall game flow, dealing cards to the user and computer, asking for input, and playing the computer's turn.

## Acknowledgments

This project was inspired by the "100 Days of Code - The Complete Python Pro Bootcamp for 2021" course on Udemy by Angela Yu.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to contribute, report issues, and have fun playing the game!