import random
from replit import clear
from art import logo

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list_of_cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Special case: If the sum of the cards is 21 and there are only 2 cards, it's a Blackjack (ace + 10-value card).
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    # If the sum is greater than 21 and there is an ace (11-value card), convert it to 1 to avoid busting.
    if sum(list_of_cards) > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)

def compare(user_score, computer_score):
    """Compares the user's and computer's scores and returns the result of the game."""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    """Main function to play the Blackjack game."""

    print(logo)
    user_card = []
    computer_card = []
    game_over = False

    # Deal two cards to the user and computer.
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_over:
        # Calculate scores for the user and computer.
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        # Check if the game should end (user got a Blackjack, computer got a Blackjack, or user busted).
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Ask the user if they want another card or want to pass.
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_card.append(deal_card())
            else:
                game_over = True

    # Computer's turn to draw cards if needed.
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    # Display the final hands and scores and the result of the game.
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Start the game when the user wants to play.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
