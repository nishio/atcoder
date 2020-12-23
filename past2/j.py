# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(S):
    N = len(S)
    cur = 0
    ret = []

    def parse_palen():
        nonlocal cur
        cur += 1
        ret = []
        while cur < N:
            c = S[cur]
            if c == ")":
                s = "".join(ret)
                s2 = "".join(reversed(s))
                return s + s2
            elif c == "(":
                ret.append(parse_palen())
            else:
                ret.append(c)
            cur += 1

    while cur < N:
        c = S[cur]
        if c == "(":
            ret.append(parse_palen())
        else:
            ret.append(c)
        cur += 1
    return "".join(ret)


def main():
    S = input().strip().decode('ascii')
    print(solve(S))


# tests
T1 = """
(ab)c
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
abbac
"""

T2 = """
past
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
past
"""

T3 = """
(d(abc)e)()
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
dabccbaeeabccbad
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
