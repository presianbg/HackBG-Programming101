#!/usr/bin/python3


def to_digits(n):
    return [int(x) for x in str(n)]


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(digits):
    n = 0
    for i in digits:
        dc = count_digits(i)
        n = n*(10**dc) + i
    return n


def is_credit_card_valid(number):
    d = to_digits(number)
    if len(d) % 2 != 0:
        g = [x*2 for x in d[1::2]]
        return (sum(to_digits(to_number(g + d[0::2])))) % 10 == 0
    else:
        return False


if __name__ == '__main__':
    number = 79927398713
    print(is_credit_card_valid(number))
