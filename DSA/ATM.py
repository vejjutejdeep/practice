class Atm:
    def __init__(self, account_no):
        self.account_no = account_no
        self.balance = 0

    def check_balance(self):
        return self.balance
    
    def withdraw(self, withdrawn_amout):
        if self.check_balance() > withdrawn_amout:
            self.balance -= withdrawn_amout
            return withdrawn_amout
        else:
            return "amount Insuffcient"
    
    def deposit(self, deposit_amount):

        self.balance +=  deposit_amount
        return self.check_balance()

Atm1 = Atm("12345123")
print(Atm1.deposit(100))
print(Atm1.check_balance())
print(Atm1.withdraw(10))
print(Atm1.check_balance())