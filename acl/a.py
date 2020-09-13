#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
INF = 10 ** 9 + 1  # sys.maxsize # float("inf")
MOD = 10 ** 9 + 7

# dsu / UnionFind


def init_unionfind(N):
    global parent, rank
    parent = [-1] * N
    rank = [0] * N


def find_root_1(x):
    p = parent[x]
    if p == -1:
        return x
    p2 = find_root(p)
    parent[x] = p2
    return p2


def find_root(x):
    p = parent[x]
    while p != -1:
        x = p
        p = parent[x]
    return x


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

# acl/dsu


init = init_unionfind
merge = unite
# FIXME: return value

same = is_connected
leader = find_root


def size(a):
    raise NotImplementedError


def group(a):
    raise NotImplementedError
# ---


def debug(*x):
    print(*x, file=sys.stderr)


def main():
    # parse input
    N, Q = map(int, input().split())
    init(N)
    for _q in range(Q):
        q, u, v = map(int, input().split())
        if q == 0:
            merge(u, v)
        else:
            print(int(same(u, v)))


# tests
T1 = """
4 7
1 0 1
0 0 1
0 2 3
1 0 1
1 1 2
0 0 2
1 1 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
0
1
0
1
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
