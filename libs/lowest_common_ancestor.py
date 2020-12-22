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
    for i in range(20):
        if n % 2:
            p = parents[i][p]
        n //= 2
    return p


@profile
def query(a, b):
    d = depth[a] - depth[b]
    if d > 0:
        a = get_nth_parent(a, d)
    elif d < 0:
        b = get_nth_parent(b, -d)

    if a == b:
        return a

    left = 0
    right = 2 ** (MAX_DOUBLING - 1)
    while left < right - 1:
        x = (left + right) // 2
        a2 = get_nth_parent(a, x)
        b2 = get_nth_parent(b, x)
        if a2 != b2:
            left = x
        else:
            right = x
    return get_nth_parent(a, right)

# --- end of library ---

# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, children, QS):
    construct(N, children, 0)
    for q in QS:
        print(query(*q))


def biased_test():
    N = 100000
    children = {}
    for i in range(N - 1):
        children[i] = [i + 1]
    children[99999] = []

    from random import randint
    QS = [(randint(0, N - 1), randint(0, N - 1)) for i in range(100000)]

    solve(N, children, QS)


def biased_test2():
    N = 100000
    children = {}
    for i in range(N):
        children[i] = []
    children[0] = [i for i in range(1, N)]

    from random import randint
    QS = [(randint(0, N - 1), randint(0, N - 1)) for i in range(100000)]

    solve(N, children, QS)


def main():
    # verified: https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C
    N = int(input())
    children = {}
    for n in range(N):
        xs = list(map(int, input().split()))
        children[n] = xs[1:]

    Q = int(input())
    QS = []
    for _q in range(Q):
        QS.append(tuple(map(int, input().split())))

    solve(N, children, QS)


# tests
T1 = """
8
3 1 2 3
2 4 5
0
0
0
2 6 7
0
0
4
4 6
4 7
4 3
5 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
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
    # main()
    biased_test2()
    sys.exit()

# end of snippets/main.py
