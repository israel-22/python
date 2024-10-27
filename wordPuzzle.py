import random

# For Bryan Chavez
#////////////////////////////////////////////////////////////////////////////////////////////
# Welcome to the word guessing game!
# Instructions: You will be given a word, represented by underscores. You have to guess the word
# by entering guesses. You will have 10 attempts to guess the correct word.
# Each time you guess, a hint will be provided.
# An uppercase letter in the hint indicates a correct letter in the correct position,
# a lowercase letter indicates the letter exists in the word but is in the wrong position,
# and an underscore means the letter is not in the word at all.
# After the game ends, you can
#  choose to play again or exit.
# Enjoy the game and good luck!
#ghthttt

# Main function for the word guessing game
def word_guessing_game():
    # List of secret words
    secret_words = ["mosiah", "temple", "moroni", "nephi", "helaman", "alma", "lehi"]
    
    while True:
        # Randomly select a secret word
        secret_word = random.choice(secret_words)
        secret_word_lower = secret_word.lower()  # Ensure the secret word is in lowercase
        max_guesses = 10  # Limit the number of attempts
        attempts = 0  # Counter for attempts

        print("\nWelcome to the word guessing game!")
        print("Instructions: Try to guess the word. You have 10 attempts. Hints will be provided as you guess.")
        hint = "_ " * len(secret_word)
        print(f"Your hint is: {hint.strip()}")

        while attempts < max_guesses:
            guess = input("What is your guess? ").strip().lower()
            attempts += 1

            # Check if the guess length is correct
            if len(guess) != len(secret_word_lower):
                print("Sorry, the guess must have the same number of letters as the secret word.")
                continue

            # Generate the hint
            hint_list = []
            for i in range(len(secret_word_lower)):
                if guess[i] == secret_word_lower[i]:
                    hint_list.append(guess[i].upper())  # Letter in the correct position
                elif guess[i] in secret_word_lower:
                    hint_list.append(guess[i])  # Letter in the word but in the wrong position
                else:
                    hint_list.append("_")  # Letter not present

            hint = " ".join(hint_list)  # Convert the hint list to a string
            print(f"Your hint is: {hint}")

            # Check if the guess is correct
            if guess == secret_word_lower:
                print(f"Congratulations! You guessed it!")
                print(f"It took you {attempts} guesses.")
                break
        else:
            print(f"Sorry, you've used all your guesses. The secret word was '{secret_word}'.")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Call the function to start the game
word_guessing_game()
