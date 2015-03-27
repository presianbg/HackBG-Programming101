#!/usr/bin/python
import sys, argparse
import math

def caesar_encrypt():

    parser = argparse.ArgumentParser(description='Process some strings.')
    parser.add_argument('-a', type=str)
    parser.add_argument('-k', nargs=1 , type=int, choices=xrange(0, 26))
    args = parser.parse_args()

    cipher = str()
    print "Your string is: %s" % args.a
    for passnum in range(len(args.a)):
        if args.a[passnum].isalpha() == True:
            n = ord(args.a[passnum])
            n += args.k[0]

            if args.a[passnum].isupper():
                if n > ord('Z'):
                    n -= 26
                elif n < ord('A'):
                    n +=26
            elif args.a[passnum].islower():
                if n > ord('z'):
                    n -= 26
                elif n < ord('a'):
                    n += 26
            cipher += chr(n)
        else:
            cipher += args.a[passnum]
    print "Your Ceasar coded string is: %s" % cipher

caesar_encrypt()
