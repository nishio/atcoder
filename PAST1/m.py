# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, AS, BS, CS, DS):
    left = 0.0
    right = 1000000.0
    while left < right - 10 ** -7:
        x = (left + right) / 2
        y = max(DS[i] - x * CS[i] for i in range(M))
        zs = list(sorted([BS[i] - x * AS[i] for i in range(N)], reverse=True))
        if y > zs[4]:
            y = y + sum(zs[:4])
        else:
            y = sum(zs[:5])

        if y >= 0:
            left = x
        else:
            right = x
    return left


def main():
    N, M = map(int, input().split())
    AS = []
    BS = []
    CS = []
    DS = []
    for _n in range(N):
        a, b = map(int, input().split())
        AS.append(a)
        BS.append(b)
    for _m in range(M):
        c, d = map(int, input().split())
        CS.append(c)
        DS.append(d)

    print(solve(N, M, AS, BS, CS, DS))


# tests
T1 = """
6 2
10 30
20 60
10 10
30 100
50 140
40 120
10 3
30 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3.000000003633886
"""

T2 = """
6 2
1 20
1 3
32 100
1 1
1 2
2 5
10 100
96 874
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
9.000000014535544
"""

T3 = """
4 1
1 1
1 1
1 1
1 1
1 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
result
"""

T4 = """
4 1
1 100000
1 100000
1 100000
1 100000
1 100000
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
result
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
