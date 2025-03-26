from art import rockArt, paperArt, scissorsArt
import random

choice = [rockArt, paperArt, scissorsArt]


def computer_choice():
    """Function for computer choice."""
    return random.choice(choice)


def player_choice():
    """Function for player input."""
    player_input = input("Tell me your choice ---- (1-Rock, 2-Paper, 3-Scissors): ").strip()

    if player_input == "1":
        return rockArt
    elif player_input == "2":
        return paperArt
    elif player_input == "3":
        return scissorsArt
    else:
        print("Invalid input. Please use '1' --> Rock, '2' --> Paper or '3' --> Scissors")
        return None


def determine_winner(player, computer):
    """Function to determine the winner."""
    if player == computer:
        return "It's a tie!"
    elif (
        (player == rockArt and computer == scissorsArt) or
        (player == scissorsArt and computer == paperArt) or
        (player == paperArt and computer == rockArt)
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():

    """ Function that runs the game. """
    while True:
        user_input = input("Do you want to play a game ?. Enter 'Y' for Yes and 'N' for no: ").strip().upper()

        if user_input == "Y":
            player_result = player_choice()
            if player_result:
                print(f"You chose: {player_result}")
                computer_result = computer_choice()
                print(f"Computer chose: {computer_result}")
                print(determine_winner(player_result, computer_result))
        elif user_input == "N":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please use 'Y' for Yes and 'N' for No: ")


play_game()
