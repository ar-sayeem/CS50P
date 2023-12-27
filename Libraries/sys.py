import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments!")      # sys.exit() to terminate the whole program

for arg in sys.argv[1:]:           # [Lower index : ] loop will run to end
    print("Hello, my name is", arg)


# for arg in sys.argv[1:-1]:           # slice from the end
    # print("Hello, may name is", arg)



"""
elif len(sys.argv) > 2:
    sys.exit("Too many arguments!")
else:
    print("Hello, my name is ", sys.argv[1])
# write : > sys.py Name
# write : > sys.py "Your Full Name" with quotes

"""


# import sys
# print("Hello, my name is ", sys.argv[0])
# if index is 0 it will print file's location