# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, M, AS, BS):
    if M > N:
        N, M = M, N
        AS, BS = BS, AS

    table = list(range(N + 1))
    # debug(table, msg=":table")
    for m in range(1, M + 1):
        newtable = [0] * (N + 1)
        prev = newtable[0] = m
        for n in range(1, N + 1):
            if AS[-n] == BS[-m]:
                d = 0
            else:
                d = 1

            prev = newtable[n] = min(
                prev + 1,
                table[n - 1] + d,
                table[n] + 1
            )
        table = newtable
        # debug(table, msg=":table")
    return table[-1]


def main():
    # parse input
    N, M = map(int, input().split())
    AS = list(map(int, input().split()))
    BS = list(map(int, input().split()))
    print(solve(N, M, AS, BS))


# tests
T1 = """
4 3
1 2 1 3
1 3 1
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
2
"""

T2 = """
5 5
1 1 1 1 1
2 2 2 2 2
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
5
"""

T3 = """
5 5
1 1 1 1 1
1 1 1 1 1
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
0
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
