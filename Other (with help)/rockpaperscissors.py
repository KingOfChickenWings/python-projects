import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

emoji_thing = {ROCK: '🗿', SCISSOR: '✂️', PAPER: '📄'}
choices = (tuple(emoji_thing.keys()))


def get_user_choice():  # Gets the choice of user and returns value
    while True:
        user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()

        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")


# Function to display user and computer choice
def display_choices(user_choice, computer_choice):
    print(f"You chose {emoji_thing[user_choice]}")
    print(f"Computer chose {emoji_thing[computer_choice]}")


# Function to determine the winner
def determining_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Its a tie!")
    elif (
            user_choice == ROCK and computer_choice == SCISSOR or
            user_choice == SCISSOR and computer_choice == PAPER or
            user_choice == PAPER and computer_choice == ROCK):
        print("You Win!!")
    else:
        print("You lose 😓")


def play_game():  # Function that runs the game
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determining_winner(user_choice, computer_choice)

        should_continue = input("Do you want to continue? (y/n): ").lower()

        if should_continue == 'n':
            break


play_game()
