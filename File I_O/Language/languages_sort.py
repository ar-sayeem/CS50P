### - - - Sort Alphabetical Order - - - ###


languages = []

with open("languages.csv") as file:
    for line in file:
        name, level = line.rstrip().split(",")
        language = {"name": name, "level": level}
        languages.append(language)

for lang in sorted(languages, key=lambda language: ["name"]):
    print(f"{lang['name']} is {lang['level']}")
# lamda is a function that have no name
# we don't have any function name (like get_name)
# lamda call language by their "name"



"""
 def get_name(language):
     return language["name"]

for lang in sorted(languages, key=get_name):        # , reverse=True id applicable
    print(f"{lang['name']} is {lang['level']}")
"""

# for dictionary:
#   for line in file:
        # language = {}      # {} for dictionary
        # language["name"] = name
        # language["level"] = level

    #        languages.append(f"{name} is {level}")
# for lang in sorted(languages):
#    print(lang)