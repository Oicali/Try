try:
    while True:
        choice = input("Type 'Yes' or 'No' to compare numbers: ")
        if choice.lower() == "yes":
            num1 = float(input("\nEnter first number: "))
            op = input("Enter Comparator: ")
            num2 = float(input("Enter second number: "))

            if op in ">":
                print("\n", num1, ">", num2, "=", num1 > num2, "\n")

            elif op == "<":
                print("\n", num1, "<", num2, "=", num1 < num2, "\n")

            elif op == ">=":
                print("\n", num1, ">=", num2, "=", num1 >= num2, "\n")

            elif op == "<=":
                print("\n", num1, "<=", num2, "=", num1 <= num2, "\n")

            elif op == "==":
                print("\n", num1, "==", num2, "=", num1 == num2, "\n")

            elif op == "!=":
                print("\n", num1, "!=", num2, "=", num1 != num2, "\n")

            else:
                print("\nInvalid Operator!\n")

        elif choice.lower() == "no":
            print("Thank you for using this program!")
            break

        else:
            print("Invalid Answer!\n")

except:
    print("\nError!\n")
    exit()
