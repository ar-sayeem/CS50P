#   try   |   except ValueError   |   else

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            # return int(input("What's x? "))
            # if do like this there is no need of else function
        except ValueError:
            print("Inputed x is not an integer")
        else:
            return x        # instead of break directly return x

main()