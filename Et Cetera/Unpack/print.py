# how print function print by unpacking things in side it's ()

# print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)

def print(*objects, sep=" ", end="\n", _more_arguments):
    for object in objects():
        ...