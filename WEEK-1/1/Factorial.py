#!/usr/bin/python3.4
import sys
import math


n=int(sys.argv[1])
def factorial(n):
	f = 1
	if n == 0:
		return 1
	else:
		for i in range(n):
			f = f * (i+1)
		print (f)
		return f


factorial(n)