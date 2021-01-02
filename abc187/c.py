# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    # parse input
    posi = set()
    nega = set()
    N = int(input())
    for _i in range(N):
        s = input().strip().decode('ascii')
        if s[0] == "!":
            nega.add(s[1:])
        else:
            posi.add(s)
    # debug(posi, nega, msg=":posi, nega")
    for s in posi:
        if s in nega:
            print(s)
            return
    print("satisfiable")


# tests
T1 = """
6
a
!a
b
!c
d
!d
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
d
"""

T2 = """
10
red
red
red
!orange
yellow
!blue
cyan
!green
brown
!gray
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
satisfiable
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
