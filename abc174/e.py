#!/usr/bin/env python3
import math
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, AS):
    left = 0
    right = max(AS) + 1

    while left < right - 1:
        mid = (left + right) // 2
        s = sum(a // mid - 1 if a >= mid else 0 for a in AS)
        debug(": ", mid, s)
        if s >= K:
            left = mid
        else:
            right = mid

    x = left
    debug("x: x", x)
    #v = max(a / (a // x + 1 if a >= x else 1) for a in AS)
    # v = max(x + (a % x) / (a // x) if a >= x else a for a in AS)
    queue = []

    leftK = 0
    for i in range(N):
        a = AS[i]
        numDivide = a // x
        leftK += numDivide
        length = a / (numDivide + 1) if numDivide else a
        queue.append((length, numDivide, a))
    debug(": leftK", leftK)
    queue.sort()
    from heapq import heappush, heappop
    for i in range(leftK - K):
        # dec numDivide
        (length, numDivide, a) = heappop(queue)
        numDivide -= 1
        debug(": a, numD", a, numDivide)
        length = a / (numDivide + 1) if numDivide else a
        if numDivide:
            heappush(queue, (length, numDivide, a))
        debug(": length", length)

    return math.ceil(length)
    # return math.ceil(left)


def solve(N, K, AS):
    left = 0
    right = max(AS)

    while left < right - 1:
        mid = (left + right) // 2
        s = sum((a - 1) // mid for a in AS)
        # debug(": ", mid, s)
        if s > K:
            left = mid
        else:
            right = mid
    return right


def main():
    # parse input
    N, K = map(int, input().split())
    AS = list(map(int, input().split()))
    print(solve(N, K, AS))


# tests
T1 = """
2 3
7 9
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
3 0
3 4 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
"""

T3 = """
10 10
158260522 877914575 602436426 24979445 861648772 623690081 433933447 476190629 262703497 211047202
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
292638192
"""

T4 = """
2 1
4 2
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
2
"""

T5 = """
2 1
5 2
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
3
"""

T6 = """
2 1
3 2
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
2
"""

T7 = """
2 2
3 2
"""
TEST_T7 = """
>>> as_input(T7)
>>> main()
2
"""

T8 = """
2 2
3 1
"""
TEST_T8 = """
>>> as_input(T8)
>>> main()
1
"""

T9 = """
3 1
3 4 5
"""
TEST_T9 = """
>>> as_input(T9)
>>> main()
4
"""

T10 = """
3 2
3 4 5
"""
TEST_T10 = """
>>> as_input(T10)
>>> main()
3
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


input = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

if sys.argv[-1] == "-t":
    print("testing")
    _test()
    sys.exit()

main()
