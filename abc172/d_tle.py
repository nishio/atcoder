#!/usr/bin/env python3

from functools import reduce
from operator import mul
from collections import defaultdict, Counter
from heapq import heappush, heappop
import sys
from math import sqrt, floor

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x)


def solve(N):
    "void()"
    px = [0] * (N + 1)
    primes = []
    divs = defaultdict(list)
    divs[1] = []

    for i in range(2, N + 1):
        if px[i] == 0:
            # prime
            primes.append(i)
#            divs[i] = [i]
            j = 2 * i
            while j <= N:
                px[j] = 1
                j += i

    # debug("num primes: len(primes)", len(primes))
    # 664579

    # numdivs = [0] * (N + 1)
    # numdivs[1] = 1
    # for i in range(2, N + 1):
    #     if not i in divs:
    #         ubound = floor(sqrt(i)) + 1
    #         for p in primes:
    #             if p > ubound:
    #                 break
    #             if i % p == 0:
    #                 divs[i] = [p] + divs[i // p]
    #                 break

    #     numdivs[i] = reduce(
    #         mul,
    #         (x + 1 for x in Counter(divs[i]).values()),
    #         1)

    # print(sum(i * numdivs[i] for i in range(1, N+1)))
    numdivs = [0] * (N + 1)
    numdivs[1] = 1
    #targets = [1]
    for p in primes:
        ubound = N // p
        for t in range(N, 0, -1):
            if t > ubound:
                continue
            if numdivs[t] == 0:
                continue
            cur = t
            cur *= p
            m = 2
            tnum = numdivs[t]
            while cur <= N:
                # debug(": cur", cur)
                numdivs[cur] = tnum * m
                m += 1
                # targets.append(cur)
                cur *= p
            # print(targets)
    # debug(": numdivs", numdivs)
    print(sum(i * numdivs[i] for i in range(1, N+1)))


def main():
    N = int(input())
    solve(N)


def _test():
    """
    >>> solve(4)
    23

    >>> solve(100)
    26879

    #>>> solve(10000000)
    #838627288460105
    """
    # solve(100000)  # 1m8.507s
    # solve(10000000)
    import doctest
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())
    input = f.readline
    read = f.read


USE_NUMBA = False
if (USE_NUMBA and sys.argv[-1] == 'ONLINE_JUDGE') or sys.argv[-1] == '-c':
    print("compiling")
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', solve.__doc__.strip().split()[0])(solve)
    cc.compile()
    exit()
else:
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read

    if (USE_NUMBA and sys.argv[-1] != '-p') or sys.argv[-1] == "--numba":
        # -p: pure python mode
        # if not -p, import compiled module
        from my_module import solve  # pylint: disable=all
    elif sys.argv[-1] == "-t":
        _test()
        sys.exit()
    elif sys.argv[-1] != '-p' and len(sys.argv) == 2:
        # input given as file
        input_as_file = open(sys.argv[1])
        input = input_as_file.buffer.readline
        read = input_as_file.buffer.read

    main()
