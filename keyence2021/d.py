# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    if N == 1:
        print("1\nAB")
        return
    from math import gcd
    M = 2 ** N - 1
    K = 2 ** (N - 1) - 1
    g = M * K // gcd(M, K)
    start = 0
    S = "A" * K + "B" * (K + 1)
    print(g)
    for i in range(g):
        print("A" + "".join(S[(i + start) % M] for i in range(M)))
        start += K


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
AABB
ABBA
ABAB
"""

T3 = """
3
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
21
AAAABBBB
ABBBBAAA
ABAAABBB
AABBBBAA
ABBAAABB
AAABBBBA
ABBBAAAB
AAAABBBB
ABBBBAAA
ABAAABBB
AABBBBAA
ABBAAABB
AAABBBBA
ABBBAAAB
AAAABBBB
ABBBBAAA
ABAAABBB
AABBBBAA
ABBAAABB
AAABBBBA
ABBBAAAB
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
