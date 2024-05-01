while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    sum = num1 + num2

    print("The sum of", num1, "and", num2, "is", sum)
    Try = input("\nDo you want to try again? (Type Yes or No):")

    x = Try.upper()

    if x in ('YES', 'NO'):
        if x == 'YES':
            continue
        else:
            print("Thank you!")
            break
    else:
        print("Invalid Input\n")

