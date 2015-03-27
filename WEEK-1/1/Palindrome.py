#!/usr/bin/python3.4
import sys

obj = sys.argv[1:]
def palindrome(obj):
    s = ' '.join(obj)
    if s[::-1].lower() == s.lower():
        print ("It is palindrome!")
        return True
    else:
        print ("It is not a palindrome!")
        return False

if __name__ == '__main__':
    palindrome(obj)