# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(a, b, x, y):
    ret = x
    if b < a:
        a -= 1

    if 2 * x < y:
        up = 2 * x
    else:
        up = y

    ret += abs(a - b) * up
    return ret


def main():
    # parse input
    a, b, x, y = map(int, input().split())
    print(solve(a, b, x, y))


# tests
T1 = """
2 1 1 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
"""

T2 = """
1 2 100 1
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
101
"""

T3 = """
1 100 1 100
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
199
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
