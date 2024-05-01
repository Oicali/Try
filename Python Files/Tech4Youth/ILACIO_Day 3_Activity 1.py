name = input("Type your name: ")
math = float(input("Type Math grades: "))
science = float(input("Type Science grades: "))
english = float(input("Type English grades: "))

average = (math + science + english)/3

print("\nName:", name)
print("Math:", math)
print("Science:", science)
print("English:", english)
print("Average:", average)

if average >= 75:
    print("\nCongratulations! You passed the semester.")

    if math < 75:
        print("Re-enrollment in Math subject is required.")

    if science < 75:
        print("Re-enrollment in Science subject is required.")

    if english < 75:
        print("Re-enrollment in English subject is required.")

else:
    print("\nSorry, you failed the semester.")