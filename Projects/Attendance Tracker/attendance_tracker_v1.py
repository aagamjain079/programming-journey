attendance = {
    "AM2": float(input("Enter the attendance percentage for AM2: ")),
    "AP2": float(input("Enter the attendance percentage for AP2: ")),
    "EM": float(input("Enter the attendance percentage for EM: ")),
    "EVS": float(input("Enter the attendance percentage for EVS: ")),
    "PC": float(input("Enter the attendance percentage for PC: "))
}
for subject in attendance:
    if attendance[subject] >= 75:
        print(subject, ": Safe")
    else:
        print(subject, ": Risk")
total = 0
for subject in attendance:
    total += attendance[subject]
average = total / len(attendance)
print("Average attendance: ", average)
if average >= 75:
    print("Overall: Safe")
else:
    print("Overall: Risk")