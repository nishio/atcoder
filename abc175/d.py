#!/usr/bin/env python3
import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def solve(N, K, PS, CS):
    PS = [x - 1 for x in PS]
    CS = [CS[PS[i]] for i in range(N)]
    visited = {}
    loops = []
    loopScore = []
    for i in range(N):
        loop = []
        c = 0
        while i not in visited:
            visited[i] = True
            c += CS[i]
            i = PS[i]
            loop.append(i)
        if loop:
            loops.append(loop)
            loopScore.append(c)

    pos = list(range(N))
    ret = -INF
    for i, loop in enumerate(loops):
        if loopScore[i] > 0:
            baseScore = loopScore[i] * (K // len(loop))
            r = K % len(loop)
            if r == 0:
                r = len(loop)
                baseScore -= loopScore[i]
            maxscore = 0
            scores = defaultdict(int)
            for i in range(r):
                for x in loop:
                    scores[x] += CS[pos[x]]
                    pos[x] = PS[pos[x]]
                maxscore = max(maxscore, max(scores.values()))
            ret = max(maxscore + baseScore, ret)
        else:
            r = len(loop)
            maxscore = -INF
            scores = defaultdict(int)
            for i in range(r):
                for x in loop:
                    scores[x] += CS[pos[x]]
                    pos[x] = PS[pos[x]]
                maxscore = max(maxscore, max(scores.values()))
            ret = max(maxscore, ret)

    return ret


def main():
    # parse input
    N, K = map(int, input().split())
    PS = list(map(int, input().split()))
    CS = list(map(int, input().split()))
    print(solve(N, K, PS, CS))


# tests
T1 = """
5 2
2 4 5 1 3
3 4 -10 -8 8
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
8
"""

T2 = """
2 3
2 1
10 -7
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
13
"""

T3 = """
3 3
3 1 2
-1000 -2000 -3000
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
-1000
"""

T4 = """
10 58
9 1 6 7 8 4 3 2 10 5
695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
29507023469
"""

T5 = """
3 1000
2 3 1
1 0 2
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
1001
"""

T6 = """
3 1000
2 3 1
1 1 -3
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
2
"""

T7 = """
4 1000
2 1 4 3
1 1 -10000 10000
"""
TEST_T7 = """
>>> as_input(T7)
>>> main()
10000
"""

T8 = """
4 1000
2 1 4 3
1 1 -10000 10001
"""
TEST_T8 = """
>>> as_input(T8)
>>> main()
10500
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
