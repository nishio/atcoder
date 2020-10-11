# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, XS):
    used = [0] * (200_000 + 1)
    cur = 0
    for i in range(N):
        used[XS[i]] = 1
        while used[cur]:
            cur += 1
        print(cur)


def main():
    # parse input
    N = int(input())
    XS = list(map(int, input().split()))
    solve(N, XS)


# tests
T1 = """
4
1 1 0 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
0
0
2
3
"""

T2 = """
10
5 4 3 2 1 0 7 7 6 6
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
0
0
0
0
6
6
6
8
8
"""

T3 = """
1
0
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
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
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
