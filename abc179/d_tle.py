#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 998244353


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, SS):
    count = [-1] * (N + 10)
    count[0] = 1

    def f(pos):
        # debug("pos", pos)
        if pos < 0:
            return 0
        if count[pos] > -1:
            return count[pos]
        ret = 0
        for left, right in SS:
            for i in range(left, right + 1):
                j = pos - i
                if j < 0:
                    continue
                r = f(j)
                count[j] = r
                ret += r

        return ret % MOD

    ret = f(N - 1)
    # debug("count", count)
    return ret % MOD


def main():
    # parse input
    N, K = map(int, input().split())
    SS = []
    for i in range(K):
        SS.append(tuple(map(int, input().split())))
    print(solve(N, K, SS))


# tests
T1 = """
5 2
1 1
3 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
5 2
3 3
5 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

T3 = """
5 1
1 2
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
5
"""

T4 = """
60 3
5 8
1 3
10 15
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
221823067
"""

T5 = """
10 1
1 2
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
55
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
