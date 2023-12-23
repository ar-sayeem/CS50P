"""

x = int(input("What's x ? "))

if x % 2 == 0:
    print("x is even number")
else:
    print("x is odd number")


"""

def main():
    x = int(input("What's x ? "))
    if is_Even(x):
        print("Even")
    else:
        print("Odd")

def is_Even(n):
    # return (n % 2 == 0)     [easiest - return the question]
    # return True if n % 2 == 0 else False
    if n % 2 == 0:
        return True
    else:
        return False

main()