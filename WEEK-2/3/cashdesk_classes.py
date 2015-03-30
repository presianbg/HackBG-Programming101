#!/usr/bin/python3


class Bill:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return "A {}$ bill".format(self.amount)

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(str(self.amount ^ 128))

    def banknotes(self):
        return [self.__int__()]
##########################################################################


class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def banknotes(self):
        cash = []
        for bill in self.bills:
            cash.append(int(bill))
        return cash

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, key):
        return self.bills[key]

    def __int__(self):
        return self.total()

    def total(self):
        total = 0
        for bill in self.bills:
            total += int(bill)
        return total


class CashDesk:
    def __init__(self):
        self.vault = []

    def take_money(self, money):
        self.vault.append(money)

    def total(self):
        total_money = 0
        for money in self.vault:
            total_money += int(money)
        return total_money

    def inspect(self):
        cash = []
        d = {}
        for bill in self.vault:
            cash += bill.banknotes()
        for notes in cash:
            if notes in d:
                d[notes] += 1
            else:
                d[notes] = 1
        for note in sorted(list(d)):
            print ("%s $ bills - %s" % (note, d[note]))
