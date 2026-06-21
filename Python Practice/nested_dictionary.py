attendance = {
    "Maths": {
        "total": 40,
        "attended": 35
    }
}

print(attendance["Maths"]["total"])
print(attendance["Maths"]["attended"])
print(attendance["Maths"]["attended"] / attendance["Maths"]["total"] * 100)
attendance["Maths"]["total"] += 1
attendance["Maths"]["attended"] += 1
print(attendance)