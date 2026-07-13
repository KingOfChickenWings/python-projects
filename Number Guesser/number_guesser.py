import random


chicken = random.randint(1, 100)


while True:
    try:
        guessing = int(input("Guess the number between 1 and 100: "))
        if guessing > chicken:
            print("Too high")
        elif guessing < chicken:
            print("Too low")
        elif guessing == chicken:
            print("Congrats! You guessed the number")
            break
        else:
            print("Invalid answer")
    except ValueError:
        print("Please enter a valid number")
