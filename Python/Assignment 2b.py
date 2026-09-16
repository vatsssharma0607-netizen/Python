marks = []
subjects = ["Math","Science","English","History","Geography"]
print("Enter the marks for 5 subjects")
for sub in subjects:
    score = float(input("Enter marks for subject: "))
    marks.append(score)
print("\nDisplaying Subject Marks")
for i in range(len(subjects)):
    print("{}:{}".format(subjects[i], marks[i]))
