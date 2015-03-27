#!/usr/bin/python3.4
import sys
import math


n=int(sys.argv[1])
def fibonachi(n):
	f = list()
	if (n == 0 or n == 1):
		f = 1
		s = 0
		print (f)
	else:
		for i in range(n):
			if i == 0 or i == 1:
				f.append(1)
			else:
				s = f[i-1] + f[i-2]
				f.append(s)
		print (f)
		return f
		

if __name__ == '__main__':
    fibonachi(n)

