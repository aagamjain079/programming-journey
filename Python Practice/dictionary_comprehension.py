squares = {i: i * i for i in range(1, 6)}
print(squares)

subjects = ["Maths", "Physics", "EVS"]
lengths = {subject: len(subject) for subject in subjects}
print(lengths)

student = {
    "name": "Aagam",
    "age": 18
}
for key, value in student.items():
    print(value)