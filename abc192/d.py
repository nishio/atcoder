# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def lessEqual(s, base, limit):
    ret = 0
    for c in s:
        ret *= base
        ret += int(c)
        if limit < ret:
            return False
    return True


def solve(X, M):
    sX = str(X)
    if len(sX) == 1:
        if X <= M:
            return 1
        else:
            return 0

    d = max(int(c)for c in str(X))
    v = int(sX, d + 1)
    if M < v:
        return 0

    left = d + 1
    start = left
    right = M + 1  # (1)

    while left < right - 1:
        x = (left + right) // 2
        if lessEqual(sX, x, M):
            left = x
        else:
            right = x
    return right - start


def anotherWay(X, M):
    from math import log, exp
    sX = str(X)
    return exp(log(M / int(sX[0])) / (len(sX) - 1)) - solve(X, M)


def main():
    X = int(input())
    M = int(input())

    print(solve(X, M))


# tests
T1 = """
22
10
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""
T2 = """
999
1500
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
3
"""
T3 = """
100000000000000000000000000000000000000000000000000000000000
1000000000000000000
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
1
"""
T4 = """
2
1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
0
"""
T5 = """
1
2
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
1
"""
T6 = """
10
1000
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
999
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
