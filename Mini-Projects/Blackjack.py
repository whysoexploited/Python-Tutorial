# deck is unlimited in size
# no jokers
# the jack/q/k are all 10
# the ace can count as 11 or 1
# the cards have equal probability of being drawn
# cards not removed from the deck as they are being drawn
# PC is the dealer
# cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


import random
from art import logoPoker

cards = (11, 2, 3, 4, 5, 6 ,7 , 8, 9, 10, 10, 10, 10)

def dealer_draw_cards():
    dealer_hand = [random.choice(cards), random.choice(cards)]
    print(f"Computer's first hand: {dealer_hand[0]}")
    dealer_total = sum(dealer_hand)

    while  dealer_total < 17:
        new_card = random.choice(cards)
        dealer_hand.append(new_card)
        dealer_total = sum(dealer_hand)

        while dealer_total > 21 and 11 in dealer_hand:
            dealer_hand[dealer_hand.index(11)] = 1
            dealer_total = sum(dealer_hand)

    return  dealer_hand, dealer_total

#def player_draw_cards():

def player_draw_cards():
    player_hand = [random.choice(cards), random.choice(cards)]
    player_total = sum(player_hand)

    while player_total < 21:

        print(f"Hand: {player_hand}. with a total of: {player_total}")
        player_input = input(f"Do you want to draw another card? (Y/N): ").strip().lower()

        if player_input == "y":
            new_card = random.choice(cards)  # Draw a new card
            player_hand.append(new_card)  # Add new card to the hand
            player_total = sum(player_hand)  # Update total after drawing

            while player_total > 21 and 11 in player_hand:
                player_hand[player_hand.index(11)] = 1
                player_total = sum(player_hand)

        elif player_input == "n":
            print(f"Stay with: {player_total}!")
            break  # Exit the loop when the player decides to stay

        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

    return player_hand, player_total



def play_game():
    """ Function that runs the game"""
    print(logoPoker)
    dealer_hand, dealer_total = dealer_draw_cards()
    player_hand, player_total = player_draw_cards()
    if player_total > 21:
        print(f"Player is busted with: {player_total}. Dealer wins!")
    elif dealer_total > 21:
        print(f"Dealer is busted with: {dealer_total}. Player wins!")
    elif player_total > dealer_total:
        print(f"Player drawn: {player_total}, against dealer's: {dealer_total} Player wins!")
    elif player_total < dealer_total:
        print(f"Dealer drawn: {dealer_total}, against player's: {player_total} a Dealer wins!")
    else:
        print(f"It's a tie! Both drawn: {player_total}!")


while True:  # Keeps looping until user decides to quit
    play_game()

    user_choice = input("Do you want to play another game? (Y/N): ").strip().lower()

    if user_choice == "n":
        print("Thanks for playing! Goodbye! ")
        break  # Exit the loop and stop the game
    elif user_choice != "y":
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

