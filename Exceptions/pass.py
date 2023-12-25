# keyword pass

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            pass        
        # pass to next line - return to while loop
        # no need to say : it's not integer everytime

main()


