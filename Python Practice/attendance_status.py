attendance = {
    "Maths": 75,
    "Physics": 82,
    "Chemistry": 68,
    "English": 91
}
for subject in attendance:
    if attendance[subject] >= 75:
        print(subject,": Safe")
    else:
        print(subject,": Risk")