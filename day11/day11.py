import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.append(1)
        cards.remove(11)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose!, Computer has blackjack"
    elif u_score == 0:
        return "User wins, user has blackjack!"
    elif u_score > 21:
        return "Computer wins!"
    elif c_score > 21:
        return "User wins!"
    elif u_score > c_score:
        return "User wins!"
    elif c_score > u_score:
        return "Computer wins!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards},Your score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            print("Computer wins!")
            is_game_over = True
        else:
            user_should_deal = input("Types y to get another card or type n to no: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards},Your final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, Computer final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play an game of blackjack, y or n? ") == "y":
    print("\n" * 20)
    play_game()
