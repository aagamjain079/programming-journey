i = 0
while i != 4:
    print("1. View")
    print("2. Add")
    print("3. Remove")
    print("4. Quit")
    i = int(input("Enter your choice: "))
    if i == 1:
            print("Viewing items...")
    elif i == 2:
            print("Adding item...")
    elif i == 3:
            print("Removing item...")
    elif i == 4:
            print("Goodbye!")
    else:
            print("Invalid choice")            