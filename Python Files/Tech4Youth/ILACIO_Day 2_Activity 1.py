first = input("Enter first name: ")
last = input("Enter last name: ")
gender = input("Type 'M' or 'F' for your gender: ")

if gender in ('M','F'):
    if gender == 'M':
            print("Hello,", first.replace(first, 'Mr.'), last)

    if gender == 'F':
            print("Hello,", first.replace(first, 'Ms.'), last)

else:
        print("Please type only 'M' or 'F'")



