# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, XS):
    from math import sqrt
    m = 0
    c = 0
    for x in XS:
        m += abs(x)
        c = max(c, abs(x))

    print(m)

    e = 0.0
    for x in XS:
        e += x * x
    print(sqrt(e))

    print(c)


def main():
    # parse input
    N = int(input())
    XS = list(map(int, input().split()))
    solve(N, XS)


# tests
T1 = """
2
2 -1

"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
2.236067977499790
2

"""


def _test():
    import doctest
    doctest.testmod()
    g = globals()
    for k in sorted(g):
        if k.startswith("TEST_"):
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
    if sys.argv[-1] == "-t":
        print("testing")
        _test()
        sys.exit()
    main()

# end of snippets/main.py
