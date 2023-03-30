# Python Number Guessing Game

import random

game_over = False  # To check if out of guesses.
guesses = 0  # Set value for guesses


def play_again():
    """Function to reset game"""
    global game_over
    if again == 'y':
        game_over = False


def check_num():
    """Function to check if guess is correct, if not tell high or low."""
    global guesses
    global game_over
    if current_guess > 100 or current_guess < 1:
        print("You number is not in range.")
    elif current_guess == secret_number:
        print("You are correct!")
        game_over = True
    elif current_guess < secret_number:
        print("That is too low.")
    elif current_guess > secret_number:
        print("That is too high.")


while not game_over:
    # Pick random number between 1 - 100 for player to guess.
    secret_number = random.randint(1, 100)

    # Ask if easy or hard mode, set guesses hard = 5, easy = 10.
    mode = input("Do you wish to play on Easy 'e' or Hard 'h' mode?: ")
    if mode == "e":
        guesses = 10
    elif mode == "h":
        guesses = 5

    # Ask player to guess a number
    current_guess = int(input("What number do you guess?: "))

    while guesses > 0:
        check_num()
        guesses -= 1
        if game_over:
            again = input("Do you wish to play again?: ")
            play_again()
            break
        # Tell number of remaining guesses and ask for new guess.
        current_guess = int(input(f"You have {guesses} guesses remaining. Pick another number.: "))
