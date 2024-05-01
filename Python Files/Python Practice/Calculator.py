try:
    while True:
        Answer = input("\nWould you like to use Calculator: ")

        if Answer.strip().upper() in ["YES", "Y"]:
            n1 = float(input("\nEnter first number: "))
            op = input("Enter operator: ")
            n2 = float(input("Enter second number: "))

            if op in ["+", "-", "*", "/", "%", "**"]:
                """
                results = float(eval(str(n1) + op + str(n2)))
                print(f"\n{n1} {op} {n2} = {results:.2f}")
                """
                print(f"\n{n1} {op} {n2} = {round(eval(str(n1) + op + str(n2)), 2)}")

            else:
                print("\nInvalid Operator!")

        elif Answer.strip().upper() in ["NO", "N"]:
            print("\nThank you for using Calculator!\n")
            break

        else:
            print("\nInvalid Answer!")

except:
    print("\nInvalid Input!\n")
    exit()
