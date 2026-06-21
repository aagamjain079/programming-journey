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
        
def get_valid_safelimit(prompt):
    while True  :
       safelimit = get_valid_float(prompt)
       if 50 > safelimit:
           print("Bro maintain decent attendance.")
           continue
       elif 100 < safelimit:
           print("Don't be unreal bro.")
           continue
       else:
        return safelimit

try:
    file = open("attendance.txt", "r")
    attendance = json.load(file)
    file.close()
except:
    file = open("attendance.txt", "w")
    file.close()
    attendance = {"safe_limit":75, "subjects":{}}
    attendance["safe_limit"] = get_valid_safelimit("Enter the Safe Limit: ")
    n = get_valid_int("Enter the number of subjects: ")
    while n <= 0:
        print("Number of subjects must be greater than zero. Please try again.")
        n = get_valid_int("Enter the number of subjects: ")
    for i in range(n):
        subject = get_valid_subject(f"Enter subject name {i + 1}: ")
        total, attended = get_attendance_data(subject)
        attendance["subjects"][subject] = {"total":total,"attended":attended}

choice = 0
while choice != 7:
    print("================================")
    print("1. Add Subject")
    print("2. Edit Safe Limit")
    print("3. Remove")
    print("4. Mark Attended Class")
    print("5. Mark Missed Class")
    print("6. View Stats")
    print("7. Exit")
    print("================================")
    choice = get_valid_int("Enter your choice: ")

    if choice == 1:
        subject = get_valid_subject("Enter subject name: ")
        total, attended = get_attendance_data(subject)
        attendance["subjects"][subject] = {"total":total,"attended":attended}

    elif choice == 2:
        attendance["safe_limit"] = get_valid_safelimit("Enter the Safe Limit: ")

    elif choice == 3:
        subject = get_valid_subject("Enter subject name to remove: ")
        if subject in attendance["subjects"]:
            del attendance["subjects"][subject]
        else:
            print("Subject Not Found X_X")

    elif choice == 4:
        subject = get_valid_subject("Enter Subject Name: ")
        if subject in attendance["subjects"]:
            attendance["subjects"][subject]["total"] += 1
            attendance["subjects"][subject]["attended"] += 1
            print("Attendance Marked")
        else:
            print("Subject Not Found x_x")

    elif choice == 5:
        subject = get_valid_subject("Enter Subject Name: ")
        if subject in attendance["subjects"]:
            attendance["subjects"][subject]["total"] += 1
            print("Missed Class Marked")
        else:
            print("Subject Not Found x_x")

    elif choice == 6:
        print("================================")
        print("Safe Limit: ",attendance["safe_limit"])
        print("================================")
        total=0
        safelimit = attendance["safe_limit"]
        for subject in attendance["subjects"]:
            percentage = attendance["subjects"][subject]["attended"]/attendance["subjects"][subject]["total"]*100
            print("Subject: ",subject,"\n")
            print("Total Classes: ",attendance["subjects"][subject]["total"])
            print("Attended Classes: ",attendance["subjects"][subject]["attended"])
            print("Attendance: ",percentage,"%\n")
            if percentage >= safelimit:
                temp_total = attendance["subjects"][subject]["total"]
                temp_attended = attendance["subjects"][subject]["attended"]
                temp_percentage = temp_attended/temp_total*100
                missable_classes = 0
                while temp_percentage >= safelimit:
                    temp_total += 1
                    temp_percentage = temp_attended/temp_total*100
                    missable_classes +=1
                print("Status: Safe")
                print("You can miss",missable_classes-1,"more classes.")
            else:
                temp_total = attendance["subjects"][subject]["total"]
                temp_attended = attendance["subjects"][subject]["attended"]
                temp_percentage = temp_attended/temp_total*100
                needed_classes = 0
                while temp_percentage <= safelimit:
                    temp_total += 1
                    temp_attended += 1
                    temp_percentage = temp_attended/temp_total*100
                    needed_classes += 1
                print("Status: Unsafe")
                print("You need to attend",needed_classes,"more classes.")
            total += percentage
            print("================================")
        if len(attendance["subjects"]) == 0:
            print("No subjects found. Average attendance cannot be calculated.")
        else:
            average = total / len(attendance["subjects"])
            print("Average attendance: ", average)
            if average >= safelimit:
                print("Overall: Bunk maar no tension")
            else:
                print("Overall: Padhai likhai kar le")
            print("================================")

    elif choice == 7:
        print("Thanks for using.")

    else:
        print("Invalid choice. Please try again.")
    
file = open("attendance.txt", "w")
json.dump(attendance, file)
file.close()
