#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve():
    from collections import defaultdict
    H, W, M = map(int, input().split())
    hcount = defaultdict(int)
    wcount = defaultdict(int)
    bombs = set()
    for _i in range(M):
        h, w = map(int, input().split())
        hcount[h] += 1
        wcount[w] += 1
        bombs.add((h, w))

    maxh = max(hcount.values())
    maxw = max(wcount.values())
    hs = [k for k in hcount if hcount[k] == maxh]
    ws = [k for k in wcount if wcount[k] == maxw]
    if len(hs) * len(ws) > M:
        return maxh + maxw
    for h in hs:
        for w in ws:
            if (h, w) not in bombs:
                return maxh + maxw
    return maxh + maxw - 1


def main():
    print(solve())


# tests
T1 = """
2 3 3
2 2
1 1
1 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
3 3 4
3 3
3 1
1 1
1 2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
3
"""

T3 = """
5 5 10
2 5
4 3
2 3
5 5
2 2
5 4
5 3
5 1
3 5
1 4
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
6
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
