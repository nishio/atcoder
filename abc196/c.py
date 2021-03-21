# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    S = int(input())
    SS = str(S)
    N = len(SS)
    ret = 0
    if N % 2 == 0:
        N //= 2
        A = int(SS[:N])
        B = int(SS[N:])
        ret += (A - 1) - (10 ** (N - 1) - 1)
        if A <= B:
            ret += 1
    else:
        N //= 2

    N -= 1
    while N > 0:
        ret += (10 ** N - 1) - (10 ** (N - 1) - 1)
        N -= 1
    
    print(ret)

# tests
T1 = """
33
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
3
"""
T2 = """
1333
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
13
"""
T3 = """
10000000
"""
TEST_T3 = """
>>> as_input(T3)
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