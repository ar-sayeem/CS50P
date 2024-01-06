# mypy - optional static type checker

def meow(n: int) -> str:       # type of the return value is str
    return "meow\n" * n
    # for _ in range(n):
        # print("meow")


number: int = int(input("Number: "))
# ': int' is a type hint, 'int(...)' is the int function
meows: str = meow(number)
print(meows, end="")

# Run in terminal > mypy file.py