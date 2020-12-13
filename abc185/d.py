# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    N, M = map(int, input().split())
    AS = list(map(int, input().split()))
    AS.append(0)
    AS.append(N + 1)
    AS.sort()
    # debug(AS, msg=":AS")
    DS = []
    for i in range(M + 1):
        d = AS[i + 1] - AS[i]
        if d > 1:
            DS.append(d - 1)
    if not DS:
        print(0)
        return
    # debug(DS, msg=":DS")
    k = min(DS)
    # debug(k, msg=":k")
    ret = 0
    for d in DS:
        ret += (d - 1) // k + 1
    print(ret)


# tests
T1 = """
5 2
1 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T2 = """
13 3
13 3 9
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
6
"""

T3 = """
5 5
5 2 1 4 3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
"""

T4 = """
1 0

"""
TEST_T4 = """
>>> as_input(T4)
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
