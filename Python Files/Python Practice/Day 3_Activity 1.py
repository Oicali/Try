subjects = ["Math", "Science", "English"]
scores = []
failed = []
i = 0


def Average(scores):
    sum = 0

    for score in scores:
        sum = sum + score

    return sum / len(scores)


name = input("Name: ")

try:
    while i < len(subjects):
        score = int(input(f"{subjects[i]} Grade: "))
        if score >= 70 and score <= 100:
            scores.append(score)
            i = i + 1

        else:
            print(f"\nInvalid Input for the subject {subjects[i]}!\n")
            continue

    result = Average(scores)

    print("Average: {:.2f}".format(result))

    if result >= 75:
        print("\nCongratulations! You passed the semester.")

        if any(val in scores for val in [74, 73, 72, 71, 70]):
            for k in range(len(scores)):
                if scores[k] < 75:
                    failed.append(subjects[k])
            print(
                "But re-enrollment in "
                + " and ".join(str(i) for i in failed)
                + " is required!\n"
            )

    else:
        print("\nSorry, you failed the semester.")

except:
    print("\nInput numbers only!\n")
    exit()
