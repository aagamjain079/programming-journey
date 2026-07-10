subjects = ["Maths", "Physics", "EVS"]
teachers = ["Sharma", "Gupta", "Verma"]

for item in zip(subjects, teachers):
    print(item)
for subject, teacher in zip(subjects, teachers):
    print(subject, "->", teacher)
    