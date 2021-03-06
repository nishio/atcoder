# included from snippets/main.py
def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(SOLVE_PARAMS):
    pass


def main():
    N = int(input())
    AS = list(map(int, input().split()))
    sumAS = sum(AS)
    sumSq = sum(a * a for a in AS)
    # muls = (sumAS * sumAS - sumSq) // 2
    # debug(sumAS, sumSq, muls, msg=":sumAS, sumSq, muls")
    print(N * sumSq - sumAS * sumAS)

# tests
T1 = """
3
2 8 4
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
56
"""
T2 = """
5
-5 8 9 -4 -3
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
950
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