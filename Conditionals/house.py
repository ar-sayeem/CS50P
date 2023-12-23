name = input("What's your name? ")

"""
if name == "Harry":
    print("Gryffindor")
elif name == "lermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who")        """



# if name == "Harry" or name == "Hermione" or name == "Ron":
    # print("Gryffindor")
# elif name == "Draco":
    # print("Slytherin")
# else:
    # print("who")


match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")