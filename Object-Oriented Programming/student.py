# tuple - IMMUTABLE - can't be change
# tuple vs list

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]
    # List - [] Mutable
    # Tuple - () Immutable - can't change inside of tuple (such as, using if)

if __name__ == "__main__":
    main()