# Dictionary comprehension is a method for 
# transforming one dictionary into another dictionary.


students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)