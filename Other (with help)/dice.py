import random


def dice_roll():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return (a, b)


while True:
    roll_choice = input("Do you want to roll the dice?  (y/n): ").lower()

    if roll_choice == "y":
        print(dice_roll())
    elif roll_choice == "n":
        print("Aight cya")
        break
    else:
        print("Invalid Choice")
 