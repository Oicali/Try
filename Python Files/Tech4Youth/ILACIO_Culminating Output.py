print("Hello, I am Digi-FLAMES! A digital program of the iconic FLAMES.")
print("This game can determine the relationship between two people with the use of their names. Refer to guide below:")
print("F - FRIENDS")
print("L - LOVERS")
print("A - ADMIRERS")
print("M - MARRIAGE")
print("E - ENEMIES")
print("S - SOULMATES")

while True:
    use = input("\nType 'YES' or 'NO' to play FLAMES: ")
    use = use.upper()

    if use in ('YES', 'NO'):
        if use == 'YES':
            N1 = input("\nType the name of the 1st person: ")
            N2 = input("Type the name of the 2nd person: ")

            N1 = N1.upper()    #Uppercase the names
            N2 = N2.upper()

            commonletters = list(set(N1)&set(N2))    #Lists the common letters 
            if ' ' in commonletters:
                commonletters.remove(' ')
            clnum = len(commonletters)

            uncommon = [i for i in N1 if i not in commonletters] + [i for i in N2 if i not in commonletters]   #Lists the uncommon letters
            for x in uncommon:           
                if ' ' in uncommon:
                    uncommon.remove(' ')

            uncommonletters = list(uncommon)
            num = len(uncommonletters)    

            print("\n====RESULTS====\n")
            print("List of common letters:", commonletters)
            print("Number of common letter/s:", clnum, '\n')
            print("List of uncommon letters:", uncommonletters)
            print("Number of uncommon letter/s:", num, '\n')

            if any([num==1, num==7, num==13, num==19, num==25]):
                print(N1.capitalize(), 'and', N2.capitalize(), 'are F as in FRIENDS!')
            elif any([num==2, num==8, num==14, num==20, num==26]):
                print(N1.capitalize(), 'and', N2.capitalize(), 'are L as in LOVERS!')
            elif any([num==3, num==9, num==15, num==21, num==27]):
                print(N1.capitalize(), 'and', N2.capitalize(), 'are A as in ADMIRERS!')
            elif any([num==4, num==10, num==16, num==22, num==28]):
                print(N1.capitalize(), 'and', N2.capitalize(), 'are M as in MARRIED!')
            elif any([num==5, num==11, num==17, num==23, num==29]):
                print(N1.capitalize(), 'and', N2.capitalize(), 'are E as in ENEMIES!')
            elif any([num==6, num==12, num==18, num==24, num==30]):
                print(N1.capitalize(), 'and', N2.capitalize(), 'are S as in SOULMATES!')
            elif num==0:
                print("Error! The names you input have same number of common letters. Please try another name.")
            else:
                print('Error!')
            print("\n===============")

        if use == 'NO':
            print('\nThank you for using Digi-FLAMES!')
            break

    else:
        print('Invalid input!')