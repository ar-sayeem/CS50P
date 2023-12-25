#   try     |   except ValueError

try:
    x = int(input("What's x? "))
    print(f"x is {x}")

# if user input anything else except integer value
except ValueError:
    print("Inputed x is not an integer")
