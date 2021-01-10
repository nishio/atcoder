# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    AS = list(map(int, input().split()))
    PS = range(2 ** N)
    for _r in range(N - 1):
        newPS = []
        for i in range(0, len(PS), 2):
            if AS[PS[i]] > AS[PS[i + 1]]:
                newPS.append(PS[i])
            else:
                newPS.append(PS[i + 1])
        PS = newPS
    if AS[PS[0]] > AS[PS[1]]:
        print(PS[1] + 1)
    else:
        print(PS[0] + 1)


# tests
T1 = """
2
1 4 2 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
2
3 1 5 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
"""

T3 = """
4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4
"""
TEST_T3 = """
>>> as_input(T3)
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
