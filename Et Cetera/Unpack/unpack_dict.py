# splitting the packed values into individual elements
# The packed values are strings, lists, tuples, sets, and dictionaries.
# *args, **kwargs


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")

# to unpack coins dictionary '**' before coins