# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(A, B, C):
    MOD = 998_244_353
    a = A * (A + 1) // 2
    a %= MOD
    b = B * (B + 1) // 2
    b %= MOD
    c = C * (C + 1) // 2
    c %= MOD
    return (a * b) % MOD * c % MOD


def main():
    # parse input
    A, B, C = map(int, input().split())
    print(solve(A, B, C))


# tests
T1 = """
1 2 3
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
18
"""

T2 = """
1000000000 987654321 123456789
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
951633476
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
