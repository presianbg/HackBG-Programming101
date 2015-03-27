#!/usr/bin/python3


def prepare_meal(number):
    spam = []
    meal = ""
    n = 0
    while 3 ^ n <= number:
        if (3 ** n) != 0:
            if number % (3 ** n) == 0:
                spam.append(n)
        n += 1
    meal += "spam "*max(spam)
    if number % 5 == 0 and meal != '':
        meal += "and eggs"
    elif number % 5 == 0:
        meal += "eggs"
    return meal


if __name__ == '__main__':
    number = 45
    print (prepare_meal(number))
