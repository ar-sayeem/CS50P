with open("students.csv") as file:
    for line in file:
                 name, home = line.rstrip().split(",")
                 print(f"{name} is {home}")
