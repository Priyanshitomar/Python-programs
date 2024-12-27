number = input("Enter a number: ")
if number.isdigit():
    number = int(number)
    if number > 0:
        print("Positive number.")
    elif number < 0:
        print("Negative number.")
    else:
        print("Zero.")
else:
    print("Invalid input.")
