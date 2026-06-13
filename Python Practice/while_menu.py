i = 0
while i != 2:
    print("1. Say Hello")
    print("2. Quit")
    i = int(input("Enter your choice: "))
    if i == 1:
        print("Hello")
    elif i == 2:
        print("Goodbye!")
    else:
        print("Invalid choice")