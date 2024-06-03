import random

def select_random_word():
    word_list = ["python", "hangman", "challenge", "programming", "development", "artificial", "intelligence"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def play_hangman():
    word = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("You have {} incorrect guesses allowed.".format(max_incorrect_guesses))
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            incorrect_guesses += 1
            print("Incorrect guess. You have {} guesses left.".format(max_incorrect_guesses - incorrect_guesses))

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You've guessed the word: {}".format(word))
            break
    else:
        print("Sorry, you've run out of guesses. The word was: {}".format(word))

play_hangman()