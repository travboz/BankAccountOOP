class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None

        if amountToDeposit < 0:
            print("You cannot deposit a negative amont")
            return None

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None

        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None

        if amountToWithdraw > self.balance:
            print("You cannot withdraw more than you have in your account")
            return None

        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        return self.balance

    def show(self):
        print(" Name:", self.name)
        print(" Balance:", self.balance)
        print(" Password:", self.password)
        print()


# driver code
# oAccount = Account("Joe Schmidt", 1000, "hello_world")

# newBalance = oAccount.deposit(500, "hello_world")
# oAccount.withdraw(250, "hello_world")
# currentBalance = oAccount.getBalance("hello_world")

# oAccount.show()
