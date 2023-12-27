def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":      # only call main when it's called
    main()

# if we blindly calling main() it means
# that the code will run even if this file is imported as a module.
# using __name__ == "__main__" only then main() can be called.