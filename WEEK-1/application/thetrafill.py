#!/usr/bin/python
import argparse
import math


def fill_tetrahedron():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-a', nargs="+", type=int)
    parser.add_argument('-l', nargs=1, type=int)
    args = parser.parse_args()

    i = len(args.a)
    print "Number of tetrahedron s: %d" % i
    print "Availabe amout of water is: %d liters" % args.l[0]

    if args.l[0] == 0:
        print "There is no WATER!?"
    else:
        lok = []
        x = 0
        while (x < i):
            print "The edge of tetrahedron #%d is: %d cm" % (x + 1, args.a[x])
            v = pow(args.a[x], 3) / (6 * math.sqrt(2))
            l = round(v / 1000, 2)
            if l > args.l[0]:
                print "The Volume of tetrahedron #%d is %f liters and it's above available %f liters" % (x + 1, l, args.l[0])
            else:
                print "The Volume of tetrahedron #%d is %f liters - OK" % (x + 1, l)
                lok.append(l)
            x += 1

        f = len(lok)

        if f != 0:
            for passnum in range(len(lok) - 1, 0, -1):
                for j in range(passnum):
                    if lok[j] > lok[j + 1]:
                        temp = lok[j]
                        lok[j] = lok[j + 1]
                        lok[j + 1] = temp
            k = 0
            ld = 0
            while (k < f):
                if ld < args.l[0]:
                    ld += lok[k]
                    if ld < args.l[0]:
                        k += 1
                    else:
                        ld -= lok[k]
                        print "We could fill maximum %d tetrahedron with %f liters of water" % (k, ld)
                        break
            if k == f:
                print "We could fill all %d tetrahedron with ~ %f liters of water" % (k, ld)
        else:
            print "There is no suitable tetrahedrons to fill."
fill_tetrahedron()
