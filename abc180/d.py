# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(X, Y, A, B):
    # debug(X, Y, A, B, msg=":X, Y, A, B")
    AX = X
    a_count = 0
    ret = 0
    while AX < Y:
        rest = Y - 1 - AX
        # debug(rest, msg=":rest")
        b_count = rest // B
        ret = max(ret, a_count + b_count)
        # debug(ret, msg=":ret")
        a_count += 1
        AX *= A

    return ret


def main():
    # parse input
    X, Y, A, B = map(int, input().split())
    print(solve(X, Y, A, B))


# tests
T1 = """
4 20 2 10
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
1 1000000000000000000 10 1000000000
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1000000007
"""

T3 = """
1 5 2 1000
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
2
"""

T4 = """
1 10 100 1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
8
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
