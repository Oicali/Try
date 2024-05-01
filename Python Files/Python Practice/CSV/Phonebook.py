import csv

#This will access phonebook.csv and append (a)
file = open("phonebook.csv", "a")

name = input("Enter name: ")
number = input("Enter Phone number: ")
 
writer = csv.writer(file)
writer.writerow([name, number])

file.close()

'''
1. Run Phonebook.py by entering "python Phonebook.py" on the Terminal
2. Input for name and number
3. Enter "ls" to check the csv file from the directory
4. Open Phonebook.csv by entering "code Phonebook.csv"
'''