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

# --- end of library ---


def main_yosupo():
    # verified: https://judge.yosupo.jp/problem/unionfind
    N, Q = [int(x) for x in input().split()]
    init_unionfind(N)
    for q in range(Q):
        typ, u, v = [int(x) for x in input().split()]
        if typ == 0:
            unite(u, v)
        else:
            print(1 if is_connected(u, v) else 0)


def main_abl():
    # verified: https://atcoder.jp/contests/abl/tasks/abl_c
    N, M = map(int, input().split())
    init_unionfind(N)
    for _i in range(M):
        a, b = map(int, input().split())
        unite(a - 1, b - 1)

    print(num_components() - 1)


# tests
T1 = """
3 1
1 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main_abl()
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


if __name__ == "__main__":
    # main_yosupo()
    # main_abl()
    _test()
