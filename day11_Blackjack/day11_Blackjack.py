import random, art

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(deck):
    """Calculates the total score from the deck at hand"""
    if sum(deck)==21 and len(deck)==2:
        return 0
    if sum(deck) > 21 and 11 in deck:
            deck.remove(11)
            deck.append(1)
    return sum(deck)

def compare(my_score, computer_score):
    if my_score==computer_score:
        return "It's a draw."
    elif computer_score==0:
        return "You lose. Opponent has blackjack."
    elif my_score==0:
        return "You win with blackjack."
    elif my_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif my_score > computer_score:
        return "You win."
    else:
        return "You lose"

def play_game():
    print(art.logo)

    my_card = []
    computer_card = []
    game = True
    computer_score = -1
    my_score = -1
    
    for i in range(2):
        my_card.append(deal_card())
        computer_card.append(deal_card())

    while game:
        my_score = calculate_score(my_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {my_card}, current score: {my_score}")
        print(f"Computer's first card: {computer_card[0]}")
        
        if my_score==0 or computer_score==0 or my_score > 21:
            game = False
        else:
            y_or_n = input("Type 'y' to get another card, type 'n' to pass: ")
            if y_or_n=="y":
                    my_card.append(deal_card())
            else:
                game = False
    
    while computer_score < 17 and computer_score != 0:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {my_card}, final score: {my_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(my_score, computer_score))

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play=="y":
    play_game()
    