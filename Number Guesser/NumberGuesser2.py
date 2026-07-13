import random


def game():
    while True:  # Picking the range
        try:
            lower_number = int(input("Enter the lower number for the range: "))
            higher_number = int(
                input("Enter the higher number for the range: "))

            if lower_number < 0 or higher_number < 0:
                print("Make sure your number is greater than 0.")
            elif higher_number - lower_number <= 1:
                print("Make sure there is atleast a 2 number gap between your numbers.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a proper number.")

    number_to_guess = random.randint(lower_number + 1, higher_number - 1)

    while True:  # Guessing part
        try:
            player_guess = int(input("Enter your guess 😀🫃 : "))

            if player_guess < lower_number or player_guess > higher_number:
                print("Please enter a value within the specified range.")
            elif player_guess > number_to_guess:
                print("Lower.")
            elif player_guess < number_to_guess:
                print("Higher.")
            else:
                print(f"Congrats you won! The number was {number_to_guess}")
                break
        except ValueError:
            print("Invalid input. Please enter a proper number.")


while True:  # Game loop
    game()
    retry = input("Do you want to play again? (y/n): ").strip().lower()
    if retry == 'y':
        print("Sure!")
    else:
        print("Thanks for playing! 🫃🙏😭🍆")
        break
