#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve0(N, AS):
    ret = 0
    for i in range(N):
        for j in range(i + 1, N):
            if AS[i] * AS[j] % 1000000000_000000000 == 0:
                # debug(": AS[i], AS[j]", AS[i], AS[j])
                ret += 1
    return ret


def solve1(N, AS):
    ret = 0
    P2 = []
    P5 = []
    for i in range(N):
        p2 = 0
        p5 = 0
        x = AS[i]
        while x % 2 == 0:
            p2 += 1
            x //= 2
        while x % 5 == 0:
            p5 += 1
            x //= 5
        P2.append(p2)
        P5.append(p5)
    # debug(": P2, P5", P2, P5)
    for i in range(N):
        for j in range(i + 1, N):
            if P2[i] + P2[j] > 17 and P5[i] + P5[j] > 17:
                # debug(": AS[i], AS[j]", AS[i], AS[j])
                ret += 1
    return ret


def solve(N, AS):
    import numpy as np
    ret = 0
    # P = [[0] * 14 for i in range(14)]
    P2 = []
    P5 = []
    P = np.zeros((20, 20), dtype=np.int)

    for i in range(N):
        p2 = 0
        p5 = 0
        x = AS[i]
        while x % 2 == 0:
            p2 += 1
            x //= 2
        while x % 5 == 0:
            p5 += 1
            x //= 5
        P2.append(p2)
        P5.append(p5)
        P[p2, p5] += 1

    for i in range(19, 0, -1):
        P[i - 1] += P[i]
    for i in range(19, 0, -1):
        P[:, i - 1] += P[:, i]

    for i in range(N):
        ret += P[18 - P2[i], 18 - P5[i]]
    ret -= P[9, 9]
    ret //= 2
    return ret


def main():
    # parse input
    N = int(input())
    AS = []
    for i in range(N):
        s = input().strip()
        try:
            v = int(s) * 1000000000
        except:
            s1, s2 = s.split(b".")
            s2 = s2 + b"0" * (9 - len(s2))
            v = int(s1) * 1000000000 + int(s2)
        # print(v)
        AS.append(v)
    print(solve(N, AS))


# tests
T1 = """
5
7.5
2.4
17.000000001
17
16.000000000
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
11
0.9
1
1
1.25
2.30000
5
70
0.000000001
9999.999999999
0.999999999
1.000000001
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
8
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            doctest.run_docstring_examples(g[k], g)


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
