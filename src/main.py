#This is a simplified version of the Blackjack game.
#Inspired by the Udemy Course 100 Days of Code

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

#Returns a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#Takes a list of cards as input and returns the score
def calculate_score(card_list):
    score = sum(card_list)
    #Checks for a blackjack - returns 0 instead of the actual score
    if score == 21 and len(card_list) == 2:
        return 0
    #Checks for an ace - if the score is over 21, replace it with a 1
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

#Compares the user score to the computer score
#Takes in the user score and computer score
#Returns the result of the game
def compare(user, computer):
    if user == computer:
        return "Draw!"
    elif computer == 0:
        return "Lose, opponent has blackjack!"
    elif user == 0:
        return "You win with a blackjack!"
    elif user > 21:
        return "You went over. You lose!"
    elif computer > 21:
        return "Computer went over. You win!"
    elif user > computer:
        return "You win!"
    else:
        return "You lose!"
    

#Plays a single game
def play_game():
    print(logo)

    computer_cards = []
    user_cards = []
    end_of_game = False

    #Deal the user and computer two cards at the beginning of each game
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    #Repeatedly calculates the score until the user has finished 
    while not end_of_game:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tcomputer's first card: {computer_cards[0]}")

        #If the computer or the user has a blackjack or if the user's score is over 21, then the game ends already
        if computer_score == 0 or user_score == 0 or user_score > 21:
            end_of_game = True
        #If the game is not over, ask the user if they want another card
        else:
            another = input("Type 'y' to get another card, type 'n' to pass: ")
            if another == "y":
                user_cards.append(deal_card())
            else:
                end_of_game = True
       
    #Repeatedly deals card to computer and calculates score until it reaches the minumum score of 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")

    print("-------------------------------------------------------------")
    print(compare(user_score, computer_score))
    print("-------------------------------------------------------------")

#Asks if the user wants to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

