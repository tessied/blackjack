import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(card_list):
    score = sum(card_list)
    if score == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def compare(user, computer):
    if user == computer:
        return "Draw"
    elif computer == 0:
        return "Lose, opponent has blackjack"
    elif user == 0:
        return "Win with a blackjack"
    elif user > 21:
        return "You went over. You lose"
    elif computer > 21:
        return "Computer went over. You win"
    elif user > computer:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)

    computer_cards = []
    user_cards = []
    end_of_game = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not end_of_game:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tcomputer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            end_of_game = True
        else:
            another = input("Type 'y' to get another card, type 'n' to pass: ")
            if another == "y":
                user_cards.append(deal_card())
            else:
                end_of_game = True
       

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

