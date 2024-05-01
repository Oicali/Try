name = input("Enter Employee name: ")
year = int(input("Enter years-in-service: "))
office = input("Enter office: ")

if office == 'IT':
    if year >= 10:
        print("Hi" + name + ", your bonus is 10000.")

    else:
        print("Hi" + name + ", your bonus is 5000.")

if office == 'acct':
    if year >= 10:
        print("Hi" + name + ", your bonus is 12000.")

    else:
        print("Hi" + name + ", your bonus is 6000.")

if office == 'hr':
    if year >= 10:
        print("Hi" + name + ", your bonus is 15000.")

    else:
        print("Hi" + name + ", your bonus is 7500.")