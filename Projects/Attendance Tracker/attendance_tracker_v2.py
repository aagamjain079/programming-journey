attendance = {}
n = int(input("Enter the number of subjects: "))

for i in range(n):
    subject = input(f"Enter subject name {i + 1}: ")
    total = float(input(f"Enter the total classes for {subject}: "))
    attended = float(input(f"Enter the attended classes for {subject}: "))
    attendance[subject] = (attended / total) * 100

for subject in attendance:
    if attendance[subject] >100:
        print(subject," :", attendance[subject],": Invalid attendance percentage")
    elif attendance[subject] >= 75:
        print(subject," :", attendance[subject], ": Kar le bunk classes")
    else:
        print(subject," :", attendance[subject], ": Classes attend kar lo")
total = 0
for subject in attendance:
    total += attendance[subject]
average = total / len(attendance)
print("Average attendance: ", average)
if average > 100:
    print("Overall: Theek se attendance daal lala")
elif average >= 75:
    print("Overall: Bunk maar no tension")
else:
    print("Overall: Padhai likhai kar le")