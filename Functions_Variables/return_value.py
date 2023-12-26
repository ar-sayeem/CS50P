def greet(input):
    if "1234" in input:
        return "Hey, welcome back, Adnan"
    else:
        return "Who are you?"
# write the actual password
greeting = greet("dfqdeq3")          # "password=1234"
print(greeting)