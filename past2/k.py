# included from snippets/main.py

def debug(*x, msg=""):
    import sys
    print(msg, *x, file=sys.stderr)


def solve(N, S, CS, DS):
    INF = 9223372036854775807
    table = [INF] * (N + 1)  # table[N] is sentinel
    table[0] = 0
    for i in range(N):
        new_table = [INF] * (N + 1)
        if S[i] == "(":
            d = 1
        else:
            d = -1

        for j in range(N):
            new_table[j] = min(
                table[j - d],  # no change
                table[j + d] + CS[i],  # change
                table[j] + DS[i],  # delete
            )
        table = new_table
    return table[0]


def main():
    # parse input
    N = int(input())
    S = input().strip().decode('ascii')
    CS = list(map(int, input().split()))
    DS = list(map(int, input().split()))
    print(solve(N, S, CS, DS))


# tests
T1 = """
3
))(
3 5 7
2 6 5
"""
TEST_T1 = """
>>> as_input(T1)
>>> main()
8
"""

T2 = """
1
(
10
20
"""
TEST_T2 = """
>>> as_input(T2)
>>> main()
20
"""

T3 = """
10
))())((()(
13 18 17 3 20 20 6 14 14 2
20 1 19 5 2 19 2 19 9 4
"""
TEST_T3 = """
>>> as_input(T3)
>>> main()
18
"""

T4 = """
4
()()
17 8 3 19
5 3 16 3
"""
TEST_T4 = """
>>> as_input(T4)
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
