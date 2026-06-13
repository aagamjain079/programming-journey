while True:
    try:
        i = int(input("Enter a number: "))
        print("You entered:", i)
        break
    except ValueError:
        print("Please enter a valid number.")