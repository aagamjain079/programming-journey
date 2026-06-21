safe = 75
total = 1
attended = 1
percentage = attended/total*100
missable = 0
while percentage >= safe:
    total += 1
    percentage = attended/total*100
    missable += 1
    print(missable)