# print("meow")
# print("meow")
# print("meow")
"""
i = 3
while i != 0:
    print("meow")
    i = i-1
"""

# i = 0               # i = 1
# while i < 3:        # i <= 3
    # print("meow")
    # i += 1          # i = i + 1

"""
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
# if user gives positive valur break and start the loop
for _ in range(n):
    print("meow")   """


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break       # not necessary, could directtly return n
    return n
    
def meow(n):
    for _ in range(n):
        print("meow")
    
main()