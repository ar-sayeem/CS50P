import re

name = input("What's your name? ")
if matches := re.search(r"^(.+), *(.+)$", name):        # * to remove ectra spaces between first and last name during input
    name = matches.group(2) + " " + matches.group(1)
    # last, first = matches.groups()
    # name = f"{first} {last}"
print(f"hello, {name}")


#   Walrus Operator        if and only if
#          :=              assign something to right to left and ask boolean question
#          ?:              means don't capture