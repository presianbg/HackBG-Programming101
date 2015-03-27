#!/usr/bin/python3.4
import sys
import math

n=int(sys.argv[1])
def sum_of_digits(n):
	s = 0
	n = abs(n)
	while n:
		s += n % 10
		n //= 10
	print (s)
	return s


if __name__ == '__main__':
	sum_of_digits(n)