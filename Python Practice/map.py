numbers = [1, 2, 3, 4]
squares = map(lambda x: x * x, numbers)
print(squares)
print(list(squares))

names = ["aagam", "rahul", "priya"]
result = map(lambda name: name.upper(), names)
print(list(result))