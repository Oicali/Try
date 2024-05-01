'''
name = input ("Enter your name: ")
math = int(input("Enter your Math subject grades: "))
science = int(input("Enter your Science subject grades: "))
english = int(input("Enter your English subject grades: "))
Average = (math + science + english) / 3
print("Congratulation,", name + "! You have an average grade of " + str(Average))
'''

name = input("Enter Full Name: ")
grade1 = input("Input Math Grade: ")
grade2 = input("Input Science Grade: ")
grade3 = input("Input English Grade: ")


avg = ((float(grade1) + float(grade2) + float(grade3))/ 3)

print("\nName: "+ name)

print("\nMath Grade: " + (grade1))

print("\nEnglish Grade: " + (grade2))

print("\nScience Grade: " + (grade3))

print("\nAverage Grade:", str(avg))