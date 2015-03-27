#!/usr/bin/python3


def is_prime(n):
    n = abs(n)
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    if n > 2 and n % 2 == 0:
        ps = []
        p = [x for x in range(n+1) if is_prime(x)]
        while len(p) > 0:
            rest = n - p[0]
            if rest in p:
                ps.append((p[0], rest))
                p.remove(rest)
                if len(p) == 0:
                    break
            p.remove(p[0])
        return ps
    else:
        return False


if __name__ == '__main__':
    n = 22
    print(goldbach(n))
