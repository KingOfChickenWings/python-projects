import math
# =================================
# FUNCTIONS
# =================================


def addition(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def subtraction(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result


def multiplication(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def division(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result /= number
    return result


def square_root(number):
    if number < 0:
        return f"({math.sqrt(abs(number))})i"
    else:
        return f"({math.sqrt(number)})"


def power(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result **= number
    return result


def modulus(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result %= number
    return result


def floor_division(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result //= number
    return result

# =================================


def factorial(number):
    return round(math.factorial(number))


def sine(number):
    return round(math.sin(math.radians(number)))


def cosine(number):
    return round(math.cos(math.radians(number)))


def tangent(number):
    return round(math.tan(math.radians(number)))


# =================================
operations = {
    '+': addition,
    '-': subtraction,
    '/': division,
    '*': multiplication,
    '^': power,
    '%': modulus,
    '//': floor_division
}

extra_operations = {
    'sqrt': square_root,
    'sin': sine,
    'cos': cosine,
    'tan': tangent
}
# =================================
# MAIN PROGRAM
# =================================
while True:
    numbers = []
    operation = input(
        "Enter operation (+, -, *, /, ^, %, //, !, sin, cos, tan, sqrt)(exit to stop): ").strip().lower()

    if operation == 'exit':
        break
# =================================

    elif operation == '!':
        try:
            number = int(input("Enter your number: "))
            answer = factorial(number)
            print(f"The factorial of your number is {answer}")
        except ValueError:
            print("Please enter a non-negative and non-decimal number.")

    elif operation in extra_operations:
        try:
            number = float(input("Enter your number: "))
            answer = extra_operations[operation](number)
            print(f"Your final answer is -> {answer}")

        except ValueError:
            print("Please enter a valid number.")

    elif operation in operations:
        # ================================================================================================

        try:
            terms = int(input("Enter number of terms: "))

            if terms <= 0:
                print("Number of terms must be greater than 0...")
                continue

            for term in range(terms):
                current_term = float(input(f"Enter term {term + 1}: "))
                numbers.append(current_term)

            print(f"Your numbers are -> {numbers}")

# =================================================================================

            result = operations[operation](numbers)
            print(f"Your final answer is {result}")

# ============================================================

        except ValueError:
            print("Please enter a valid number.")

        except ZeroDivisionError:
            print("Divisor cannot be zero.")
# ============================================================

    else:
        print("Please enter a valid operation.")
        continue
