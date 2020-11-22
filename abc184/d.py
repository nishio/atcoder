# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(A, B, C):
    cache = {}

    def f(x):
        if 100 in x:
            return 0
        if x in cache:
            return cache[x]
        a, b, c = x
        ret = 1
        if a:
            y = tuple(sorted((a + 1, b, c)))
            ret += f(y) * a / (a + b + c)
        if b:
            y = tuple(sorted((a, b + 1, c)))
            ret += f(y) * b / (a + b + c)
        if c:
            y = tuple(sorted((a, b, c + 1)))
            ret += f(y) * c / (a + b + c)
        cache[x] = ret
        return ret
    return f((A, B, C))


def main():
    # parse input
    A, B, C = map(int, input().split())
    print(solve(A, B, C))


# tests
T1 = """
99 99 99
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1.0
"""

T2 = """
98 99 99
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1.3310810810810811
"""

T3 = """
0 0 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
99.0
"""

T4 = """
31 41 59
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
91.83500820215889
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
