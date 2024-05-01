try:
    name = str(input("Enter Employee name: "))
    year = int(input("Enter years-in-service: "))
    office = str(input("Enter office: "))

    if office.lower() == 'it':
        if year >= 10: bonus = 10000

        else: bonus = 5000

    if office.lower() == 'acct':
        if year >= 10: bonus = 12000

        else: bonus = 6000

    if office.lower() == 'hr':
        if year >= 10: bonus = 15000

        else: bonus = 7500

    print(f"Hi {name}, your bonus is {bonus}.")

except:
    print("Invalid Input!")
    exit()