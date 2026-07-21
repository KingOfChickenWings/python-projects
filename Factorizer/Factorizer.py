import math
# =================================
# FUNCTIONS
# =================================


def complex_roots():
    print("The roots are complex and cannot be expressed in integer form.")


def repeated_roots(a, b):
    x1 = -b / (2 * a)

    if x1 < 0:
        sign = "+"
    else:
        sign = "-"

    if x1 % 1 == 0:
        print(f"The factorized form is -> (x {sign} {abs(int(x1))})²")
    else:
        numerator = abs(int(a * x1))
        denominator = abs(a)

        print(
            f"The factorized form is -> ({denominator}x {sign} {numerator})²")


def normal_roots(a, b, c, discriminant, sign):
    x1 = (-b + math.sqrt(discriminant))/(2*a)
    x2 = (-b - math.sqrt(discriminant))/(2*a)

    sign1 = "+" if x1 < 0 else "-"
    sign2 = "+" if x2 < 0 else "-"

    if x1 % 1 != 0 and x2 % 1 != 0:
        print(
            f"The factorized form of {a}x² {b}x {sign} {c} is -> ({a}x {sign1} {abs(a*(-x1))})({a}x {sign2} {abs(a*(-x2))})")

    elif x1 % 1 != 0:
        print(
            f"The factorized form of {a}x² {b}x {sign} {c} is -> ({a}x {sign1} {abs(a*(-x1))})(x {sign2} {-x2})")

    elif x2 % 1 != 0:
        print(
            f"The factorized form of {a}x² {b}x {sign} {c} is -> (x {sign1} {-x1})({a}x {sign2} {abs(a*(-x2))})")

    else:
        print(
            f"The factorized form of {a}x² {b}x {sign}{c} is -> (x {sign1} {abs(-x1)})(x {sign2} {abs(-x2)})")

# =================================
# MAIN PROGRAM
# =================================


while True:
    try:
        a = int(input("Enter the coefficient of x²: "))
        b = int(input("Enter the coefficient of x: "))
        c = int(input("Enter the constant term: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    discriminant = b**2 - 4*a*c
    if a == 0:
        print("The coefficient of x² cannot be 0")
        continue

    sign = '+' if c >= 0 else '-'

    if discriminant < 0:
        complex_roots()

    elif discriminant == 0:
        repeated_roots(a, b)

    elif (math.isqrt(discriminant))**2 != discriminant:
        print("The expression cannot be factorized in form of integers.")
        continue

    elif discriminant > 0:
        normal_roots(a, b, c, discriminant, sign)
