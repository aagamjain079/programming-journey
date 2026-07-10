number1 = [i for i in range(1, 6)]
print(number1)

number2 = [i * 2 for i in range(1, 6)]
print(number2)

number3 = [i for i in range(1, 11) if i % 2 == 0]
print(number3)

subjects = ["maths", "physics", "evs"]
capitalized = [subject.upper() for subject in subjects]
print(capitalized)