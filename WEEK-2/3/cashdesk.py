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
        cash = [self.__int__()]
        return cash

a = Bill(10)
b = Bill(5)
c = Bill(10)
print (c.banknotes())
print (a == b)
print (str(a))
money_holder = {}
money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1

print (money_holder)

##########################################################################


class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def banknotes(self):
        cash = []
        for bill in bills:
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


values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]
batch = BatchBill(bills)
for bill in batch:
    print(bill)

print (batch.banknotes(), "Echo")

print (batch.total())


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
        print (cash)
        for notes in cash:
            if notes in d:
                d[notes] += 1
            else:
                d[notes] = 1
        print (d)
        for note in sorted(list(d)):
            print ("%s $ bills - %s" % (note, d[note]))


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(Bill(10))
desk.take_money(batch)
desk.take_money(Bill(600))
desk.take_money(Bill(200))
desk.take_money(Bill(1))

print(desk.total())
desk.inspect()
