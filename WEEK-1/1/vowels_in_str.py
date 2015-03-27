#!/usr/bin/python3.4
import sys

sttt = str(sys.argv[1])
def count_vowels(sttt):
    v = 0
    c = 0
    for i in sttt:
        if i.lower() in 'aeiouy':
            v +=1
        elif i.lower() in 'bcdfghjklmnpqrstvwxz':
            c +=1
    print ("The number of Vowels in this string are %d" %v)
    print ("The number of Consonants in this string are %d" %c)
    return (v, c)

if __name__ == '__main__':
    count_vowels(sttt)