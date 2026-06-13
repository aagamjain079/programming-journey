import json

attendance = {
    "Maths": 80,
    "Physics": 75
}
json_string = json.dumps(attendance)
print(type(json_string))
json_dict = json.loads(json_string)
print(type(json_dict))