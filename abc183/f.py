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
        cls[y].update(cls[x])
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
        cls[x].update(cls[y])


def is_connected(x, y):
    return (find_root(x) == find_root(y))


def num_components():
    return sum(1 for x in range(NUM_VERTEX) if find_root(x) == x)


# end of libs/unionfind.py

# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    global cls
    from collections import Counter
    # parse input
    N, Q = map(int, input().split())
    init_unionfind(N)
    CS = list(map(int, input().split()))
    cls = [Counter([CS[i] - 1]) for i in range(N)]
    # debug(cls, msg=":cls")
    for _q in range(Q):
        typ, a, b = map(int, input().split())
        if typ == 1:
            unite(a - 1, b - 1)
        else:
            root = find_root(a - 1)
            # debug(cls, root, msg=":cls, root")
            print(cls[root].get(b - 1, 0))


# tests
T1 = """
5 5
1 2 3 2 1
1 1 2
1 2 5
2 1 1
1 3 4
2 3 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
0
"""

T2 = """
5 4
2 2 2 2 2
1 1 2
1 1 3
1 2 3
2 2 2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
3
"""

T3 = """
12 9
1 2 3 1 2 3 1 2 3 1 2 3
1 1 2
1 3 4
1 5 6
1 7 8
2 2 1
1 9 10
2 5 6
1 4 8
2 6 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
1
0
0
"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
            print(k)
            doctest.run_docstring_examples(g[k], g, name=k)


def as_input(s):
    "use in test, use given string as input file"
    import io
    f = io.StringIO(s.strip())
    g = globals()
    g["input"] = lambda: bytes(f.readline(), "ascii")
    g["read"] = lambda: bytes(f.read(), "ascii")


if __name__ == "__main__":
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    sys.setrecursionlimit(10 ** 6)
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()
    sys.exit()

# end of snippets/main.py
