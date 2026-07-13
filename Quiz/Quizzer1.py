def questions_thing(questions):
    for question in questions:
        print(question["question"])
        print(question["options"])

        answer = input().lower().strip()

        if answer in question["answers"]:
            print("Correct answer!")
        else:
            print("Wrong!")
        print()


def game():
    while True:
        try:
            play = int(input(
                "Choose one of the following-> Math, Science, Computer (1,2,3): "))
            if play not in [1, 2, 3]:
                print("Please enter a number between 1 and 3...")
            else:
                return play
        except ValueError:
            print("Enter a valid number (1,2,3).")


# ------------------------------------------------------


def quiz_math():
    questions_math = [
        {
            "question": "7 x 8 = ?",
            "options": ["A. 54", "B. 56", "C. 64", "D. 58"],
            "answers": ["b", "56"]
        },
        {
            "question": "√81 = ?",
            "options": ["A. 7", "B. 8", "C. 9", "D. 10"],
            "answers": ["c", "9"]
        },
        {
            "question": "π ≈ ?",
            "options": ["A. 3.14", "B. 2.71", "C. 1.41", "D. 1.73"],
            "answers": ["a", "3.14"]
        }
    ]

    questions_thing(questions_math)


# ------------------------------------------------------


def quiz_science():
    questions_science = [
        {
            "question": "H₂O is?",
            "options": ["A. Oxygen", "B. Water", "C. Hydrogen", "D. Helium"],
            "answers": ["b", "water"]
        },
        {
            "question": "Planet?",
            "options": ["A. Sun", "B. Moon", "C. Earth", "D. Star"],
            "answers": ["c", "earth"]
        },
        {
            "question": "Gas?",
            "options": ["A. Iron", "B. Oxygen", "C. Gold", "D. Copper"],
            "answers": ["b", "oxygen"]
        }
    ]

    questions_thing(questions_science)


# ------------------------------------------------------


def quiz_cs():
    questions_cs = [
        {
            "question": "CPU stands for?",
            "options": [
                "A. Central Process Unit",
                "B. Central Processing Unit",
                "C. Computer Processing Unit",
                "D. Core Processing Unit"
            ],
            "answers": ["b", "central processing unit"]
        },
        {
            "question": "Python is a?",
            "options": ["A. Browser", "B. Language", "C. Hardware", "D. Virus"],
            "answers": ["b", "language"]
        },
        {
            "question": "RAM is?",
            "options": ["A. Storage", "B. Memory", "C. Processor", "D. Monitor"],
            "answers": ["b", "memory"]
        }
    ]

    questions_thing(questions_cs)


# ------------------------------------------------------


while True:
    happy = input("Do you want to play? (y/n): ").lower().strip()

    if happy != "y":
        print("Aight cya!")
        break

    play = game()

    if play == 1:
        quiz_math()
    elif play == 2:
        quiz_science()
    else:
        quiz_cs()
