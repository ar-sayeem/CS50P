def get_Guess():
    number = int(input("Guess a number between 49 and 51:\n"))
    return number

def main():
    guess = get_Guess()
    if guess == 50:
        print("🏆Correct✔")
    else:
        print("❌Incorrect❌")

main()