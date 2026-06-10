marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))

average = (marks1 + marks2 + marks3) / 3
print("The average marks is:", average)
if average >=40:
    print("Pass")
else:
    print("Fail")