import random

def wordle(secret_word, max_attempts=6):
    secret_word = secret_word.upper()
    word_length = len(secret_word)
    current_guess = ["#"] * word_length

    print("Word Guessing Game!")
    print("Guess the word: " + "".join(current_guess))

    for attempt in range(1, max_attempts + 1):
        guess = input(f"Attempt{attempt}/{max_attempts}: ").strip().upper()

        if len(guess) != word_length:
            print("Please only enter 5 word letter!")
            continue

        for i in range(word_length):
            if guess[i] == secret_word[i]:
                current_guess[i] = guess[i]

        print("Current progress:" + "".join(current_guess))

        if "".join(current_guess) == secret_word:
            print("Congrats! You guessed the word!")
            return

    print(f"Game over! The word was {secret_word}")

wordle("damper")

























