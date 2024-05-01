acronyms = ["F", "L", "A", "M", "E", "S"]
meaning = ["FRIENDS", "LOVERS", "ADMIRERS", "MARRIAGE", "ENEMIES", "SOULMATES"]

print("Hello, I am Digi-FLAMES! A digital program of the iconic FLAMES.")
print(
    "This game can determine the relationship between two people with the use of their names. Refer to guide below:"
)
for _ in range(len(meaning)):
    print(f"{acronyms[_]} - {meaning[_]}")

while True:
    use = input("\nType 'YES' or 'NO' to play FLAMES: ")
    if use.strip().upper() in ["YES", "Y"]:
        N1 = input("\nType the name of the 1st person: ")
        N2 = input("Type the name of the 2nd person: ")

        Name1 = N1.replace(" ", "").upper()  # Uppercase the names and removes spaces
        Name2 = N2.replace(" ", "").upper()

        commonletters = list(set(Name1) & set(Name2))  # Lists the common letters

        uncommon = [i for i in Name1 if i not in commonletters] + [
            i for i in Name2 if i not in commonletters
        ]  # Lists the uncommon letters

        uncommonletters = list(uncommon)
        num = len(uncommonletters)

        print("\n====RESULTS====\n")
        print("List of common letters:", commonletters)
        print("Number of common letter/s:", len(commonletters), "\n")
        print("List of uncommon letters:", uncommonletters)
        print("Number of uncommon letter/s:", num, "\n")

        if num == 0:
            print(
                "Error! The names you input have same number of common letters. Please try another name."
            )
        elif num % 6 == 1:
            print(N1.title(), "and", N2.title(), "are F as in FRIENDS!")
        elif num % 6 == 2:
            print(N1.title(), "and", N2.title(), "are L as in LOVERS!")
        elif num % 6 == 3:
            print(N1.title(), "and", N2.title(), "are A as in ADMIRERS!")
        elif num % 6 == 4:
            print(N1.title(), "and", N2.title(), "are M as in MARRIED!")
        elif num % 6 == 5:
            print(N1.title(), "and", N2.title(), "are E as in ENEMIES!")
        elif num % 6 == 0:
            print(N1.title(), "and", N2.title(), "are S as in SOULMATES!")
        else:
            print("Error!")
        print("\n===============")

    elif use.strip().upper() in ["NO", "N"]:
        print("\nThank you for using Digi-FLAMES!\n")
        break

    else:
        print("Invalid input!")