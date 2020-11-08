# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, AS):
    pos = 0
    dpos = 0
    maxdpos = 0
    ret = 0
    for a in AS:
        dpos += a
        if dpos > maxdpos:
            maxdpos = dpos
        if pos + maxdpos > ret:
            ret = pos + maxdpos
        pos += dpos

    return ret


def main():
    # parse input
    N = int(input())
    AS = list(map(int, input().split()))
    print(solve(N, AS))


# tests
T1 = """
3
2 -1 -2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
5
"""

T2 = """
5
-2 1 3 -1 -1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
2
"""

T3 = """
5
-1000 -1000 -1000 -1000 -1000
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
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
