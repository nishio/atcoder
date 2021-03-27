# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    cx = (x0 + x2) / 2
    cy = (y0 + y2) / 2
    v = (x0 - cx) + (y0 - cy) * 1j
    from math import sin, cos, pi
    rot = cos(2 * pi / N) + sin(2 * pi / N) * 1j
    v *= rot
    x1 = cx + v.real
    y1 = cy + v.imag

    print(x1, y1)

# tests
T1 = """
4
1 1
2 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2.00000000000 1.00000000000
"""
T2 = """
6
5 3
7 4
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5.93301270189 2.38397459622
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