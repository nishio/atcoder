# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N, W = map(int, input().split())
    diff = [0] * 20_0010
    for _i in range(N):
        S, T, P = map(int, input().split())
        diff[S] += P
        diff[T] -= P
    usage = 0
    for v in diff:
        usage += v
        if usage > W:
            print("No")
            return
    print("Yes")


# tests
T1 = """
4 10
1 3 5
2 4 4
3 10 6
2 4 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
No
"""

T2 = """
4 10
1 3 5
2 4 4
3 10 6
2 3 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
Yes
"""

T3 = """
6 1000000000
0 200000 999999999
2 20 1
20 200 1
200 2000 1
2000 20000 1
20000 200000 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
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
