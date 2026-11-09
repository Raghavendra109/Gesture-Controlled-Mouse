
import random

# List of 5 predefined words
words = ["python", "linux", "cloud", "server", "coding"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("===== WELCOME TO HANGMAN GAME =====")

while incorrect_guesses < max_attempts:

    # Display guessed word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Attempts left:", max_attempts - incorrect_guesses)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    # Take user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
