import numba
from math import sqrt


def precompute1(maxAS=1000000):
    eratree = [0] * (maxAS + 1)
    for p in range(2, maxAS + 1):
        if eratree[p]:
            continue
        # p is prime
        eratree[p] = p
        x = p * p
        while x <= maxAS:
            if not eratree[x]:
                eratree[x] = p
            x += p
    return eratree


# @numba.njit
def precompute(maxAS=1000000):
    eratree = [0] * (maxAS + 1)
    for p in range(2, int(sqrt(maxAS)) + 1):
        if eratree[p]:
            continue
        # p is prime
        x = p * p
        while x <= maxAS:
            if not eratree[x]:
                eratree[x] = p
            x += p
    return eratree


eratree = []


def factor(a):
    factors = []
    while a > 1:
        d = eratree[a]
        if not d:
            factors.append(a)
            break
        factors.append(d)
        a //= d
