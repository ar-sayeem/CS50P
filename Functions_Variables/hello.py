# Ask user for their name
# name = input("What's your name? ")


# Say hello to user
# print("Hello,", name)


# sep-end function
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# https://docs.python.org/3/library/functions.html
# print("Hello,", name, sep='???')
# print("Hello,", name, end='???')
"""
print("Hello,",end='???')
print(name)
"""

# - - - Corner case - quotation in " " - - - #
# print('Hello, "Friend"')    # Single Quotes outside
# print("Hello, \"Friend\"")  # Slash before Quotes, 
                            # quoting the metacharacter
                            # \ means scaping technic - backslash escape

"""
# Formate String/ F String
name = input("What's your name? ")
print(f"Hello, {name}")
# docs.python.org/3/library/stdtypes.html#string-methods
"""


# - - - Remove whitespace from string - - - #
# name = name.strip()         # strip only from left & right(2 kind - lstrip(), rstrip())

# - - - Capitalize user's name - - - #
# name = name.capitalize()    # Only 1st letter
# name = name.title()         # 1st letter of every word

# - - - TOGATHER : Remove whitespace and capitalize user's name - - - #
# name = name.strip().title()


### - - - Shortest way - - -###
# name = input("What's your name? ").strip().title()

### - - - Splite user's name into first name and laste name - - - ###
# name = input("What's your name? ").strip().title()
# first, mid , last = name.split(" ")
# print(f"Hello, {first}")
# print(f"Hello, {mid}")
# print("Hello,", last)
