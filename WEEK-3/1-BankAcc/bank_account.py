#!/usr/bin/python3
import datetime


class BankAccount:

    def __init__(self, name, balance, currency):
        if not ((type(name) and type(currency) is str) and type(balance) is int or float):
            raise TypeError
        if balance < 0:
            raise ValueError
        self.name = name
        self.balance = balance
        self.currency = currency
        self.history = []
        self.history.append("{}: Acount was Created".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M")))

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        return round(self.balance)

    def deposit_amount(self, amount):
        if amount < 0:
            raise ValueError
        self.balance += amount
        self.history.append("{}: Deposited -> {}{}".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"), amount, self.currency))
        return amount

    def check_balance(self):
        self.history.append("{}: Balance Check ->  {}{}".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"), self.balance, self.currency))
        return self.balance

    def withdraw(self, amount):
        if type(amount) is int and (self.balance > amount) and amount > 0:
            self.balance -= amount
            self.history.append("{}: Withdrawed ->  {}{}".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"), amount, self.currency))
            return True
        else:
            self.history.append("{}: Withdraw Failed for ->  {}{}".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"), amount, self.currency))
            return False

    def transffering_to(self, acc, amount):
        if not(type(acc) is BankAccount):
            raise TypeError
        if self.currency != acc.currency or self.balance < amount:
            print ("Not enough minerals or different currency")
            raise ValueError
        if amount <= 0:
            self.history.append("{}: Transfer to {} Failed ->  {}{}".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"), acc.name, amount, self.currency))
            return False
        self.balance -= amount
        self.history.append("{}: Transfer to {} for ->  {}{}".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"), acc.name, amount, self.currency))
        acc.balance += amount
        acc.history.append("{}: Transfer from {} for ->  {}{}".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M"), self.name, amount, acc.currency))
        return True

    def get_history(self):
        for ivent in self.history:
            print (ivent)


def main():
    rado = BankAccount("Rado", 30, "$")
    ivo = BankAccount("Ivo", 5, "$")
    rado.deposit_amount(10.99)
    rado.withdraw(5)
    print (rado.check_balance())
    print (rado)
    print (int(rado))
    rado.transffering_to(ivo, 5.89)
    print (int(ivo))
    print (int(rado))
    ivo.get_history()
    print ("------------------------------")
    rado.get_history()

if __name__ == '__main__':
    main()
