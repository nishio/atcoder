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
    return sum(1 for x in range(NUM_VERTEX) if find_root(x) == x)

# end of libs/unionfind.py

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    init_unionfind(400000 + 1)
    numEdge = [0] * (400000 + 1)

    for _i in range(N):
        a, b = map(int, input().split())
        ra = find_root(a)
        rb = find_root(b)
        if ra == rb:
            numEdge[ra] += 1
        else:
            unite(a, b)
            rc = find_root(a)
            numEdge[rc] = numEdge[ra] + numEdge[rb] + 1

    from collections import Counter
    ccs = Counter(find_root(a) for a in range(1, 400000 + 1))
    ret = 0
    for cc in ccs:
        V = ccs[cc]
        E = numEdge[cc]
        if E == V - 1:
            ret += V - 1
        else:
            ret += V

    print(ret)


# tests
T1 = """
4
1 2
1 3
4 2
2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
2
111 111
111 111
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
"""

T3 = """
12
5 2
5 6
1 2
9 7
2 7
5 5
4 2
6 7
2 2
7 8
9 7
1 8
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
8
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
