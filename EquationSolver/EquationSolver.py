import math

# =================================
# Main program
# =================================

while True:
    try:
        degree = int(input("Enter the degree of your equation (1/2): "))
    except ValueError:
        print("Please enter a valid number. (1, 2)")
        continue

# =================================
# Linear
# =================================

    if degree == 1:
        while True:
            try:
                a = int(input("Enter the coefficient of x: "))
                b = int(input("Enter the coefficient on the left: "))
                c = int(input("Enter the coefficient on the right: "))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue
        if a == 0:
            print("The coefficient of x cannot be 0.")
        else:
            print(f"The value of x is {(c - b)/a}")
            break

# =================================
# Quadratic
# =================================

    elif degree == 2:
        while True:
            try:
                a = int(input("Enter the coefficient of x²: "))
                b = int(input("Enter the coefficient of x: "))
                c = int(input("Enter the Constant: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        discriminant = b**2 - 4*a*c

        if a == 0:
            print("The coefficient of x² cannot be zero")
            continue

        elif discriminant > 0:
            sqrt_discriminant = math.sqrt(discriminant)
            x2 = (-b - sqrt_discriminant)/(2*a)
            x1 = (-b + sqrt_discriminant)/(2*a)
            print(f"The values of x are {x1} and {x2}")

        elif discriminant == 0:
            x1 = (-b/(2*a))
            print(f"The repeated root is {x1}")

        else:
            sqrt_discriminant = math.sqrt(abs(discriminant))
            x2 = f"{(-b/(2*a))} - {(sqrt_discriminant/(2*a))}i"
            x1 = f"{(-b/(2*a))} + {(sqrt_discriminant/(2*a))}i"
            print(f"The values of x are {x1} and {x2}")
        break
