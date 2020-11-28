# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N):
    from math import sqrt
    x = int(sqrt(2 * N + 2)) - 1
    # debug(N, x, msg=":N, x")
    if (x + 2) * (1 + x) // 2 <= N + 1:
        x += 1

    return N - x + 1


def main():
    # parse input
    N = int(input())
    print(solve(N))


# tests
T1 = """
4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""

T01 = """
1
"""
TEST_T01 = """
>>> as_input(T01)
>>> main()
1
"""

T2 = """
109109109109109109
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
109109108641970782
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
