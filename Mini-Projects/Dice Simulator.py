import numpy as np

# Define ASCII Art for Dice Faces
dice_faces = {
    1: """
     -----
    |     |
    |  o  |
    |     |
     -----
    """,
    2: """
     -----
    | o   |
    |     |
    |   o |
     -----
    """,
    3: """
     -----
    | o   |
    |  o  |
    |   o |
     -----
    """,
    4: """
     -----
    | o o |
    |     |
    | o o |
     -----
    """,
    5: """
     -----
    | o o |
    |  o  |
    | o o |
     -----
    """,
    6: """
     -----
    | o o |
    | o o |
    | o o |
     -----
    """
}

def roll_dice():
    """Roll a 6-sided die using NumPy."""
    return np.random.randint(1, 7)  # Generates a number from 1 to 6

def play_game():
    while True:
        input("\nPress ENTER to roll the dice...")  # Wait for user input

        # Roll the dice for Player and Computer
        player_roll = roll_dice()
        computer_roll = roll_dice()

        # Display Dice Faces
        print("\n You rolled:\n", dice_faces[player_roll])
        print(" Computer rolled:\n", dice_faces[computer_roll])

        # Determine Winner
        if player_roll > computer_roll:
            print(" You WIN!")
        elif player_roll < computer_roll:
            print(" Computer WINS!")
        else:
            print(" It's a DRAW!")

        # Ask to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! ")
            break

# Run the Game
play_game()