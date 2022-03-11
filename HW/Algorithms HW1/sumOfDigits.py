
def sum_digits(x):
    intValue = int(x)

    counter = 0
    total = 0

    while(counter < intValue):
        counter += 1
        total += counter

    print(total)

value = input("Enter value:")
print(f"You enter: {value}")
sum_digits(value)