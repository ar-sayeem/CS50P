# map(function, iterables, ...)

def main():
    yell("This", "is", "Cs50p")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)
    # uppercased = [word.upper() for word in words]
    # print(*uppercased)

if __name__ == "__main__":
    main()