# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    AS = list(map(int, input().split()))
    AS.sort()
    DS = []
    for i in range(N - 1):
        DS.append(AS[i + 1] - AS[i])
    ret = 0
    for i in range(N - 1):
        ret += DS[i] * (N - 1 - i) * (i + 1)
    print(ret)


# tests
T1 = """
3
5 1 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
8
"""

T2 = """
5
31 41 59 26 53
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
176
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
