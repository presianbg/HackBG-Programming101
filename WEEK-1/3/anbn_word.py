#!/usr/bin/python3
import re


def is_an_bn(word):
    if word.count('a') == word.count('b'):
        n = word.count('a')
        result = re.search('^a{' + str(n) + '}b{' + str(n) + '}$', word)
        if result:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    word = "aaabbb"
    print(is_an_bn(word))
