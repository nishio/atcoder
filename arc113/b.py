# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    A, B, C = map(int, input().split())
    doubling = [B % 20]
    for i in range(32):
        doubling.append(
            (doubling[-1] ** 2) % 20
        )
    BC = 1
    for i in range(32):
        if C % 2:
            BC *= doubling[i]
            BC %= 20
        C //= 2

    if BC == 0:
        BC = 20

    ret = (A % 10) ** BC
    ret %= 10
    print(ret)


# tests
T1 = """
4 3 2
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
4
"""
T2 = """
1 2 3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
1
"""
T3 = """
3141592 6535897 9323846
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
2
"""

T4 = """
2 10 1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
4
"""
T5 = """
2 20 1
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
6
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
