# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(R1, C1, R2, C2, phase=0):
    # debug(R1, C1, msg=":R1, C1")
    if R1 == R2 and C1 == C2:
        return 0
    if R1 + C1 == R2 + C2:
        return 1
    if R1 - C1 == R2 - C2:
        return 1
    if abs(R1 - R2) + abs(C1 - C2) <= 3:
        return 1

    d1 = abs(R1 + C1 - R2 - C2)
    d2 = abs(R1 - C1 - R2 + C2)
    if d1 > d2:
        d = R1 + C1 - R2 - C2
        d //= 2
        R1 -= d
        C1 -= d
        return solve(R1, C1, R2, C2) + 1
    else:
        d = R1 - C1 - R2 + C2
        d //= 2
        R1 -= d
        C1 += d
        return solve(R1, C1, R2, C2) + 1


def main():
    # parse input
    R1, C1 = map(int, input().split())
    R2, C2 = map(int, input().split())
    print(solve(R1, C1, R2, C2))


# tests
T1 = """
1 1
5 6
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
1 1
1 200001
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
2
"""

T3 = """
2 3
998244353 998244853
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
3
"""

T4 = """
1 1
1 1
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
0
"""

T5 = """
1 1
1 6
"""
TEST_T5 = """
>>> as_input(T5)
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
