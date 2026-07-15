import random

money = int(input("Amount Of Money To Be Gambled: "))
numbers_thing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gamble_stuff = input("Odd Or Even: ")
cap_gamble = gamble_stuff.upper()   #Capitalizes the answer
numbers_random = random.choice(numbers_thing)   #Chooses a random number from the array 'numbers_thing'

if numbers_random % 2 == 1:
    print(numbers_random)
    if cap_gamble == "ODD":
        print(f"You won {money * 2}!")
    else:
        print(
            f"You lost your {money}!")
elif numbers_random % 2 == 0:
    print(numbers_random)
    if cap_gamble == "EVEN":
        print(f"You won {money * 2}!")
    else:
        print(
            f"You lost your {money}!")
else:
    print("Please enter a valid number...")
