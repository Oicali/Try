while True:
    choice = input("Type 'Yes' or 'No' to compare numbers: ")
    if choice in ('Yes', 'No'):
        if choice == 'Yes':
            if True:
                operator = input("Type comparing operator: ")
                if operator in ('<', '>', '==', '>=', '<=', '!='):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if operator == '<':
                        print(num1, "<", num2, ":", num1 < num2)

                    if operator == '>':
                        print(num1, ">", num2, ":", num1 > num2)

                    if operator == '==':
                        print(num1, "==", num2, ":", num1 == num2)

                    if operator == '>=':
                        print(num1, ">=", num2, ":", num1 >= num2)

                    if operator == '<=':
                        print(num1, "<=", num2, ":", num1 <= num2)

                    if operator == '!=':
                        print(num1, "!=", num2, ":", num1 != num2)

                else:
                    print("Invalid Comparators")

        elif choice == 'No':
            print("End of comparison")
            break

    else:
        print("Invalid Input")