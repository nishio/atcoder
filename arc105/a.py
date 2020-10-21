# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(XS):
    S = sum(XS)
    if S % 2 == 1:
        return False
    goal = S // 2
    for i in range(16):
        s = 0
        for j in range(4):
            if i & 1:
                s += XS[j]
            i >>= 1
        if s == goal:
            return True
    return False


def main():
    # parse input
    XS = list(map(int, input().split()))
    if solve(XS):
        print("Yes")
    else:
        print("No")


# tests
T1 = """
1 3 2 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
Yes
"""

T2 = """
1 2 4 8
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
No
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
