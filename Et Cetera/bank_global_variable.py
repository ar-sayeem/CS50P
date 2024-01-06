# use of global variable

balance = 0

def main():
    print("Balance:", balance)
    deposite(100)
    withdraw(50)
    print("Balance:", balance)

def deposite(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount


if __name__ == "__main__":
    main()