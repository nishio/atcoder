# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N, M = map(int, input().split())
    edges = []
    for _i in range(M):
        edges.append(tuple(map(int, input().split())))

    ccs = [[1]]
    # vcc = [None] * N
    # vcc[0] = 0

    ret = 18

    def visit(pos):
        nonlocal ret
        debug(pos, ccs, msg=":pos")
        if pos == N + 1:
            if len(ccs) < ret:
                ret = len(ccs)
            return
        if len(ccs) >= ret:
            return

        for cc in ccs:
            if all((v, pos) in edges for v in cc):
                # can join the cc
                cc.append(pos)
                visit(pos + 1)
                cc.pop()

        # create new cc
        # cid = len(ccs)
        ccs.append([pos])
        # vcc[pos - 1] = cid
        visit(pos + 1)

    visit(2)
    print(ret)

# print(solve(SOLVE_PARAMS))


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
