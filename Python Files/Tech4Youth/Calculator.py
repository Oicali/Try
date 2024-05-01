while True: 
    choice = input("Type 'Yes' or 'No' to use calculator: ")
    if choice in ('Yes', 'No'):
        if choice == 'Yes':
            print("Choose an operation: ")
            print("1 - add")
            print("2 - subtract")
            print("3 - multiply")
            print("4 - divide")
            print("5 - remainder")
            print("6 - exponent")
            if True:
                choice_1 = input("Type number operator (1-6): ")
                if choice_1 in ('1', '2', '3', '4', '5', '6'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice_1 == '1':
                        print(num1, "+", num2, "=", num1 + num2)

                    elif choice_1 == '2':
                        print(num1, "-", num2, "=", num1 - num2)

                    elif choice_1 == '3':
                        print(num1, "*", num2, "=", num1 * num2)

                    elif choice_1 == '4':
                        print(num1, "/", num2, "=", num1 / num2)

                    elif choice_1 == '5':
                        print(num1, "%", num2, "=", num1 % num2)

                    elif choice_1 == '6':
                        print(num1, "^", num2, "=", num1 ** num2)

                else:
                    print("Invalid Input")

        elif choice == 'No':
            print("Thank you for using calculator")
            break

    else:
        print("Invalid Input")