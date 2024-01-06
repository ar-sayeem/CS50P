students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Revenclaw"}
]

"""
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"]) """
# same using using set
houses = set()
for student in students:
    houses.add(student["house"])        # set cut the duplicates and add new ones

for house in sorted(houses):
    print(house)