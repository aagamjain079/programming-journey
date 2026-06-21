data = {
    "safe_limit": 75,
    "subjects": {
        "Maths": {
            "Total": 40,
            "Attended": 35
        },
        "Physics": {
            "Total": 50,
            "Attended": 42
        }
    }
}

print(data["safe_limit"])
print(data["subjects"]["Maths"]["Total"])
for subjects in data["subjects"]:
    print(subjects)