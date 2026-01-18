balance_bank = 0

def deposit():
    global balance_bank
    try:
        deposit1 = int(input("Enter the amount you want to deposit: $ "))
        if deposit1 > 0:
            balance_bank += deposit1
        else:
            print("Invalid deposit amount.")
    except ValueError:
        print("Invalid amount. Please enter numbers only.")


def withdraw():
    global balance_bank
    a = input("Would you like to withdraw? (Y/N): ").capitalize()
    if a == "Y":
        try:
            withdraw1 = int(input("How much would you like to withdraw? $ "))
            if withdraw1 > 0 and withdraw1 <= balance_bank:
                balance_bank -= withdraw1
            else:
                print("Insufficient or invalid balance.")
        except ValueError:
            print("Invalid amount. Please enter numbers only.")


def show_balance():
    print(f"Your current balance is $ {balance_bank}")


deposit()
withdraw()
show_balance()
