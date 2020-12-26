# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    import re
    N = int(input())
    buf = []
    for _i in range(N):
        s = input().strip().decode('ascii')
        buf.append((int(s), re.match("^0*", "0001").span()[1], s))
    buf.sort()
    for x in buf:
        print(x[2])


# tests
T1 = """
5
2
1
01
1
0010
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
01
1
1
2
0010
"""

T2 = """
6
1111111111111111111111
00011111111111111111111
000000111111111111111111
0000000001111111111111111
00000000000011111111111111
000000000000000111111111111
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
000000000000000111111111111
00000000000011111111111111
0000000001111111111111111
000000111111111111111111
00011111111111111111111
1111111111111111111111
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
