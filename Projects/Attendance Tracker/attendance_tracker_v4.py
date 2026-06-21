import json

def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer value.")       

def get_attendance_data(subject):
    total = get_valid_float(f"Enter the total classes for {subject}: ")
    while total <= 0:
        print("Total classes must be greater than zero. Please try again.")
        total = get_valid_float(f"Enter the total classes for {subject}: ")
    attended = get_valid_float(f"Enter the attended classes for {subject}: ")
    while attended < 0:
        print("Attended classes cannot be negative. Please try again.")
        attended = get_valid_float(f"Enter the attended classes for {subject}: ")
    while total < attended:
        print("Attended classes cannot be more than total classes. Please try again.") 
        attended = get_valid_float(f"Enter the attended classes for {subject}: ")
    return total, attended      

def get_valid_subject(prompt):
    while True:
        subject = input(prompt)
        if subject.strip() == "":
            print("Subject name cannot be empty. Please try again.")
        else:
            return subject        

try:
    file = open("attendance.txt", "r")
    attendance = json.load(file)
    print(attendance)
except:
    file = open("attendance.txt", "w")
    file.close()
    attendance = {}
    n = get_valid_int("Enter the number of subjects: ")
    while n <= 0:
        print("Number of subjects must be greater than zero. Please try again.")
        n = get_valid_int("Enter the number of subjects: ")
    for i in range(n):
        subject = get_valid_subject(f"Enter subject name {i + 1}: ")
        total, attended = get_attendance_data(subject)
        attendance[subject] = (attended / total) * 100

choice = 0
while choice != 4:
    print("1. Add/Edit")
    print("2. Remove")
    print("3. View Attendance")
    print("4. Calculate Average and Exit")
    choice = get_valid_int("Enter your choice: ")
    if choice == 1:
        subject = get_valid_subject("Enter subject name: ")
        total, attended = get_attendance_data(subject)
        attendance[subject] = (attended / total) * 100
    elif choice == 2:
        subject = get_valid_subject("Enter subject name to remove: ")
        if subject in attendance:
            del attendance[subject]
        else:
            print("Subject not found.")
    elif choice == 3:
        for subject in attendance:
            print(subject, ":", attendance[subject])        
    elif choice == 4:
        print("Calculating average attendance...")
    else:
        print("Invalid choice. Please try again.")
    
file = open("attendance.txt", "w")
json.dump(attendance, file)
file.close()

for subject in attendance:
    if attendance[subject] >= 75:
        print(subject," :", attendance[subject], ": Kar le bunk classes")
    else:
        print(subject," :", attendance[subject], ": Classes attend kar lo")
total = 0
for subject in attendance:
    total += attendance[subject]
if len(attendance) == 0:
    print("No subjects found. Average attendance cannot be calculated.")
else:
    average = total / len(attendance)
    print("Average attendance: ", average)
    if average >= 75:
        print("Overall: Bunk maar no tension")
    else:
        print("Overall: Padhai likhai kar le")