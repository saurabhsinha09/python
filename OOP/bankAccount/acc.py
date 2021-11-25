class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath) as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

#account = Account("balance.txt")    
#print(account.balance)
#account.withdraw(250)
#print(account.balance)
#account.deposit(100)
#print(account.balance)
#account.commit()

class Checking(Account):
    
    """This class generates checking account objects"""

    type="checking"

    def __init__(self, filepath, fees):
        Account.__init__(self, filepath)
        self.fee = fees

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking("balance.txt", 1)
print(checking.__doc__)
print(checking.balance)
print(checking.type)
checking.transfer(50)
checking.commit()

