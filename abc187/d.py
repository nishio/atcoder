# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N = int(input())
    # AS = []
    # BS = []
    sumA = 0
    diff = []
    for _i in range(N):
        a, b = map(int, input().split())
        # AS.append(a)
        # BS.append(b)
        sumA += a
        diff.append(2 * a + b)

    diff.sort()
    ret = 0
    while sumA >= 0:
        ret += 1
        d = diff.pop()
        sumA -= d
    print(ret)


# tests
T1 = """
4
2 1
2 2
5 1
1 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
5
2 1
2 1
2 1
2 1
2 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
3
"""

T3 = """
1
273 691
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
