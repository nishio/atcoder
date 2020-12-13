# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N, M, T = map(int, input().split())
    c = N
    prev = 0
    for _m in range(M):
        A, B = map(int, input().split())
        c -= (A - prev)
        # debug(A, c, msg=":A, c")
        if c <= 0:
            print("No")
            return
        c += (B - A)
        c = min(c, N)
        # debug(B, c, msg=":B, c")
        prev = B

    c -= (T - prev)
    if c <= 0:
        print("No")
        return
    print("Yes")


# tests
T1 = """
10 2 20
9 11
13 17
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""

T2 = """
10 2 20
9 11
13 16
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
"""

T3 = """
15 3 30
5 8
15 17
24 27
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
Yes
"""

T4 = """
20 1 30
20 29
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
No
"""

T5 = """
20 1 30
1 10
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
No
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
