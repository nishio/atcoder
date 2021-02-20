# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    S = input().strip().decode('ascii')
    from string import ascii_uppercase, ascii_lowercase
    if all(c in ascii_uppercase for c in S[1::2]) and all(c in ascii_lowercase for c in S[::2]):
        print("Yes")
    else:
        print("No")


# tests
T1 = """
dIfFiCuLt
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""
T2 = """
eASY
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
"""
T3 = """
a
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
Yes
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
