# included from snippets/main.py

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
    return sum(1 for x in range(NUM_VERTEX) if find_root(x) == x)


# end of libs/unionfind.py
def solve(N, M, LARGE, SMALL):
    from math import sqrt
    # from collections import defaultdict
    # edges = defaultdict(dict)
    edges = []
    for i in range(N):
        x1, y1, c1 = LARGE[i]
        for j in range(i + 1, N):
            x2, y2, c2 = LARGE[j]
            d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            if c1 != c2:
                d *= 10
            # edges[i][j] = d
            # edges[j][i] = d
            edges.append((d, i, j))
    large_edges = edges[:]

    INF = 9223372036854775807
    ret = INF
    for subset in range(2 ** M):
        edges = large_edges[:]
        for m in range(M):
            if subset & (1 << m):
                x2, y2, c2 = SMALL[m]
                for i in range(N):
                    x1, y1, c1 = LARGE[i]
                    d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    if c1 != c2:
                        d *= 10
                    edges.append((d, i, N + m))

        init_unionfind(N + M)
        edges.sort()
        cost = 0
        for d, i, j in edges:
            if is_connected(i, j):
                continue
            unite(i, j)
            cost += d
        ret = min(ret, cost)
    return ret


def main():
    N, M = map(int, input().split())
    LARGE = []
    for _n in range(N):
        LARGE.append(tuple(map(int, input().split())))
    SMALL = []
    for _m in range(M):
        SMALL.append(tuple(map(int, input().split())))
    print(solve(N, M, LARGE, SMALL))


# tests
T1 = """
3 1
0 0 1
0 1 1
1 0 1
1 1 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2.0
"""

T2 = """
3 1
0 10 1
10 0 2
10 20 3
10 10 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
210.0
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
