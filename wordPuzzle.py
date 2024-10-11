#Santos Israel


def word_guessing_game():
    # Palabra secreta
    secret_word = "mosiah"
    secret_word_lower = secret_word.lower()  # Aseguramos que la palabra secreta esté en minúsculas
    max_guesses = 10  # Limitar el número de intentos
    attempts = 0  # Contador de intentos

    print("Welcome to the word guessing game!")
    hint = "_ " * len(secret_word)
    print(f"Your hint is: {hint.strip()}")

    while attempts < max_guesses:
        guess = input("What is your guess? ").strip().lower()
        attempts += 1

        # Verifica si la longitud de la suposición es correcta
        if len(guess) != len(secret_word_lower):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            continue

        # Genera la pista
        hint_list = []
        for i in range(len(secret_word_lower)):
            if guess[i] == secret_word_lower[i]:
                hint_list.append(guess[i].upper())  # Letra en la posición correcta
            elif guess[i] in secret_word_lower:
                hint_list.append(guess[i])  # Letra en la palabra pero en la posición incorrecta
            else:
                hint_list.append("_")  # Letra no presente

        hint = " ".join(hint_list)  # Convertir la lista de pistas a string
        print(f"Your hint is: {hint}")

        # Verifica si la suposición es correcta
        if guess == secret_word_lower:
            print(f"Congratulations! You guessed it!")
            print(f"It took you {attempts} guesses.")
            break
    else:
        print(f"Sorry, you've used all your guesses. The secret word was '{secret_word}'.")
# Llama a la función para iniciar el juego
word_guessing_game()
 