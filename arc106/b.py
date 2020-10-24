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
# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, AS, BS, CD):
    init_unionfind(N)
    for (c, d) in CD:
        unite(c - 1, d - 1)

    from collections import defaultdict
    sumA = defaultdict(int)
    sumB = defaultdict(int)
    for v in range(N):
        root = find_root(v)
        sumA[root] += AS[v]
        sumB[root] += BS[v]

    for k in sumA:
        if sumA[k] != sumB[k]:
            return "No"
    return "Yes"


def main():
    # parse input
    N, M = map(int, input().split())
    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))
    CD = [list(map(int, input().split())) for _i in range(M)]
    print(solve(N, M, AS, BS, CD))


# tests
T1 = """
3 2
1 2 3
2 2 2
1 2
2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""

T2 = """
1 0
5
5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
Yes
"""

T3 = """
2 1
1 1
2 1
1 2
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
No
"""

T4 = """
17 9
-905371741 -999219903 969314057 -989982132 -87720225 -175700172 -993990465 929461728 895449935 -999016241 782467448 -906404298 578539175 9684413 -619191091 -952046546 125053320
-440503430 -997661446 -912471383 -995879434 932992245 -928388880 -616761933 929461728 210953513 -994677396 648190629 -530944122 578539175 9684413 595786809 -952046546 125053320
2 10
6 12
9 11
11 5
7 6
3 15
3 1
1 9
10 4
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
Yes
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
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
