#!/usr/bin/env python3

# from collections import defaultdict
# from heapq import heappush, heappop
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")


def debug(*x):
    print(*x, file=sys.stderr)


cdef long[3000 * 3000] memo
cdef int[3000 * 3000] done

cdef first(L, R):
    if L == R:
        return XS[L]
    pos = L * N + R
    if done[pos + N]:
        right = memo[pos + N]
    else:
        right = first(L + 1, R)

    if done[pos - 1]:
        left = memo[pos - 1]
    else:
        left = first(L, R - 1)

    ret = XS[L] - right
    x = XS[R] - left
    if x > ret:
        ret = x
    memo[pos] = ret
    done[pos] = True
    return ret


cdef solve():
    for i in range(N * N):
        memo[i] = 0
        done[i] = False

    return first(0, N - 1)


def main():
    global N, XS
    # parse input
    N = int(input())
    XS = list(map(int, input().split()))
    print(solve())


# tests
T1 = """
4
10 80 90 30
"""


def test_T1():
    """
    >>> as_input(T1)
    >>> main()
    10
    """


T2 = """
3
10 100 10
"""


def test_T2():
    """
    >>> as_input(T2)
    >>> main()
    -80
    """


T3 = """
1
10
"""


def test_T3():
    """
    >>> as_input(T3)
    >>> main()
    10
    """


T4 = """
10
1000000000 1 1000000000 1 1000000000 1 1000000000 1 1000000000 1
"""


def test_T4():
    """
    >>> as_input(T4)
    >>> main()
    4999999995
    """


T5 = """
6
4 2 9 7 1 5
"""


def test_T5():
    """
    >>> as_input(T5)
    >>> main()
    2
    """
# add tests above


def _test():
    import doctest
    doctest.testmod()


def as_input(s):
    "use in test, use given string as input file"
    import io
    global read, input
    f = io.StringIO(s.strip())

    def input():
        return bytes(f.readline(), "ascii")

    def read():
        return bytes(f.read(), "ascii")


main()
