# Python documentation strings (or docstrings) provide a convenient way
# of associating documentation with Python modules, functions, classes, and methods.
# """ ... """ or ''' ... '''


def meow(n: int) -> str:
    """
    Meow n times.
    
    : param n: Number of times to meow
    : type n: int
    : raise TypeError: If is not an int
    : return: A string of n meows, one per line
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
