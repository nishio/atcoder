# included from snippets/main.py


def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    S = input().strip().decode('ascii')
    from collections import defaultdict
    count = defaultdict(int)
    ret = 0
    prev = None
    count[S[-1]] += 1
    count[S[-2]] += 1
    for i in reversed(range(len(S) - 2)):
        # debug(count, msg=":count")
        if S[i] != prev and S[i] == S[i + 1] != S[i + 2]:
            d = (len(S) - 2) - i
            # debug(d, msg=":d")
            # debug(count[S[i]] - 1, msg=":count[S[i]] - 1")
            d -= count[S[i]] - 1  # except S[i + 1]
            ret += d
            # debug(d, ret, msg=":ret")
            count = defaultdict(int)
            p = len(S) - i
            # debug(p, msg=":p")
            count[S[i]] = p
            prev = S[i]
        else:
            count[S[i]] += 1
            prev = None

    print(ret)


# tests
T1 = """
accept
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""
T2 = """
atcoder
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
0
"""
T3 = """
anerroroccurred
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
16
"""
T4 = """
aabaabb
"""
TEST_T4 = """
>>> as_input(T4)
>>> main()
3
"""
T5 = """
aabaabaabb
"""
TEST_T5 = """
>>> as_input(T5)
>>> main()
4
"""
T6 = """
aabbaa
"""
TEST_T6 = """
>>> as_input(T6)
>>> main()
6
"""
T7 = """
aabab
"""
TEST_T7 = """
>>> as_input(T7)
>>> main()
2
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
