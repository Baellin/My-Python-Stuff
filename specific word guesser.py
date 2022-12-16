def guessing_game():
    secret_word = "plank" # stating the word to be guessed
    guess = ""
    guesses = 0
    guesses_limit = 5
    out_of_guesses = False

    while guess != secret_word and not out_of_guesses: # as long as the word input does not equal the secret_word stated above, will continue guessing until guesses_limit reached
        if guesses < guesses_limit:
            guess = input("Enter a word: ") # input a word
            guesses += 1
        else:
            out_of_guesses = True
    if out_of_guesses: # after guess limit reached without guessing correctly
        input("You lost")
        return guessing_game()
    else: # guessing the word correctly
        print("You guessed the word!")


guessing_game()