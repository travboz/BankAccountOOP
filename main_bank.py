# main program controlling a Bank made up of Accounts

from Bank import *

# create a bank
aBank = Bank()

# Main code
joesAccountNumber = aBank.createAccount("Joe", 100, "JoesPassword")
print("Joe's account number is:", joesAccountNumber)

marysAccountNumber = aBank.createAccount("Mary", 12345, "MarysPassword")
print("Mary's account number is:", marysAccountNumber)

while True:
    print()

    print("To get an account balance, press b")
    print("To close an account, press c")
    print("To make a deposit, press d")
    print("To open a new account, press o")
    print("To quit, press q")
    print("To show all accounts, press s")
    print("To make a withdrawal, press w ")
    print()

    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0]
    print()

    if action == "b":
        aBank.balance()
    elif action == "c":
        aBank.closeAccount()
    elif action == "d":
        aBank.deposit()
    elif action == "o":
        aBank.openAccount()
    elif action == "s":
        aBank.show()
    elif action == "q":
        break
    elif action == "w":
        aBank.withdraw()
    else:
        print("Sorry, that was not a valid action. Please try again.")

print("Done")
