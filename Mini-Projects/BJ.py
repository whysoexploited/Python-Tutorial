# deck is unlimited in size
# no jokers
# the jack/q/k are all 10
# the ace can count as 11 or 1
# the cards have equal probability of being drawn
# cards not removed from the deck as they are being drawn
# PC is the dealer
# cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


import random

cards = (11, 2, 3, 4, 5, 6 ,7 , 8, 9, 10, 10, 10, 10)
cards_number = len(cards)
probability = ( 1 / cards_number ) * 100

def dealer_draw_cards():
    first_drawn_card = random.choice(cards)
    second_drawn_card = random.choice(cards)
    total = first_drawn_card + second_drawn_card

    while total < 17:
        new_card = random.choice(cards)
        total += new_card

    if total == 21:
        print("Blackjack! Dealer has: "  + str(total))
    elif total > 21:
        print("Dealer is busted: " + str(total))
    else:
        print("Dealer has: " + str(total))

    return total

def player_draw_cards():
    first_drawn_card = random.choice(cards)
    second_drawn_card = random.choice(cards)
    total = first_drawn_card + second_drawn_card

    while total < 21:
     print(f"You have: {total}")
    player_input = input("You have: " + str(total) + ". Do you want to draw another card? (Y/N): ").strip().lower()

    if player_input == "y":
        new_card = random.choice(cards)
        total += new_card
        elif player_input = "n":
        print(f"You choose to stay with:{total}")
        break

    else:
        print("Invalid input. Please use Y or N.")
    return total
def play_game():

    print(f.)
    dealer = dealer_draw_cards()
    player = player_draw_cards()

    if player > 21:
        print(f"Player is busted with: {player}. Dealer wins!")
    elif dealer > 21:
        print(f"Dealer is busted with: {dealer}. Player wins!")
    elif player > dealer:
        print(f"Player drawn: {player}, against dealer's: {dealer} Player wins!")
    elif player < dealer:
        print(f"Dealer drawn: {dealer}, against player's: {player} a Dealer wins!")
    else:
        print(f"It's a tie! Both drawn: {player}!")
play_game()

#INTREBARI LEO: Nu respecta code-ul egalitatea
#Rectificari:
# 1. Sa mai tragi o carte daca ai nevoie
# 2. Alege 1 sau 11 in cazul AS
# Copia exacta a jocului/sus e doar test.