"""
def main():
    print_coloum(3)

def print_coloum(height):
    print("#\n" * height, end="")

main()
# - - - - - - - - - - - - - - - - - - #
def main():
    print_row(4)

def print_row(width) :
    print("?" * width)

main()
"""



def main():
    print_square(3)

def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):   # [in short: print("#" * size)]

            # Print brick
            print("#", end="")

        print()         # A new line after every row

main()



### - - - in short - - - ###
"""
def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print("#" * size)
main()  """