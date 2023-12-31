### - - - Read a file - - - ###

with open("names.txt", "r") as file:
# r = read, to open a file "r" is not necessary
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
    # print("hello,", line, end="")

# .rstrip() does same as end="", terminate the extra new line

# in short # - in this names can't be sort
# with open("names.txt", "r") as file:
    # for line in lines:
        # print("hello,", line.rstrip())