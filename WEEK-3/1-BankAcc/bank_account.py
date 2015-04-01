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
        self.history.append("{}: Acount was Created".format(self.get_timestamp()))

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        return round(self.balance)

    def deposit_amount(self, amount):
        if amount < 0:
            raise ValueError
        self.balance += amount
        self.history.append("{}: Deposited -> {}{}".format(self.get_timestamp(), amount, self.currency))
        return amount

    def check_balance(self):
        self.history.append("{}: Balance Check ->  {}{}".format(self.get_timestamp(), self.balance, self.currency))
        return self.balance

    def withdraw(self, amount):
        if type(amount) is int and (self.balance > amount) and amount > 0:
            self.balance -= amount
            self.history.append("{}: Withdrawed ->  {}{}".format(self.get_timestamp(), amount, self.currency))
            return True
        else:
            self.history.append("{}: Withdraw Failed for ->  {}{}".format(self.get_timestamp(), amount, self.currency))
            return False

    def transffering_to(self, acc, amount):
        if not(type(acc) is BankAccount):
            raise TypeError
        if self.currency != acc.currency or self.balance < amount:
            print ("Not enough minerals or different currency")
            raise ValueError
        if amount <= 0:
            self.history.append("{}: Transfer to {} Failed ->  {}{}".format(self.get_timestamp(), acc.name, amount, self.currency))
            return False
        self.balance -= amount
        self.history.append("{}: Transfer to {} for ->  {}{}".format(self.get_timestamp(), acc.name, amount, self.currency))
        acc.balance += amount
        acc.history.append("{}: Transfer from {} for ->  {}{}".format(self.get_timestamp(), self.name, amount, acc.currency))
        return True

    def get_history(self):
        for ivent in self.history:
            print (ivent)

    def get_timestamp(self):
        timestamp = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        return timestamp
