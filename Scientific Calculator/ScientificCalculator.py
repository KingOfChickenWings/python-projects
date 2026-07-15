import math
# =================================


def addition(numbers):
    final_answer = 0
    for number in numbers:
        final_answer += number
    return final_answer
# =================================


def subtraction(numbers):
    final_answer = numbers[0]
    for number in numbers[1:]:
        final_answer -= number
    return final_answer
# =================================


def multiplication(numbers):
    final_answer = 1
    for number in numbers:
        final_answer *= number
    return final_answer
# =================================


def division(numbers):
    final_answer = numbers[0]
    for number in numbers[1:]:
        final_answer /= number
    return final_answer
# =================================


def square_root(number):
    if number < 0:
        return f"({math.sqrt(abs(number))})i"
    else:
        return f"({math.sqrt(number)})"
# =================================


operations = {
    '+': addition,
    '-': subtraction,
    '/': division,
    '*': multiplication
}
# =================================
while True:
    numbers = []
    operation = input(
        "Enter operation (+, -, *, /, sqrt)(exit to stop): ").strip().lower()

    if operation == 'exit':
        break

    elif operation in ['+', '-', '*', '/']:
# ================================================================================================

        try:
            terms = int(input("Enter number of terms: "))

            if terms <= 0:
                print("Number of terms must be greater than 0...")
                continue

            for term in range(terms):
                current_term = float(input(f"Enter term {term + 1}: "))
                numbers.append(current_term)

            print(f"Your current numbers are -> {numbers}")

# =================================================================================

            final_answer = operations[operation](numbers)
            print(f"Your final answer is {final_answer}")

# ============================================================

        except ValueError:
            print("Please enter a valid number.")

        except ZeroDivisionError:
            print("Divisor cannot be zero.")
# ============================================================

    elif operation == 'sqrt':
        try:
            number = float(input("Enter your number: "))
            answer = square_root(number)
            print(f"The square root of your number is {answer}")

        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Please enter a valid operation.")
        continue
