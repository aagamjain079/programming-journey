def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid float.")

number = get_valid_float("Enter a number: ")
print(number)