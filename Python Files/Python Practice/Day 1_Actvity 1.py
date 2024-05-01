name = input("Name: ")

subjects = ["Math", "Science", "English"]
scores = []
avg = 0

try:
    for subject in subjects:
        score = float(input(f"{subject} Grade: "))
        scores.append(score)

    for score in scores: avg = avg + score

    avg = avg/len(scores)

    print("\nAverage: {:.2f}".format(avg))

except:
    print("\nInvalid Input!")
    exit()