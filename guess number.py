import random

def guess(x):
    random_number = random.randint(1, x) # random number chosen between 1 and number in () when calling the def
    guess = 0 # default to 0, chosen at random later
    while guess != random_number: # is not equal to
        guess = int(input(f"Guess a number between 1 and {x}: ")) # user picks # between 1 and x
        if guess < random_number: # if
            print("Sorry, guess is too low") # will print if user # too low
        elif guess > random_number:
            print("Sorry, guess is too high") # will print if user # too high

    print(f"You have guess the correct number: {random_number}") # prints when correct # is guessed by user


guess(1000) # calling the def and choosing the max random number in ()