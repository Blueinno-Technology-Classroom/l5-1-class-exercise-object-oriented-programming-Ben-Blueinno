##################################################
'''
Q1a: 
'''
{'x': 9, 'y': 2}
##################################################
'''
Q1b: 
'''
{'x': 27, 'y': 2}
##################################################
'''
Q2:
'''


class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


name = Name('Jhon', 'Wick')
##################################################
'''
Q3:
'''


class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def normal_order(self):
        print(self.first_name, self.last_name)

    def reverse_order(self):
        print(self.last_name, self.first_name)


name = Name('Jhon', 'Wick')
name.normal_order()
name.reverse_order()
##################################################
'''
Q4:
'''


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


##################################################
'''
Q5:
'''


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit: {amount}, Lastestbalance: {self.balance}')

    def withdraw(self, amount):
        self.balance -= amount
        print(f'Withdraw: {amount}, Lastestbalance: {self.balance}')


myAccount = BankAccount('Jhon', 100)
myAccount.deposit(100.5)
myAccount.withdraw(45.5)
##################################################
'''
Q6:
'''


##################################################
'''
Q7:
'''


##################################################
