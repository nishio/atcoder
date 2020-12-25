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

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, Q, edges, QS, ordered_edges):
    from collections import defaultdict
    color = [0] * N
    uplink = [None] * N
    root = 0
    # graph to tree
    children, parents = graph_to_tree(N, edges, root)
    # ready lca
    construct(N, children, root, parents)

    def paint(start, end, c):
        cur = start
        while cur != end:
            if color[cur] == 0:
                color[cur] = c
                uplink[cur] = end
                cur = parents[cur]
            else:
                if query(uplink[cur], end) != end:
                    # uplink if avobe end
                    return
                cur = uplink[cur]

    for a, b, c in reversed(QS):
        a -= 1
        b -= 1
        lca = query(a, b)
        paint(a, lca, c)
        paint(b, lca, c)

    for frm, to in ordered_edges:
        if parents[frm] == to:
            print(color[frm])
        else:
            print(color[to])


def main():
    # parse input
    N, Q = map(int, input().split())
    from collections import defaultdict
    edges = defaultdict(list)
    ordered_edges = []
    for _i in range(N - 1):
        frm, to = map(int, input().split())
        edges[frm - 1].append(to - 1)  # -1 for 1-origin vertexes
        edges[to - 1].append(frm - 1)  # if bidirectional
        ordered_edges.append((frm - 1, to - 1))
    QS = []
    for _i in range(Q):
        QS.append(tuple(map(int, input().split())))
    solve(N, Q, edges, QS, ordered_edges)


# tests
T1 = """
4 2
1 2
1 3
2 4
2 3 10
1 2 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
5
10
0
"""

T2 = """
10 10
7 2
5 8
8 6
8 3
8 9
9 1
4 8
4 10
8 7
7 5 12773
2 6 74733
1 6 64470
7 2 41311
1 9 39776
4 8 71709
9 1 23551
4 6 29181
3 7 23742
8 4 54686
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
41311
12773
29181
23742
64470
23551
54686
0
23742
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
