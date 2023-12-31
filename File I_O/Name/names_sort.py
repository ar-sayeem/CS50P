# sorted(iterable, /, *, key=None, reverse=False)

names = []

with open("names.txt") as file: #to open a file "r" is not necessary
    for line in file:
        names.append(line.rstrip())

# after reading every line of that file, we sort
for name in sorted(names):      # Accending
    print(f"{name}")

print("-  -  -  -  -  -  -")

for name in sorted(names, reverse=True):  # Decending
    print(f"{name}")