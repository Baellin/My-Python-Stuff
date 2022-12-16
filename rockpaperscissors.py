import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n") # ask user to choose
    computer = random.choice(['r', 'p', 's']) # computer auto choose 1 of 3

    if user == computer: # if user and computer choose same, tie
        print("The computer chose: " + computer)  # prints what computer chose
        return "You tie"

    if is_win(user, computer):  # if user beats computer
        return "You win"

    return "You lose"  # if neither the other return statements are true, you lose


def is_win(player, opponent):  # defining how the player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r'):  # methods of user beating computer
        return True  # when true, above if statement is_win becomes true


print(play())  # prints the play function to play the game