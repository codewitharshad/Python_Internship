
balance = 50000

def add_money(balance):
    amount = float(input("Enter amount to add: "))
    balance += amount
    print("Updated Balance:", balance)
    return balance

def spend_money(balance):
    amount = float(input("Enter amount to spend: "))
    if amount <= balance:
        balance -= amount
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance")
    return balance

while True:
    print("Add Money")
    print("Spend Money")
    print("Check Balance")
    print("Exit")

    choice = input("Enter choice: ").lower()

    if choice == "add money":
        balance = add_money(balance)

    elif choice == "spend money":
        balance = spend_money(balance)

    elif choice == "check balance":
        print("Current Balance:", balance)

    elif choice == "exit":
        break

    else:
        print("Invalid Choice")
