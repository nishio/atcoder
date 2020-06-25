#!/usr/bin/env python3
import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
# INF = sys.maxsize
INF = 10 ** 27 + 1
# INF = float("inf")


def dp(*x):  # debugprint
    print(*x)


def solve(N, A, B, C, D):
    to_visit = [-N]
    cost = {N: 0}

    def put(n, c):
        cost[n] = min(cost.get(n, INF), c)
        heappush(to_visit, -n)

    visited = N + 1
    while to_visit:
        n = -heappop(to_visit)
        if n == visited:
            continue

        visited = n
        c = cost[n]
        put(0, c + n * D)

        if n % 2 == 0:
            put(n // 2, c + A)
        else:
            put((n+1) // 2, c + A + D)
            put((n-1) // 2, c + A + D)

        if n % 3 == 0:
            put(n // 3, c + B)
        elif n % 3 == 1:
            put((n-1) // 3, c + B + D)
            put((n+2) // 3, c + B + D * 2)
        else:
            put((n+1) // 3, c + B + D)
            put((n-2) // 3, c + B + D * 2)

        if n % 5 == 0:
            put(n // 5, c + C)
        elif n % 5 == 1:
            put((n-1) // 5, c + C + D)
            put((n+4) // 5, c + C + D * 4)
        elif n % 5 == 2:
            put((n-2) // 5, c + C + D * 2)
            put((n+3) // 5, c + C + D * 3)
        elif n % 5 == 3:
            put((n+2) // 5, c + C + D * 2)
            put((n-3) // 5, c + C + D * 3)
        elif n % 5 == 4:
            put((n+1) // 5, c + C + D)
            put((n-4) // 5, c + C + D * 4)

    return cost[0]


def main():
    """
    >>> solve(4, 1000000000, 1000000000, 1000000000, 1)
    4
    >>> solve(4, 1, 1000000000, 1000000000, 1)
    3
    >>> solve(8, 1, 1000000000, 1000000000, 1)
    4
    """
    T = int(input())
    for t in range(T):
        print(solve(*[int(x) for x in input().split()]))


def _test():
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
