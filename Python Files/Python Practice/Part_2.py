#mini Program 1
'''
names = []

for i in range(5):
    name = input("Enter name: ")
    names.append(name)

print('\n=======RESULTS=======')
for j in range(5):
    print(f"The name {names[j]} has {len(names[j])} character/s.")
print('=====================')
'''

#Mini Program 2
'''
while True:
    try:
        choice = input("Would you like to use this program?: ")
        if choice.upper() == "YES":
            num = int(input("Input a number: "))

            if num%2 == 0:
                print("The number you input is an even number!\n")
            
            else: print("The number you input is an odd number!\n")

        elif choice.upper() == 'NO':
            print("Thank you for using this program!\n")
            break

        else: print("Invalid Answer! [Yes or No]\n")

    except:
        print("Invalid Input\n")
        continue
'''
            
#Mini Program 3

word = input("Enter a word: ")

for i in range(len(word)): print(word[0:i+1])


#Mini Program 4
'''
x = 1

for y in range(10, 0, -1):
    print(f"{x} {y}")
    x+=1
'''

#Mini Program 5
'''
word = input("Enter a word: ")
if word.upper() == word[::-1].upper(): print(f"The word {word.upper()} is a PALINDROME")
else: print(f"The word {word.upper()} is NOT a PALINDROME")
'''