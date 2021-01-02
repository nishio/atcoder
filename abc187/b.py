# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N = int(input())
    points = []
    ret = 0
    for _i in range(N):
        x, y = map(int, input().split())
        for x2, y2 in points:
            if - 1 <= (y2 - y) / (x2 - x) <= 1:
                ret += 1

        points.append((x, y))

    print(ret)


# tests
T1 = """
3
0 0
1 2
2 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
1
-691 273
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""

T3 = """
10
-31 -35
8 -36
22 64
5 73
-14 8
18 -58
-41 -85
1 -88
-21 -85
-11 82

"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
11
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
