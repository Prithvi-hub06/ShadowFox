import random

words = ["python", "developer", "hangman", "programming", "shadowfox"]

def play_game():
    chosen_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6

    print("\n🎮 Welcome to Hangman!")

    while wrong_guesses < max_attempts:
        # Display word
        display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print("\nWord:", display)
        print("Wrong guesses left:", max_attempts - wrong_guesses)

        # Check win
        if all(letter in guessed_letters for letter in chosen_word):
            print("🎉 Congratulations! You won!")
            break

        # User input
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        # Check guess
        if guess in chosen_word:
            guessed_letters.append(guess)
            print("✅ Correct guess!")
        else:
            guessed_letters.append(guess)
            wrong_guesses += 1
            print("❌ Wrong guess!")

    # Loss condition
    if wrong_guesses >= max_attempts:
        print("💀 You lost! The word was:", chosen_word)


# Game Loop for Play Again
while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing!")
        break