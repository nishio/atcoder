# included from libs/graph_to_tree.py
def graph_to_tree(N, edges, root):
    from collections import defaultdict
    children = defaultdict(list)
    parents = [None] * N
    root = 0
    parents[root] = root
    stack = [root]
    while stack:
        v = stack.pop()
        for u in edges[v]:
            if parents[u] is not None:
                # already visited
                continue
            parents[u] = v
            children[v].append(u)
            stack.append(u)
    return children, parents

# end of libs/graph_to_tree.py

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    from collections import defaultdict
    N = int(input())
    edges = defaultdict(list)
    AS = []
    BS = []
    for _i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        AS.append(a)
        BS.append(b)
        edges[a].append(b)
        edges[b].append(a)

    root = 0
    children, parents = graph_to_tree(N, edges, root)
    veterx_diff = [0] * N

    Q = int(input())
    for _q in range(Q):
        t, e, x = map(int, input().split())
        e -= 1
        a = AS[e]
        b = BS[e]
        if t == 1:
            if parents[a] == b:
                veterx_diff[a] += x
            else:
                veterx_diff[root] += x
                veterx_diff[b] -= x
        else:
            if parents[a] == b:
                veterx_diff[root] += x
                veterx_diff[a] -= x
            else:
                veterx_diff[b] += x

    finish = [0] * N

    stack = [(root, 0)]
    while stack:
        v, x = stack.pop()
        x += veterx_diff[v]
        finish[v] += x
        for c in children[v]:
            stack.append((c, x))

    print(*finish, sep="\n")


# tests
T1 = """
5
1 2
2 3
2 4
4 5
4
1 1 1
1 4 10
2 1 100
2 2 1000
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
11
110
1110
110
100
"""

T2 = """
7
2 1
2 3
4 2
4 5
6 1
3 7
7
2 2 1
1 3 2
2 2 4
1 6 8
1 3 16
2 4 32
2 1 64
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
72
8
13
26
58
72
5
"""

T3 = """
11
2 1
1 3
3 4
5 2
1 6
1 7
5 8
3 9
3 10
11 4
10
2 6 688
1 10 856
1 8 680
1 8 182
2 2 452
2 4 183
2 6 518
1 3 612
2 6 339
2 3 206
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
1657
1657
2109
1703
1474
1657
3202
1474
1247
2109
2559
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
