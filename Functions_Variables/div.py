x = float(input("What's x? "))
y = float(input("What's y? "))

p = x/y
q = x//y

print(f"x/y(2 decimal) = {p:.2f}")
print(f"x/y(floor value) = {q}")

# /  : Divides the number on its left by the number on its right,
#       and returns a floating point value.
# // : Divides the number on its left by the number on its right,
#       rounds down the answer, and returns a whole number.