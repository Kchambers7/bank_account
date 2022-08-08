
class BankAccount:

    def __init__(self, savingbalance, checkingbalance):
        self.savingbalance = savingbalance
        self.checkingbalance = checkingbalance

    def deposit(self, amount):
        self.checkingbalance += amount
        return self

   def deposit(self, amount):
        self.savingsbalance += amount
        return self

    def withdraw(self, amount):
        if self.checkingbalance >= amount:
            self.checkingbalance -= amount
        elif self.checkingbalance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.checkingbalance -= 5
        return self

    # def display_account_info(self):
    #     print(f"Balance: ${self.checkingbalance, self.savingsbalance}")

    def yield_interest(self):
        self.checkingbalance = self.checkingbalance * self.int_rate + self.checkingbalance
        return self

    def yield_interest(self):
        self.savingsbalance = self.savingsbalance * self.int_rate + self.savingsbalance
        return self

acct1 = BankAccount(0.05,500)
acct2 = BankAccount(0.1,1000)
acct1.deposit(300).deposit(100).deposit(200).withdraw(50).yield_interest().display_account_info()
acct2.deposit(500).deposit(500).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()