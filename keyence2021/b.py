# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N, K = map(int, input().split())
    AS = list(map(int, input().split()))
    from collections import Counter
    count = Counter(AS)
    ret = 0
    while count[0] > 0 and K > 0:
        i = 0
        K -= 1
        while count[i] > 0:
            ret += 1
            count[i] -= 1
            i += 1

    print(ret)


# tests
T1 = """
4 2
0 1 0 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""

T2 = """
20 4
6 2 6 8 4 5 5 8 4 1 7 8 0 3 6 1 1 8 3 0
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
11
"""

T3 = """
3 2
0 0 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
3
"""

T4 = """
3 1
0 0 1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
2
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
