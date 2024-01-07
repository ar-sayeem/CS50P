# 'yield' statement returns a generator object to the one who calls
# the function which contains yield, instead of simply returning a value.


# Works for bigger inputs.
# Don't run the entire loop then return a value.
# It's do one iteration and yield a result.
# Each iteration return only that string,
# not also the previos ones, so memory cant easily execute full code.

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i          # yield = return 1 value at a time

if __name__ == "__main__":
    main()


"""
# if the n is big enough for example 1000000 code won't work
# Code can't return so many times, need huge memory

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock

if __name__ == "__main__":
    main()
"""
