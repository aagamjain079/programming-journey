attendance = {
    "AM2": 80,
    "AP2": 70,
    "EM": 90
}
file = open("attendance.txt", "w")
file.write(str(attendance))
file.close()

import ast
file = open("attendance.txt", "r")
content = file.read()
attendance = ast.literal_eval(content)

print(attendance)
print(type(attendance))