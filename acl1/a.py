#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


# included from libs/unionfind.py
"""
Union-Find Tree / Disjoint Set Union (DSU)
"""


def init_unionfind(N):
    global parent, rank, NUM_VERTEX
    NUM_VERTEX = N
    parent = [-1] * N
    rank = [0] * N


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


def num_components():
    return len(set(find_root(x) for x in range(NUM_VERTEX)))


# end of libs/unionfind.py
def solve(N, YS, XS):
    from collections import Counter
    group = [None] * N
    init_unionfind(N)
    group_to_rightmost = {}
    for i in range(N):
        y0 = YS[i]
        if y0 is None:
            continue
        group[i] = i
        rightmost = i
        for j in range(i + 1, N):
            y = YS[j]
            if y is None:
                continue
            if y > y0:
                # add to group
                group[j] = i
                rightmost = j
                YS[j] = None
        for g in group_to_rightmost:
            r = group_to_rightmost[g]
            if i < r:
                unite(i, g)
                if rightmost < r:
                    rightmost = r

        group_to_rightmost[find_root(i)] = rightmost

    roots = [find_root(group[i]) for i in range(N)]
    count = Counter(roots)
    return [count[roots[x]] for x in XS]


def main():
    # parse input
    N = int(input())
    YS = [0] * N
    XS = []
    for _i in range(N):
        x, y = map(int, input().split())
        YS[x - 1] = y - 1
        XS.append(x - 1)

    print(*solve(N, YS, XS), sep="\n")


# tests
T1 = """
4
1 4
2 3
3 1
4 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
1
2
2
"""

T2 = """
7
6 4
4 3
3 5
7 1
2 7
5 2
1 6
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
3
3
1
1
2
3
2
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
