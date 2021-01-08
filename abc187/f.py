# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, edges):
    global cost
    ccs = [[1]]  # Connected Components
    ret = 18
    cost = 0

    def visit(pos):
        nonlocal ret
        global cost
        if pos == N + 1:
            if len(ccs) < ret:
                ret = len(ccs)
            return
        if len(ccs) >= ret:
            return

        for cc in ccs:
            cost += len(cc)
            if all((v, pos) in edges for v in cc):
                # can join the cc
                cc.append(pos)
                visit(pos + 1)
                cc.pop()

        # create new cc
        ccs.append([pos])
        visit(pos + 1)
        ccs.pop()

    visit(2)
    return ret


def main():
    N, M = map(int, input().split())
    edges = set()
    for _i in range(M):
        edges.add(tuple(map(int, input().split())))
    print(solve(N, edges))


def random_test1():
    from random import random, seed
    seed(1)
    N = 18
    for p in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        edges = []
        for i in range(1, N):
            for j in range(i, N + 1):
                if random() < p:
                    edges.append((i, j))
        debug(p, msg=":p")
        solve(N, edges)


def random_test2():
    from random import random, seed
    seed(1)
    N = 18
    best = 0
    for s in range(10000):
        seed(s)
        for p in [0.8]:  # [0.6, 0.7, 0.8]:
            edges = []
            for i in range(1, N):
                for j in range(i + 1, N + 1):
                    if random() < p:
                        edges.append((i, j))
            if not "solve":
                solve(N, edges)
            else:
                if s == 7186 and p == 0.8:
                    for i in range(1, N):
                        print([1 if (i, j) in edges else 0 for j in range(1, N + 1)])
            if cost > best:
                best = cost
                debug(s, p, cost, msg=":p")


def random_test3():
    from random import random, seed
    seed(1)
    N = 18
    best = 0
    for s in range(10000):
        seed(s)
        edges = []
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if j < 17 or random() < 0.8:
                    edges.append((i, j))
        if "solve":
            solve(N, edges)
        else:
            if s == 7850:
                for i in range(1, N):
                    print([1 if (i, j) in edges else 0 for j in range(1, N + 1)])
        if cost > best:
            best = cost
            debug(s, cost, msg=":p")


# tests
T1 = """
3 2
1 2
1 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
4 6
1 2
1 3
1 4
2 3
2 4
3 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
"""

T3 = """
10 11
9 10
2 10
8 9
3 4
5 8
1 8
5 6
2 5
3 6
6 9
1 9
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
5
"""

T4 = """
18 0
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
18
"""

T5 = """
17 0
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
17
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
