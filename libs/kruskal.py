"""
Kruskal's algorithm / Maximum Spanning Tree (MST)
"""

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

def _from_edges(edges):
    edgelist = []
    for i in edges:
        for j in edges[i]:
            edgelist.append((edges[i][j], i, j))

    edgelist.sort()
    return edgelist


def kruskal(num_vertex, edges=None, edgelist=None):
    """
    edges: edges[i][j] = cost
    edgelist: [(cost, i, j)], sorted
    """
    if edges and not edgelist:
        edgelist = _from_edges(edges)

    init_unionfind(num_vertex)
    cost = 0
    for c, i, j in edgelist:
        if is_connected(i, j):
            continue
        unite(i, j)
        cost += c
    return cost

# --- end of library ---


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(V, E, edges):
    return kruskal(V, edgelist=sorted((c, i, j) for i, j, c in edges))


def main():
    # verified: https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_A
    V, E = map(int, input().split())
    edges = []
    for _i in range(E):
        edges.append(tuple(map(int, input().split())))
    print(solve(V, E, edges))


# tests
T1 = """
6 9
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
5
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
