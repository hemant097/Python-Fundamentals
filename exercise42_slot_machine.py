#python slot machine
import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '🌟']
    # using the list comprehension, it will run 3 times, in each iteration will select a random symbol from the [] and add into a new[]
    return [ random.choice(symbols) for _ in range(0,3) ]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if(row[0]==row[1]==row[2]):
        #inside this if, we can check for either element, as all 3 are matching
        match(row[0]):
            case '🍒': return bet*3
            case '🍉': return bet*4
            case '🍋': return bet*5
            case '🔔': return bet*10
            case '🌟': return bet*20
        return bet
    # when all 3 are not matching
    return 0

def main():
    balance = 100;
    print("**************")
    print("Welcome to python slot machine")
    print("Symbols:🍒 🍉 🍋 🔔 🌟")
    print("**************")

    while (balance>0):
        print(f"current balance is ${balance}")
        bet = input("Place your bet amount: ")

        if(not bet.isdigit()):
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if(bet>balance):
            print("Insufficient funds")
            continue

        if(bet<=0):
            print("Bet must be positive and greater than 0")
            continue

        balance-=bet

        row = spin_row()
        print("Spinning....\n")

        print_row(row)
        payout = get_payout(row, bet)

        if(payout>0):
            print(f"You won ${payout}")
        else:
            print(f"Sorry , you lost this round")

        balance+=payout

        play_again = input("Do you want to spin again? (y/n): ").lower()
        if(play_again != "y"):
            break

    print("*****************")
    print(f"Game over! Your final balance is ${balance}")



if __name__ == "__main__":
    main()