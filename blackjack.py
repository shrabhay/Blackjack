"""
This programs emulates a simple Blackjack game.
"""


import os
import random
from art import logo
os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """
    Returns a random card from the cards list.
    :return: random card
    """
    return random.choice(cards)


def calculate_score(cards_list):
    """
    Returns the sum of the items inside cards_list.
    :param cards_list: List containing cards.
    :return: Sum of the items inside cards_list.
    """
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare(users_score, dealers_score):
    """
    Compares the user's and the dealer's score and returns the result.
    :param users_score: User's final score
    :param dealers_score: Dealer's final score
    :return: Result
    """
    if users_score > 21 and dealers_score > 21:
        return "You went over. You lose 😤"

    if users_score == dealers_score:
        return "Draw 🙃"
    elif dealers_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif users_score == 0:
        return "Win with a Blackjack 😎"
    elif users_score > 21:
        return "You went over. You lose 😭"
    elif dealers_score > 21:
        return "Opponent went over. You win 😁"
    elif users_score > dealers_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def blackjack():
    print(logo)
    user_cards = []
    dealer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(cards_list=user_cards)
        dealer_score = calculate_score(cards_list=dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(cards_list=dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(users_score=user_score, dealers_score=dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system('clear')
    blackjack()
else:
    print("Goodbye!!!")
