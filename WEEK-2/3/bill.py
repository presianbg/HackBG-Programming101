#!/usr/bin/python3
from cashdesk_classes import Bill


def main():
    a = Bill(10)
    b = Bill(5)
    c = Bill(10)
    print (int(a))
    print (a == c)
    print (str(a))
    print (b)
    money_holder = {}
    money_holder[a] = 1

    if c in money_holder:
        money_holder[c] += 1
    print(money_holder)


if __name__ == '__main__':
    main()
