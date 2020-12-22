# included from snippets/main.py
# included from libs/lowest_common_ancestor.py
"""
LCA: Lowest Common Ancestor
"""

MAX_DOUBLING = 20  # calc 2 ** 19 th parent


def parent_to_children(parent):
    from collections import defaultdict
    children = defaultdict(list)
    for i, p in enumerate(parent):
        children[p].append(i)
    return children


def children_to_parent(N, children, root):
    # Nth element is sentinel: parent[-1] == -1
    parent = [-1] * (N + 1)

    stack = [root]
    while stack:
        v = stack.pop()
        for c in children[v]:
            parent[c] = v
            stack.append(c)

    return parent


def construct(N, children, root, parent=None):
    "children: 0-origin vertex -> list of children vertex"
    global depth, parents
    # calc depth
    depth = [0] * N

    stack = [root]
    while stack:
        v = stack.pop()
        d = depth[v] + 1
        for c in children[v]:
            depth[c] = d
            stack.append(c)

    # doubling
    if not parent:
        parent = children_to_parent(N, children, root)
    parents = [parent]
    for _i in range(20):
        prev = parents[-1]
        # Nth element is sentinel: parent[-1] == -1
        next = [-1] * (N + 1)
        for i in range(N):
            next[i] = prev[prev[i]]
        parents.append(next)


def get_nth_parent(a, n):
    # find n-th parent of a
    p = a
    for i in range(MAX_DOUBLING):
        if n % 2:
            p = parents[i][p]
        n //= 2
    return p


def query(a, b):
    d = depth[a] - depth[b]
    if d > 0:
        a = get_nth_parent(a, d)
    elif d < 0:
        b = get_nth_parent(b, -d)

    if a == b:
        return a

    d = 0
    for i in range(MAX_DOUBLING):
        a2 = parents[MAX_DOUBLING - 1 - i][a]
        b2 = parents[MAX_DOUBLING - 1 - i][b]
        if a2 != b2:
            d += 2 ** (MAX_DOUBLING - 1 - i)
            a = a2
            b = b2
    return parents[0][a]


# end of libs/lowest_common_ancestor.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, PS, Q, QS):
    # to 0-origin
    PS = [p - 1 for p in PS]

    children = parent_to_children(PS)

    root = children[-2][0]
    construct(N, children, root, PS)

    for a, b in QS:
        a -= 1
        b -= 1
        d = depth[a] - depth[b]
        if d < 0:
            print("No")
            continue

        p = get_nth_parent(a, d)
        if p == b:
            print("Yes")
        else:
            print("No")


def main():
    # parse input
    N = int(input())
    PS = []
    for _n in range(N):
        PS.append(int(input()))
    Q = int(input())
    QS = []
    for _q in range(Q):
        QS.append(list(map(int, input().split())))
    solve(N, PS, Q, QS)


# tests
T1 = """
7
-1
1
1
2
2
3
3
6
7 1
4 1
2 3
5 1
5 2
2 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
Yes
No
Yes
Yes
No
"""

T2 = """
20
4
11
12
-1
1
13
13
4
6
20
1
1
20
10
8
8
20
10
18
1
20
18 14
11 3
2 13
13 11
10 15
9 5
17 11
18 10
1 16
9 4
19 6
5 10
17 8
15 8
5 16
6 20
3 19
10 12
5 13
18 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
No
No
No
No
No
No
Yes
No
Yes
No
No
No
Yes
No
Yes
No
No
No
Yes
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
