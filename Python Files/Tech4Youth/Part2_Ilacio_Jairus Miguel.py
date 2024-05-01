#NAME: ILACIO, JAIRUS MIGUEL
#PYTHAGORAS

#MINI PROGRAM 1
'''
F1 = input("1. Type a firstname: ")
F2 = input("2. Type a firstname: ")
F3 = input("3. Type a firstname: ")
F4 = input("4. Type a firstname: ")
F5 = input("5. Type a firstname: ")

print('\n=======RESULTS=======')
print("1. The name", F1, "has", len(F1), "characters.")
print("2. The name", F2, "has", len(F2), "characters.")
print("3. The name", F3, "has", len(F3), "characters.")
print("4. The name", F4, "has", len(F4), "characters.")
print("5. The name", F5, "has", len(F5), "characters.")
print('=====================')
'''

#MINI PROGRAM 2
'''
print("Greetings! This is Odd or Even Checker. A program that identifies the number you input whether it is an even or odd.")

while True:
    choice = input("Would you like to use this program?: ")
    choice = choice.upper()
    if choice in ("YES", "NO"):
        if choice == "YES":
            num = int(input("Input a number: "))

            if num%2 == 0:
                print("The number you input is an even number!")
            else:
                print("The number you input is an odd number!")

        elif choice == 'NO':
            print("Thank you for using this program!")
            break

    else:
        print("Invalid Input!")
'''

#MINI PROGRAM 3
'''
word = input("Input a string: ")
counter = 0
wordctr = len(word)
listing = range(wordctr+1)

for x in listing:
    print(word[0: counter])
    counter+=1
'''

#MINI PROGRAM 4
'''
xctr = 1
yctr = 10
ctr = 0

while True:
    if ctr == 10:
        break

    else:
        print (xctr, yctr)
        xctr+=1
        yctr-=1
        ctr+=1
'''

#MINI PROGRAM 5
'''
word = input("Type a word: ")
word = word.upper()
wordrev = reversed(word)

if list(word) == list(wordrev):
    print(word, "is a PALINDROME!")

else:
    print(word, "is NOT a PALINDROME!")
'''