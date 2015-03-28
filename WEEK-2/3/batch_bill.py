#!/usr/bin/python3
from cashdesk_classes import Bill, BatchBill


def main():
    values = [10, 20, 50, 100, 500]
    bills = [Bill(value) for value in values]
    batch = BatchBill(bills)

    for bill in batch:
        print(bill)

    print (batch.total())

if __name__ == '__main__':
    main()
