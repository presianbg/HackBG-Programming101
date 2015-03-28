#!/usr/bin/python3
from cashdesk_classes import Bill, BatchBill, CashDesk


def main():
    values = [10, 20, 50, 100, 100, 100, 20, 500]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(Bill(10))
    desk.take_money(batch)
    desk.take_money(Bill(500))
    desk.take_money(Bill(100))
    desk.take_money(Bill(1000))

    print("Total in da BANK =  %s$" % desk.total())
    desk.inspect()

if __name__ == '__main__':
    main()
