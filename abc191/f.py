# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    from math import gcd
    N = int(input())
    AS = list(map(int, input().split()))
    minA = min(AS)
    ALL = set(AS)
    NEW = set(AS)
    while NEW:
        next = set()
        for x in ALL:
            for y in NEW:
                next.add(gcd(x, y))
        ALL.update(NEW)
        NEW = next - ALL
    ret = 1
    for x in ALL:
        if x < minA:
            ret += 1

    print(ret)


# tests
T1 = """
3
6 9 12
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
4
8 2 12 6
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
"""

T3 = """
7
30 28 33 49 27 37 48
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
7
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
