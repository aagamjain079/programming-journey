with open("test.txt","w") as file:
    file.write("BRO IS LEARNING")
with open("test.txt", "r") as file:
    content = file.read()

print(content)
print(file.closed)
content2 = file.read()
print(content2)