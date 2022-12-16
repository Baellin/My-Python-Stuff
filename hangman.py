import random
import string

def get_valid_word(words):
    word = random.choice(words)  # gets a word from the list
    return word.upper()


def hangman():
    words = ["adrift", "apes", "atrophy", "ablaze", "computer", "hardware", "software", "friends", "programming",
             "zebra"]
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word chosen
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # tracks what user has guessed

    lives = 6

    # user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'c']) -> 'a b c'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have guessed that letter already, please enter a new letter:')

        else:
            print('Invalid character, try again:')

    if lives == 0:
        print('You have died, the word was', word)
    else:
        print('You guessed the word', word, '!!')

hangman()
