# enumerate(iterable, start=0)
# Enumerate is a built-in function in python that
# allows you to keep track of the number of iterations (loops) in a loop. 

student = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(student):
    print(i+1, student)