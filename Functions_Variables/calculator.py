### - - - INTEGER - - - ###

# x = input("What's x? ")
# y = input("What's y? ")
# z = x + y             # output will be xy, + concatenating as string
# z = int(x) + int(y)   # output x+y as integer
# print(z)
"""
x = int(input("What's x? "))
y = int(input("What's y?"))
print("Sum is", x+y)
"""

### - - - FLOAT - - - ###

# x = float(input("What's x? "))
# y = float(input("What's y? "))



# print("Sum is", x+y)
# round(number[, ndigits]) | https://docs.python.org/3/library/functions.html#round


# z = round(x+y, 4)   # rounding to 5 decimal places
# print(f"{z:,}")     # put Coma (,) after every 3 digits
# w = x/y
# print(w)            # 2/3 = 0.6666666666666666

# w = round(x/y, 2)
# print(w)            # 2/3 = 0.67

# print(f"{w:.2f}")   # 2/3 = 0.67



### - - - return value - - - ###

def main():
    x = int(input("What's x? "))
    print("Square of x =", square(x))
    print("x Power of x =", power(x))

def square(n):
    return n * n
    # return pow(n, 2)
def power(n):
    # return n ** n
     return pow(n, n)
     
main()