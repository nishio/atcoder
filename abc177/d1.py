#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x):
    print(*x, file=sys.stderr)


def find_root(x):
    p = parent[x]
    if p == -1:
        return x
    p2 = find_root(p)
    parent[x] = p2
    return p2


def unite(x, y):
    x = find_root(x)
    y = find_root(y)
    if x == y:
        return  # already united
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


def is_connected(x, y):
    return (find_root(x) == find_root(y))


def solve(SOLVE_PARAMS):
    pass


def main():
    global parent, rank
    # parse input
    N, M = map(int, input().split())
    parent = [-1] * N
    rank = [0] * N
    for q in range(M):
        a, b = map(int, input().split())
        unite(a - 1, b - 1)

    xs = list(find_root(x) for x in range(N))
    # debug(": xs", xs)
    # print(len(set(xs)))
    from collections import Counter
    print(max(Counter(xs).values()))


# tests
T1 = """
5 3
1 2
3 4
5 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
4 10
1 2
2 1
1 2
2 1
1 2
1 3
1 4
2 3
2 4
3 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
4
"""

T3 = """
10 4
3 1
4 1
5 9
2 6
"""
TEST_T3 = """
>>> as_input(T3)
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
