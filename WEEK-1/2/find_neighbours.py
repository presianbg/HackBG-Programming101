#!/usr/bin/python3


def find_neighbors(xb, yb, X, Y):
    return [(x2, y2) for x2 in range(xb - 1, xb + 2)
            for y2 in range(yb - 1, yb + 2)
            if (-1 < xb <= X and
                -1 < yb <= Y and
                (xb != x2 or yb != y2) and
                (0 <= x2 <= X) and
                (0 <= y2 <= Y))]

if __name__ == '__main__':
    print(find_neighbors(1, 3, 3, 3))
