#!/usr/bin/python
import sys
import math

num=float(sys.argv[1])
def fill_tetrahedron(num):
	print "Edge is:", num
	v=pow(num,3)/(6*math.sqrt(2))
	l=round(v/1000,2)

	print "You can fill Regular tetrahedron with edge of %s cm with %s liters of water " % (num, l)

fill_tetrahedron(num)