def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i+1))

if __name__ == "__main__":
    main()

# debugging - run the code line by line & find errors
# breakpoint - pause somewhere
# step over - execute one line at a time
# step into - to next step

# need debugging when expected output is not in result