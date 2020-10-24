# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(H, W):
    if W % 3 == 0:
        return 0

    def f(x):
        ret = []
        a1 = H * x
        ar = H * (W - x)
        a2 = H // 2 * (W - x)
        a3 = ar - a2
        ret.append(max(a1, a2, a3) - min(a1, a2, a3))
        a2 = H * ((W - x) // 2)
        a3 = ar - a2
        ret.append(max(a1, a2, a3) - min(a1, a2, a3))
        return min(ret)

    return min(f(W // 3), f(W // 3 + 1))


def main():
    H, W = map(int, input().split())
    print(min(solve(H, W), solve(W, H)))


# tests
T1 = """
3 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
0
"""

T2 = """
4 5
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
2
"""

T3 = """
5 5
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
4
"""

T4 = """
100000 2
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
1
"""

T5 = """
100000 100000
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
50000
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
