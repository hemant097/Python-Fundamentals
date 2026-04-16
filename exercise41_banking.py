


def show_balance(balance):
    print("******************")
    print(f"Your current balance is ${balance:.2f}")
    print("******************")

def deposit():
    print("******************")
    deposit_amount = float(input("Enter the amount to deposit: "))
    print("******************")

    if(deposit_amount < 0) :
        print("******************")
        print("Invalid amount")
        print("******************")
        return 0
    else:
        return deposit_amount

def withdraw(balance):
    print("******************")
    amount = float(input("Enter the amount to withdraw: "))
    print("******************")

    if(amount > balance):
        print("******************")
        print("Insufficient funds")
        print("******************")
        return 0
    elif(amount < 0):
        print("******************")
        print("Amount must be > 0")
        print("******************")
        return 0
    else:
        return amount

def main():
    balance=0
    is_runnning=True

    while is_runnning:
        print("******************")
        print("Welcome to the banking program")
        print("******************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("******************")

        choice = int(input("Enter your choice (1-4): "))

        match(choice):
            case 1:
                show_balance(balance)
            case 2:
                balance+=deposit()
            case 3:
                balance-=withdraw(balance)
            case 4:
                is_runnning = False
            case _:
                print("Invalid choice")

    print("Thank you for using this program")

if __name__=="__main__":
    main()
