"""
ShadowFox Python Development Internship
Task 2 (Intermediate) - Hangman
Author: Shaik Sadiya Kousar

A word-guessing game with visual progress (ASCII hangman figure) and hints.
"""

import random

# Word bank: word -> hint
WORD_BANK = {
    "python": "A popular programming language named after a snake",
    "keyboard": "You type on this",
    "internship": "What you're currently doing at ShadowFox",
    "elephant": "The largest land animal",
    "guitar": "A musical instrument with strings",
    "planet": "Earth is one of these",
    "umbrella": "You use this when it rains",
}

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """,
]


def choose_word():
    word = random.choice(list(WORD_BANK.keys()))
    hint = WORD_BANK[word]
    return word, hint


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word, hint = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0

    print("=" * 50)
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print("=" * 50)

    while incorrect_guesses < MAX_ATTEMPTS:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word:", display_word(word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_ATTEMPTS}")
        print(f"Guessed letters so far: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Win condition check
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

        guess = input("\nGuess a letter (or type 'hint' for a clue): ").strip().lower()

        if guess == "hint":
            print(f"Hint: {hint}")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess. '{guess}' is not in the word.")

    # Loss condition
    print(HANGMAN_STAGES[MAX_ATTEMPTS])
    print(f"\nGame over! The word was: {word}")


def play_again():
    choice = input("\nPlay again? (yes/no): ").strip().lower()
    return choice in ("yes", "y")


if __name__ == "__main__":
    while True:
        play_hangman()
        if not play_again():
            print("Thanks for playing Hangman! Goodbye.")
            break
