principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter principle amount: $"))
    if principle <= 0:
        print("Principle amount must be greater than 0")
    else:
        break

while True:
    rate = float(input("Enter interest rate: %"))
    if rate <= 0:
        print("Rate amount must be greater than 0")
    else:
        break

while True:
    time = float(input("Enter amount of time (in years): "))
    if time < 0:
        print("Time amount must be greater than 0")
    else:
        break

frequency_time = float(input(
    "How many times does it compound annually?[Monthly(12), Quarterly(4)]: "))

while True:
    if frequency_time < 0:
        print("Give a valid answer.")
    else:
        break

final_amount = principle * \
    pow((1 + rate/100/frequency_time), frequency_time * time)


print(
    f"The final amount over {time} year(s) at %{rate} rate is : ${final_amount}")
