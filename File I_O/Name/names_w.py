### - - - Write a file - - - ###

name = input("What's your name? ")

with open("names.txt", "a") as file:
# w = write to edit, if use "w" old data will be removed
# a = append
    file.write(f"{name}\n")
# \n to new line after every name in the new container file

"""
name = input("What's your name? )
file = open("names.txt", "a")
file.write(f"{name\n")
file.close()
"""