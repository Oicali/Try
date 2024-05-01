wordlist = []

while True:
    word = input("Enter a word: ")
    wordlist.append(word)
    ctr = len(wordlist)
    listing = range(0, ctr)

    Try = input("Do you want to try again? (Type Yes or No):")

    x = Try.upper()
    if x in ('YES', 'NO'):
        if x == 'YES':
            continue
        else:
            print("\n====RESULTS====")
            print("Number of word/s:", ctr)
            print(wordlist)
            print("\nlisting method:")

            for n in listing:
                print(wordlist[n])

            print("===============")
            break
    else:
        print("Invalid output")
        break