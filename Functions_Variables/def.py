"""
def hello():
    print("Hello!")


name = input("What's your name? ")
hello()
print(name)
"""

# def hello(to = "world"):
    #print("Hello!", to)

# name = input("What's your name? ")
# hello()
# hello(name)

### - - - Using main function - - - ###
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)

main()