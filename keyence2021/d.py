# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    group = []
    for i in range(N):
        P = 2 ** (2 ** i)
        group = [x * (P + 1) for x in group]
        group.append(P - 1)

    K = 2 ** N - 1
    print(K)
    for i in range(1, K + 1):
        x = 0
        for j in range(N):
            if (1 << j) & i:
                x = x ^ group[j]
        s = f"{x:0256b}"[-(2 ** N):]
        s = s.replace("0", "A").replace("1", "B")
        print(s)


# tests
T1 = """
1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
1
AB
"""

T2 = """
2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
3
ABAB
AABB
ABBA
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
