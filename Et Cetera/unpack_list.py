# splitting the packed values into individual elements
# The packed values are strings, lists, tuples, sets, and dictionaries.
# *args, **kwargs


"""
first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")
"""

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

# print(total(100, 50, 25), "Knuts")
# print(total(coins[0], coins[1], coins[2]), "Knuts")

print(total(*coins), "Knuts")

# to unpack coins list '*' before coins